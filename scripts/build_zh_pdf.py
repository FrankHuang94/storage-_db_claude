#!/usr/bin/env python3
"""Build a print-ready PDF of the Simplified Chinese edition ("Chinese translation/").

Pipeline: Mermaid blocks pre-rendered to SVG with CJK fonts (mmdc) -> each chapter converted with
pandoc (GFM, footnote ids prefixed per chapter) -> links rewritten (chapters become in-PDF anchors,
images absolute file paths) -> one HTML book with cover, preface, table of contents, part dividers,
chapters and glossary -> Chromium (Playwright) prints A4 PDF with header/footer and bookmarks.
Two passes: the first PDF is scanned with pdftotext to find each chapter's page so the table of
contents can show real page numbers.

Usage: python3 scripts/build_zh_pdf.py [--out PATH]
Requires: pandoc, mmdc (@mermaid-js/mermaid-cli), node + playwright, pdftotext, Noto CJK fonts.
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from atlas_lib import ROOT, load_registry  # noqa: E402

ZH = ROOT / "Chinese translation"
OUT_DEFAULT = ZH / "pdf" / "Everpure-Tech-Atlas-zh-CN.pdf"
CHROME = "/opt/pw-browsers/chromium"

PART_TITLES_ZH = {
    "0": "第 0 部分 · 从这里开始",
    "1": "第 1 部分 · 存储基础",
    "2": "第 2 部分 · 协议与网络",
    "3": "第 3 部分 · 存储系统架构",
    "4": "第 4 部分 · Everpure",
    "5": "第 5 部分 · AI 存储",
    "6": "第 6 部分 · 行业与竞争",
    "7": "第 7 部分 · 历史与未来",
    "8": "第 8 部分 · 对话工具箱",
}

CSS = r"""
@page { size: A4; margin: 20mm 17mm 20mm 17mm; }
html { font-size: 10.2pt; }
body { font-family: "Noto Serif CJK SC", "Noto Serif", serif; color: #1a1a1a; line-height: 1.72;
       text-align: justify; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1, h2, h3, h4, .cover, .toc, .part-page, th, figcaption, .src, summary {
       font-family: "Noto Sans CJK SC", "Noto Sans", sans-serif; }
h1 { font-size: 21pt; line-height: 1.35; color: #0b3a5c; margin: 0 0 6mm 0; padding-bottom: 3mm;
     border-bottom: 2px solid #0072B2; break-before: page; }
h2 { font-size: 14pt; color: #0b3a5c; margin: 8mm 0 3mm 0; break-after: avoid; }
h3 { font-size: 11.6pt; color: #333; margin: 6mm 0 2mm 0; break-after: avoid; }
h4 { font-size: 10.6pt; margin: 4mm 0 1.5mm 0; break-after: avoid; }
p { margin: 0 0 2.6mm 0; orphans: 3; widows: 3; }
a { color: #0060a0; text-decoration: none; }
ul, ol { margin: 0 0 3mm 0; padding-left: 6mm; }
li { margin-bottom: 1mm; }
blockquote { margin: 3mm 0; padding: 2mm 4mm; border-left: 3px solid #0072B2; background: #f3f7fb;
             color: #333; font-size: 9.4pt; }
blockquote p { margin: 0.8mm 0; }
code { font-family: "Noto Sans Mono CJK SC", "DejaVu Sans Mono", monospace; font-size: 8.6pt;
       background: #f2f2f2; padding: 0 1px; border-radius: 2px; }
pre { font-size: 8.2pt; background: #f6f6f6; border: 1px solid #ddd; padding: 2.5mm; white-space: pre-wrap;
      word-break: break-all; break-inside: avoid; }
pre code { background: none; }
table { border-collapse: collapse; width: 100%; margin: 3mm 0 4mm 0; font-size: 8.2pt; line-height: 1.45;
        text-align: left; break-inside: auto; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th { background: #e8eef4; color: #0b3a5c; font-weight: 700; }
th, td { border: 1px solid #c9d3dd; padding: 1.2mm 1.6mm; vertical-align: top; word-break: break-word; }
tbody tr:nth-child(even) td { background: #fafbfc; }
img { max-width: 100%; max-height: 210mm; display: block; margin: 3mm auto 1.5mm auto; break-inside: avoid; }
p:has(> img) { text-align: center; margin: 0; }
em { font-style: normal; color: #444; }
p > em:only-child { display: block; font-size: 8.8pt; color: #555; text-align: center; margin: 0 0 3mm 0; }
strong { font-weight: 700; color: #111; }
hr { border: none; border-top: 1px solid #ccc; margin: 5mm 0; }
section.footnotes, .footnotes { font-size: 7.6pt; line-height: 1.45; color: #444; word-break: break-all; }
.footnotes hr { display: none; }
.footnotes ol { padding-left: 7mm; }
.footnotes li { margin-bottom: 0.6mm; }
a.footnote-ref sup, sup { font-size: 70%; line-height: 0; }
details { border: 1px solid #d5dde5; border-radius: 3px; padding: 1.5mm 3mm; margin: 0 0 2mm 0;
          break-inside: avoid; background: #fcfdfe; }
summary { font-weight: 700; color: #0b3a5c; font-size: 9.6pt; list-style: none; }
summary::-webkit-details-marker { display: none; }
details p { margin: 1mm 0 0 0; font-size: 9.6pt; }
.src { font-size: 8pt; color: #666; margin: -3mm 0 4mm 0; }
/* cover */
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover .kicker { color: #0072B2; font-size: 12pt; letter-spacing: 2px; margin-bottom: 8mm; }
.cover .title { font-size: 34pt; font-weight: 700; color: #0b3a5c; line-height: 1.3; }
.cover .subtitle { font-size: 15pt; color: #333; margin-top: 6mm; }
.cover .meta { font-size: 10pt; color: #666; margin-top: 30mm; line-height: 1.9; }
/* toc */
.toc { break-before: page; }
.toc h1 { break-before: avoid; }
.toc .tp { font-weight: 700; color: #0b3a5c; margin: 4mm 0 1mm 0; font-size: 10.5pt; }
.toc .tc { display: flex; font-size: 9.6pt; line-height: 1.75; }
.toc .tc a { color: #1a1a1a; }
.toc .tc .dots { flex: 1; border-bottom: 1px dotted #999; margin: 0 2mm 1.4mm 2mm; }
.toc .tc .pg { min-width: 9mm; text-align: right; color: #333; }
/* part divider */
.part-page { break-before: page; height: 240mm; display: flex; flex-direction: column; justify-content: center; }
.part-page .pt { font-size: 26pt; font-weight: 700; color: #0b3a5c; border-left: 6px solid #0072B2;
                 padding-left: 6mm; }
.part-page .pe { font-size: 12pt; color: #666; padding-left: 7.5mm; margin-top: 3mm; }
.part-page ul { margin-top: 10mm; padding-left: 8mm; font-size: 10.5pt; line-height: 2; color: #333; }
.preface h1 { break-before: page; }
.mk { color: #ffffff; font-size: 1px; line-height: 0; position: absolute; }
"""

LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"{cmd[0]} failed: {r.stderr[-1500:]}")
    return r.stdout


def anchor_for(path: Path) -> str:
    return "ch-" + re.sub(r"[^a-z0-9]+", "-", path.stem.lower())


def rewrite_links(md: str, src: Path, chapter_files: dict[Path, str]) -> str:
    def fix(m):
        bang, text, target = m.group(1), m.group(2), m.group(3)
        if re.match(r"^[a-z]+:", target):
            return m.group(0)
        if target.startswith("#"):
            return m.group(0)
        path_part, _, frag = target.partition("#")
        dest = (src.parent / path_part).resolve()
        if bang:
            return f"![{text}]({dest.as_uri()})" if dest.exists() else m.group(0)
        if dest in chapter_files:
            return f"[{text}](#{chapter_files[dest]})"
        return text  # links to English originals, CSVs, etc. -> plain text in print
    return LINK.sub(fix, md)


def render_mermaid(md_text: str, workdir: Path, stem: str) -> str:
    if "```mermaid" not in md_text:
        return md_text
    inp = workdir / f"{stem}.in.md"
    out = workdir / f"{stem}.out.md"
    inp.write_text(md_text)
    run(["mmdc", "-q", "-p", str(workdir / "pc.json"), "-c", str(workdir / "mcfg.json"), "-b", "white",
         "-e", "svg", "-i", str(inp), "-o", str(out)], timeout=900)
    text = out.read_text()
    # make generated image paths absolute
    return re.sub(r"!\[([^\]]*)\]\(\./([^)]+)\)", lambda m: f"![{m.group(1)}]({(workdir / m.group(2)).as_uri()})",
                  text)


def md_to_html(md_text: str, prefix: str) -> str:
    out = run(["pandoc", "-f", "gfm-tex_math_dollars+footnotes", "-t", "html5",
               "--wrap=none", f"--id-prefix={prefix}-"], input=md_text)
    out = out.replace("<details>", "<details open>")
    return out


def build_html(workdir: Path, page_map: dict[str, int] | None) -> str:
    parts = load_registry()
    chapters = []
    chapter_files: dict[Path, str] = {}
    for part in parts:
        for ch in part["chapters"]:
            zp = (ZH / ch["path"].relative_to(ROOT)).resolve()
            chapter_files[zp] = anchor_for(zp)
            chapters.append((part, ch, zp))
    gloss = (ZH / "docs" / "glossary.md").resolve()
    chapter_files[gloss] = "ch-glossary"

    def title_of(p: Path) -> str:
        first = p.read_text().lstrip().splitlines()[0]
        return re.sub(r"^#\s*", "", first).strip()

    body = []
    # cover
    body.append("""<div class="cover"><div class="kicker">简体中文参考译本</div>
<div class="title">Everpure 技术图谱</div><div class="subtitle">Everpure Tech Atlas · 存储与 AI 存储战略知识库</div>
<div class="meta">面向企业发展 / 战略团队的存储与 AI 存储读本<br>英文原版与本译本均位于 GitHub 仓库 FrankHuang94/storage-_db_claude<br>
内容截至 2026-11-01 · 本译本仅供参考，如有出入以英文原文为准</div></div>""")
    # preface: the "关于本中文译本" section of the Chinese README
    readme = (ZH / "README.md").read_text()
    m = re.search(r"^##\s*关于本中文译本.*?(?=^##\s)", readme, flags=re.S | re.M)
    if m:
        pre = "# 关于本中文译本\n\n" + m.group(0).split("\n", 1)[1]
        pre = rewrite_links(pre, ZH / "README.md", chapter_files)
        body.append('<div class="preface">' + md_to_html(pre, "preface") + "</div>")
    # toc
    toc = ['<div class="toc"><h1>目录</h1>']
    for part in parts:
        toc.append(f'<div class="tp">{html.escape(PART_TITLES_ZH.get(part["id"], part["title"]))}</div>')
        for ch in part["chapters"]:
            zp = (ZH / ch["path"].relative_to(ROOT)).resolve()
            a = chapter_files[zp]
            pg = str(page_map.get(a, "")) if page_map else "000"
            toc.append(f'<div class="tc"><a href="#{a}">{html.escape(title_of(zp))}</a><span class="dots"></span>'
                       f'<span class="pg">{pg}</span></div>')
    pg = str(page_map.get("ch-glossary", "")) if page_map else "000"
    toc.append(f'<div class="tp">附录</div><div class="tc"><a href="#ch-glossary">术语表（Glossary）</a>'
               f'<span class="dots"></span><span class="pg">{pg}</span></div></div>')
    body.append("\n".join(toc))
    # parts + chapters
    for part in parts:
        items = "".join(f"<li>{html.escape(title_of((ZH / c['path'].relative_to(ROOT)).resolve()))}</li>"
                        for c in part["chapters"])
        eng = html.escape(part["title"])
        body.append(f'<div class="part-page"><div class="pt">{html.escape(PART_TITLES_ZH[part["id"]])}</div>'
                    f'<div class="pe">{eng}</div><ul>{items}</ul></div>')
        for p_, ch, zp in [c for c in chapters if c[0] is part]:
            a = chapter_files[zp]
            body.append(chapter_html(zp, a, chapter_files, workdir))
    body.append(chapter_html(gloss, "ch-glossary", chapter_files, workdir))
    return ("<!DOCTYPE html><html lang='zh-CN'><head><meta charset='utf-8'><title>Everpure 技术图谱（简体中文参考译本）</title>"
            f"<style>{CSS}</style></head><body>" + "\n".join(body) + "</body></html>")


_cache: dict[str, str] = {}


def chapter_html(zp: Path, anchor: str, chapter_files, workdir: Path) -> str:
    if anchor in _cache:
        return _cache[anchor]
    md = zp.read_text()
    # source-reference line -> small plain note
    md = re.sub(r"^>\s*📄\s*英文原文：\[([^\]]+)\]\([^)]+\)(.*)$", lambda m: f"<p class=\"src\">英文原文：{m.group(1)}{m.group(2)}</p>",
                md, count=1, flags=re.M)
    md = render_mermaid(md, workdir, anchor)
    md = rewrite_links(md, zp, chapter_files)
    h = md_to_html(md, anchor)
    marker = f'<span class="mk">QQMK{anchor}QQ</span>'
    h = h.replace("</h1>", "</h1>" + marker, 1) if "</h1>" in h else marker + h
    out = f'<section class="chapter" id="{anchor}">{h}</section>'
    _cache[anchor] = out
    return out


NODE_PRINT = r"""
const { chromium } = require('playwright');
(async () => {
  const [html, pdf] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: process.env.CHROME || undefined, args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('file://' + html, { waitUntil: 'load', timeout: 0 });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: pdf, format: 'A4', printBackground: true, outline: true, tagged: true,
    displayHeaderFooter: true,
    headerTemplate: '<div style="font-family:Noto Sans CJK SC;font-size:7.5px;color:#888;width:100%;padding:0 17mm;text-align:right">Everpure 技术图谱 · 简体中文参考译本</div>',
    footerTemplate: '<div style="font-family:Noto Sans CJK SC;font-size:8px;color:#666;width:100%;text-align:center">第 <span class="pageNumber"></span> 页 / 共 <span class="totalPages"></span> 页</div>',
    margin: { top: '20mm', bottom: '20mm', left: '17mm', right: '17mm' }, timeout: 0 });
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
"""


def print_pdf(html_path: Path, pdf_path: Path, workdir: Path) -> None:
    js = workdir / "print.js"
    js.write_text(NODE_PRINT)
    env = dict(os.environ, NODE_PATH=run(["npm", "root", "-g"]).strip(),
               CHROME=CHROME if Path(CHROME).exists() else "")
    r = subprocess.run(["node", str(js), str(html_path), str(pdf_path)], env=env, capture_output=True, text=True,
                       timeout=3600)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:])


def find_pages(pdf_path: Path) -> dict[str, int]:
    """Map chapter anchors to the page carrying their invisible start marker (QQMK<anchor>QQ)."""
    pages = run(["pdftotext", str(pdf_path), "-"]).split("\f")
    found: dict[str, int] = {}
    for i, pg in enumerate(pages):
        for a in re.findall(r"QQMK(ch-[a-z0-9-]+)QQ", pg):
            found.setdefault(a, i + 1)
    return found


def main(argv: list[str]) -> int:
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else OUT_DEFAULT
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="zhpdf-"))
    (work / "pc.json").write_text(json.dumps({"executablePath": CHROME, "args": ["--no-sandbox", "--headless"]}))
    (work / "mcfg.json").write_text(json.dumps({"theme": "default", "themeVariables": {
        "fontFamily": "Noto Sans CJK SC, sans-serif", "fontSize": "14px"},
        "flowchart": {"htmlLabels": True}}))
    print("pass 1: rendering diagrams and chapters …", flush=True)
    html1 = work / "book1.html"
    html1.write_text(build_html(work, None))
    pdf1 = work / "pass1.pdf"
    print_pdf(html1, pdf1, work)
    pages = find_pages(pdf1)
    print(f"pass 1 done: {len(pages)} chapter start pages located", flush=True)
    html2 = work / "book2.html"
    html2.write_text(build_html(work, pages))
    print_pdf(html2, out, work)
    info = run(["pdfinfo", str(out)])
    npages = re.search(r"Pages:\s+(\d+)", info).group(1)
    print(f"wrote {out} ({npages} pages, {out.stat().st_size/1e6:.1f} MB); work dir {work}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Render the cloned ABOOL-PLATFORM profile/README.md faithfully as a website.
Content is NOT rewritten — markdown is converted 1:1, only wrapped in a styled shell.
Source: ~/workspace/ABOOL-PLATFORM/profile/README.md (git clone of ABOOL-PLATFORM/.github)
"""
import markdown, pathlib, html

src = pathlib.Path.home() / "workspace/ABOOL-PLATFORM/profile/README.md"
out_dir = pathlib.Path.home() / "workspace/abool-website"
out_dir.mkdir(parents=True, exist_ok=True)

md_text = src.read_text(encoding="utf-8")
body = markdown.markdown(md_text, extensions=["fenced_code", "tables", "sane_lists", "toc"])

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ABOOL — Agricultural Traceability &amp; Compliance Platform</title>
<meta name="description" content="ABOOL is an open-source digital infrastructure platform for agricultural supply-chain traceability, geospatial verification, EUDR compliance, and product provenance. Initially focused on Ethiopian coffee.">
<style>
:root{--green:#14532d;--green2:#166534;--leaf:#22c55e;--earth:#92400e;--coffee:#3b2314;--bg:#faf9f6;--card:#ffffff;--ink:#1c1917;--muted:#57534e;--line:#e7e5e4;--gold:#d97706}
*{box-sizing:border-box} html{scroll-behavior:smooth}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Inter,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;-webkit-font-smoothing:antialiased}
.topbar{background:var(--coffee);color:#fef3c7;font-size:13px;text-align:center;padding:8px 16px}
.topbar a{color:#fde68a}
header.site{position:sticky;top:0;z-index:50;background:rgba(20,83,45,.97);backdrop-filter:blur(8px);color:#fff}
.nav{max-width:1080px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:14px 20px;gap:12px;flex-wrap:wrap}
.logo{font-weight:800;font-size:22px;letter-spacing:.5px;color:#fff;text-decoration:none}
.logo span{color:var(--leaf)}
.nav-links{display:flex;gap:6px;flex-wrap:wrap}
.nav-links a{color:#dcfce7;text-decoration:none;font-size:14px;padding:6px 10px;border-radius:8px}
.nav-links a:hover{background:rgba(255,255,255,.14);color:#fff}
main{max-width:1080px;margin:0 auto;padding:28px 20px 64px}
article{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:36px 40px;box-shadow:0 8px 30px rgba(28,25,23,.06)}
article h1{font-size:clamp(26px,4.5vw,40px);line-height:1.2;color:var(--green);margin:.2em 0 .5em}
article h2{font-size:clamp(21px,3.4vw,28px);color:var(--green);border-bottom:2px solid #dcfce7;padding-bottom:8px;margin-top:1.6em}
article h3{font-size:19px;color:var(--coffee);margin-top:1.4em}
article a{color:var(--green2)}
article blockquote{border-left:4px solid var(--gold);background:#fffbeb;margin:1em 0;padding:12px 18px;border-radius:0 12px 12px 0;color:#44403c}
article pre{background:#1c1917;color:#e7e5e4;padding:18px;border-radius:14px;overflow-x:auto;font-size:13.5px;line-height:1.55}
article code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
article p code, article li code{background:#f0fdf4;border:1px solid #dcfce7;padding:1px 6px;border-radius:6px;font-size:.92em;color:var(--green)}
article hr{border:none;border-top:1px solid var(--line);margin:2em 0}
article ul,article ol{padding-left:1.4em}
article li{margin:.25em 0}
article table{border-collapse:collapse;width:100%;overflow-x:auto;display:block}
article th,article td{border:1px solid var(--line);padding:8px 12px;text-align:left}
footer{background:var(--coffee);color:#d6d3d1;padding:36px 20px;text-align:center;font-size:14px}
footer a{color:#fde68a}
footer .tag{font-size:18px;color:#fff;font-weight:700}
@media(max-width:640px){article{padding:22px 18px;border-radius:14px} .nav{justify-content:center;text-align:center} main{padding:16px 10px 48px}}
</style>
</head>
<body>
<div class="topbar">Website rendered from the cloned <a href="https://github.com/ABOOL-PLATFORM">github.com/ABOOL-PLATFORM</a> README &mdash; the platform code (web / api / mobile) has not been published yet.</div>
<header class="site"><div class="nav">
<a class="logo" href="#">ABOOL<span>.</span></a>
<nav class="nav-links">
<a href="#vision">Vision</a><a href="#core-platform">Core Platform</a><a href="#eudr-compliance">EUDR</a><a href="#coffee-passport">Coffee Passport</a><a href="#abol-mobile">Mobile</a><a href="#architecture">Architecture</a><a href="#roadmap">Roadmap</a>
</nav></div></header>
<main><article>
__BODY__
</article></main>
<footer>
<div class="tag">Trace the origin. Verify the land. Prove the product.</div>
<p>ABOOL &mdash; Agricultural Traceability &amp; Compliance Platform &middot; Initial Market: Ethiopia &middot; Primary Commodity: Coffee</p>
<p>Source: <a href="https://github.com/ABOOL-PLATFORM">github.com/ABOOL-PLATFORM</a> (cloned README, rendered as a website) &middot; Built for African Agriculture</p>
</footer>
</body>
</html>
"""
# markdown toc extension adds ids like "vision", "core-platform" etc. to headings — nav anchors rely on that.
(out_dir / "index.html").write_text(template.replace("__BODY__", body), encoding="utf-8")
# Also keep the raw source alongside for transparency
(out_dir / "README-source.md").write_text(md_text, encoding="utf-8")
print("built", out_dir / "index.html", len(body), "chars of rendered content")

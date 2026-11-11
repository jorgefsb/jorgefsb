#!/usr/bin/env python3
"""Arma README.md (EN) y README.es.md (ES) con medios reales para cada repo.

Estándar: docs/README-STANDARD.md. Los textos viven en data1.py, data2.py y
data3.py; cada cambio de copy se hace ahí, en los dos idiomas.

Uso:
  python3 tools/readme-kit/mkdocs.py --repos DIR_CON_LOS_CLONES \
      --captures DIR_DE_capture.py --outfit Outfit-Bold.woff2 \
      --inter Inter-Regular.woff2 --signature JorgeSuarez-A-oscuro-bicolor.svg \
      [--updated AAAA-MM-DD] [repo ...]

Fechas: la de las capturas sale de captured.txt (lo escribe capture.py y se
guarda en docs/readme/ de cada repo). La de "documentación actualizada" es la
del día en que se corre, o --updated. Ninguna fecha va escrita a mano aquí.
El About (descripción, sitio y topics) se revisa y se aplica con about.py.
"""
import argparse, datetime, re, sys, shutil, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE))
import build_assets as B
from data1 import REPOS1
from data2 import REPOS2
from data3 import REPOS3
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("--repos", required=True, help="carpeta con los repos clonados")
ap.add_argument("--captures", required=True, help="salida de capture.py")
ap.add_argument("--outfit", required=True)
ap.add_argument("--inter", required=True)
ap.add_argument("--signature", required=True, help="firma A del BrandKit (Maestros 1.0)")
ap.add_argument("--updated", default=datetime.date.today().isoformat(), help="fecha de actualización, AAAA-MM-DD (hoy por defecto)")
ap.add_argument("only", nargs="*")
A = ap.parse_args()

REPOS = REPOS1 + REPOS2 + REPOS3
ROOT = pathlib.Path(A.repos)
CAP = pathlib.Path(A.captures)
LANG = HERE.parent.parent / "assets" / "lang"
F = B.Fonts(A.outfit, A.inter)
MES = dict(es="ene feb mar abr may jun jul ago sep oct nov dic".split(),
           en="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())


def fecha(iso, lang):
    d = datetime.date.fromisoformat(iso.strip())
    return f"{d.day} {MES[lang][d.month - 1]} {d.year}"


DATE = {lang: fecha(A.updated, lang) for lang in ("es", "en")}

sig_src = pathlib.Path(A.signature).read_text()
SIG_VB = re.search(r'viewBox="([^"]+)"', sig_src).group(1)
SIG_INNER = sig_src[sig_src.index("</desc>") + 7: sig_src.rindex("</svg>")]


def wrap(s, text, f, size, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if s.tw(t, f, size) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines


def banner(r, lang):
    W, H = 1000, 270
    s = B.Svg(F, W, H, r["title"], r["promise"][lang])
    body, css = B.frame(W, H)
    s.css.append(css); s.add(B.GRAD); s.add(body)
    s.add(f'<g fill="{B.AMBER}" class="fade" style="{B.d(1.2)}"><rect x="24" y="24" width="8" height="8"/><rect x="40" y="24" width="8" height="8"/></g>')
    s.add(B.particles(s, 104, 126, 16, 170, .45, 5))
    s.add(B.monogram(s, 44, 66, 120))
    x = 204
    s.add(f'<g class="rise" style="{B.d(.3)}">' + s.text(x, 76, r["kicker"][lang], "o", 14, B.ACCENT, ls=3) + "</g>")
    ts = B.fit(s, r["title"], "o", 48, W - 56 - x, ls=-0.5, floor=30)
    s.add(f'<g class="rise" style="{B.d(.42)}">' + s.text(x, 128, r["title"], "o", ts, B.TEXT, ls=-0.5) + "</g>")
    lines = wrap(s, r["promise"][lang], "i", 19, W - 60 - x)
    assert len(lines) <= 2, (r["key"], lang, lines)
    for k, ln in enumerate(lines):
        s.add(f'<g class="rise" style="{B.d(.55 + k * .08)}">' + s.text(x, 162 + k * 27, ln, "i", 19, B.MUTED) + "</g>")
    chip = r["chip"][lang]
    cw = s.tw(chip, "o", 12, 1.4) + 26
    s.add(f'<g class="pop" style="{B.d(.9)}"><rect x="{x}" y="212" width="{cw:.1f}" height="28" rx="14" fill="{B.SURFACE}" stroke="{B.BORDER}"/>'
          + s.text(x + cw / 2, 230.5, chip, "o", 12, B.TEXT, ls=1.4, anchor="middle") + "</g>")
    sw = 270; sh = sw * 280.5 / 1168
    s.add(f'<g class="fade" style="{B.d(1.0)}"><svg x="{W - sw - 22}" y="{H - sh - 10:.1f}" width="{sw}" height="{sh:.1f}" viewBox="{SIG_VB}">{SIG_INNER}</svg></g>')
    return s.render()


def flow(r, lang):
    src, fmts, edit, out = r["flow"][lang]
    W, H = 1000, 300
    s = B.Svg(F, W, H, r["title"], " → ".join([src, " / ".join(fmts), edit, out]))
    body, css = B.frame(W, H)
    s.css.append(css); s.add(B.GRAD); s.add(body)

    def box(x, y, w, h, label, hot=False, delay=0.2, size=15):
        bg, fg, st = (B.ACCENT, B.INK, "none") if hot else (B.SURFACE, B.TEXT, B.BORDER)
        fs = B.fit(s, label, "o", size, w - 20, ls=1, floor=10)
        return (f'<g class="pop" style="{B.d(delay)}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{st}" stroke-width="1.5"/>'
                + s.text(x + w / 2, y + h / 2 + fs * .36, label, "o", fs, fg, ls=1, anchor="middle") + "</g>")

    def arrow(x1, y1, x2, y2, delay):
        return (f'<g class="fade" style="{B.d(delay)}"><path d="M{x1} {y1}L{x2 - 8} {y2}" stroke="{B.AMBER}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
                f'<path d="M{x2} {y2}l-10 -6v12Z" fill="{B.AMBER}"/></g>')

    s.add(box(50, 110, 190, 80, src, True, .2))
    ys = [40, 100, 160, 220]
    for k, (f_, y) in enumerate(zip(fmts, ys)):
        s.add(arrow(240, 150, 330, y + 22, .4 + k * .08))
        s.add(box(330, y, 190, 44, f_, False, .5 + k * .08, 13))
        s.add(arrow(520, y + 22, 610, 150, .8 + k * .08))
    s.add(box(610, 110, 170, 80, edit, False, 1.1))
    s.add(arrow(780, 150, 836, 150, 1.25))
    s.add(box(836, 110, 124, 80, out, True, 1.35, 14))
    return s.render()


def jpg(src, dst, maxw):
    im = Image.open(src).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(dst, quality=84, optimize=True, progressive=True)


L = dict(
    es=dict(tour="Recorrido real del sitio en vivo, grabado el {cap} en Chromium (1280×720). Sin retoque. Se reproduce una sola vez; recarga la página para verlo de nuevo.",
            shots="Capturas reales del sitio en vivo, {cap}: escritorio (1280×720) y móvil (390×780).",
            lock="Captura real de la pantalla de acceso, {cap}. El contenido cifrado no se muestra.",
            mp4="Ver el video MP4", desk="en escritorio", mob="en móvil", tourw="Recorrido de",
            foot='Hecho con amor ❤️🎮 por <a href="https://jorgesuarez.com.mx">JorgeSuarez.com.mx</a> · <a href="https://github.com/jorgefsb">Más proyectos</a> · <a href="./README.md">Read in English</a><br />Documentación actualizada el {upd}.',
            cfoot='Repositorio mantenido por <a href="https://github.com/jorgefsb">Jorge Suárez</a> · <a href="./README.md">Read in English</a> · Documentación actualizada el {upd}.',
            more="Más proyectos en"),
    en=dict(tour="Real walkthrough of the live site, recorded {cap} in Chromium (1280×720). No retouching. It plays once; reload the page to watch it again.",
            shots="Real screenshots of the live site, {cap}: desktop (1280×720) and mobile (390×780).",
            lock="Real screenshot of the access screen, {cap}. The encrypted content is not shown.",
            mp4="Watch the MP4 video", desk="on desktop", mob="on mobile", tourw="Walkthrough of",
            foot='Made with love ❤️🎮 by <a href="https://jorgesuarez.com.mx">JorgeSuarez.com.mx</a> · <a href="https://github.com/jorgefsb">More projects</a> · <a href="./README.es.md">Leer en español</a><br />Documentation updated on {upd}.',
            cfoot='Repository maintained by <a href="https://github.com/jorgefsb">Jorge Suárez</a> · <a href="./README.es.md">Leer en español</a> · Documentation updated on {upd}.',
            more="More projects at"),
)


def tour_block(r, lang, has):
    t = L[lang]
    if not has:
        return ""
    cap = fecha(r["_captured"], lang)
    return (f'<p align="center"><img src="docs/readme/tour.gif" width="720" alt="{t["tourw"]} {r["title"]}"></p>\n'
            f'<p align="center"><sub>{t["tour"].format(cap=cap)} <a href="docs/readme/tour.mp4">{t["mp4"]}</a></sub></p>\n')


def shots_block(r, lang, lock=False):
    t = L[lang]
    return (f'<p align="center">\n  <img src="docs/readme/desktop.jpg" width="620" alt="{r["title"]} {t["desk"]}">\n'
            f'  <img src="docs/readme/mobile.jpg" width="190" alt="{r["title"]} {t["mob"]}">\n</p>\n'
            f'<p align="center"><sub>{(t["lock"] if lock else t["shots"]).format(cap=fecha(r["_captured"], lang))}</sub></p>')


def rewrite_paths(md):
    def fix(p):
        if re.match(r"^(https?:|mailto:|#|/|data:)", p) or not p:
            return p
        p2 = p[2:] if p.startswith("./") else p
        return p2[5:] if p2.startswith("docs/") else "../" + p2
    md = re.sub(r"\]\(([^)\s]+)\)", lambda m: "](" + fix(m.group(1)) + ")", md)
    md = re.sub(r'(src|href)="([^"]+)"', lambda m: f'{m.group(1)}="{fix(m.group(2))}"', md)
    return md


def build(r):
    repo = ROOT / r["key"]
    dr = repo / "docs" / "readme"; dr.mkdir(parents=True, exist_ok=True)
    old = (repo / "README.md").read_text(encoding="utf-8")
    herdr = ""
    if r.get("herdr"):
        m = re.search(r"<!-- HERDR-CONTEXT:START -->.*?<!-- HERDR-CONTEXT:END -->", old, re.S)
        herdr = "\n" + m.group(0) + "\n" if m else ""
    # guía técnica: el README anterior se conserva íntegro
    if r.get("guide") and not (repo / r["guide"]).exists():
        g = rewrite_paths(old)
        if r["key"] == "linkedin-automation-template":
            note = "> Original full guide of this template. The people-first overview lives in the [README](../README.md) · [Español](../README.es.md).\n\n"
        else:
            note = "> Guía técnica original del proyecto, conservada íntegra. El recorrido para personas está en el [README en español](../README.es.md) · [English](../README.md).\n\n"
        (repo / r["guide"]).write_text(note + g, encoding="utf-8")
    # medios: se copian capturas nuevas si las hay; si no, se usan las que el repo ya tiene
    cap = CAP / r["key"]
    if cap.exists():
        need = ["desktop.png", "mobile.png", "captured.txt"] + ([] if r["media"] == "lock" else ["tour.gif", "tour.mp4"])
        falta = [n for n in need if not (cap / n).exists()]
        if falta:
            sys.exit(f"{r['key']}: captura incompleta en {cap}, falta {', '.join(falta)}. Vuelve a correr capture.py.")
        jpg(cap / "desktop.png", dr / "desktop.jpg", 1280)
        jpg(cap / "mobile.png", dr / "mobile.jpg", 780)
        shutil.copy(cap / "captured.txt", dr / "captured.txt")
        if r["media"] != "lock":
            shutil.copy(cap / "tour.gif", dr / "tour.gif"); shutil.copy(cap / "tour.mp4", dr / "tour.mp4")
    has_shots = (dr / "desktop.jpg").exists() and (dr / "mobile.jpg").exists()
    has_cap = has_shots and (dr / "tour.gif").exists() and (dr / "tour.mp4").exists()
    usa_shots = "{{SCREENS}}" in r["body"]["es"] or "{{SCREENS}}" in r["body"]["en"]
    if (r["media"] in ("capture", "lock") or usa_shots) and not has_shots:
        sys.exit(f"{r['key']}: no hay capturas en {cap} ni en {dr}. No se toca el README. Corre capture.py primero.")
    if r["media"] == "capture" and not has_cap:
        sys.exit(f"{r['key']}: falta el recorrido (tour.gif y tour.mp4). No se toca el README. Corre capture.py primero.")
    if has_shots:
        if not (dr / "captured.txt").exists():
            sys.exit(f"{r['key']}: falta {dr / 'captured.txt'} con la fecha real de las capturas (AAAA-MM-DD).")
        r["_captured"] = (dr / "captured.txt").read_text().strip()
        fecha(r["_captured"], "es")  # valida el formato antes de escribir nada
    if r["personal"]:
        for lang in ("es", "en"):
            (dr / f"banner-{lang}.svg").write_text(banner(r, lang), encoding="utf-8")
        for n in ("es", "es-on", "en", "en-on"):
            shutil.copy(LANG / f"{n}.svg", dr / f"lang-{n}.svg")
    if r["media"] == "flow":
        for lang in ("es", "en"):
            (dr / f"flow-{lang}.svg").write_text(flow(r, lang), encoding="utf-8")

    for lang, fname in (("en", "README.md"), ("es", "README.es.md")):
        t = L[lang]; out = []
        if r["personal"]:
            if lang == "en":
                pills = ('<img src="docs/readme/lang-en-on.svg" height="44" alt="English, current language" />\n'
                         '<a href="./README.es.md"><img src="docs/readme/lang-es.svg" height="44" alt="Leer en español" /></a>')
            else:
                pills = ('<a href="./README.md"><img src="docs/readme/lang-en.svg" height="44" alt="Read in English" /></a>\n'
                         '<img src="docs/readme/lang-es-on.svg" height="44" alt="Español, idioma actual" />')
            out.append(f'<div align="center">\n\n<a href="{r.get("live_" + lang, r["live"])}"><img src="docs/readme/banner-{lang}.svg" width="1000" alt="{r["title"]}: {r["promise"][lang]}" /></a>\n\n<br />\n\n{pills}\n\n<br />\n\n**[▶ {r["cta"][lang]}]({r.get("live_" + lang, r["live"])})** · {t["more"]} [github.com/jorgefsb](https://github.com/jorgefsb)\n\n</div>\n\n---\n')
        else:
            sw = "**English** · [Español](./README.es.md)" if lang == "en" else "[English](./README.md) · **Español**"
            out.append(f'# {r["title"]}\n\n{sw}\n\n> {r["tagline"][lang]}\n\n**[▶ {r["cta"][lang]}]({r.get("live_" + lang, r["live"])})** · {r["owner"][lang]}\n')
        if r["media"] == "capture":
            out.append(tour_block(r, lang, has_cap))
        elif r["media"] == "custom":
            out.append(r["top"][lang])
        elif r["media"] == "flow":
            out.append(f'<p align="center"><img src="docs/readme/flow-{lang}.svg" width="1000" alt="{r["flow_cap"][lang]}"></p>\n<p align="center"><sub>{r["flow_cap"][lang]}</sub></p>\n')
        body = r["body"][lang]
        if "{{SCREENS}}" in body:
            if r["media"] == "lock":
                blk = shots_block(r, lang, lock=True)
            elif r["media"] == "custom" and has_cap:
                blk = tour_block(r, lang, True) + "\n" + shots_block(r, lang)
            else:
                blk = shots_block(r, lang)
            body = body.replace("{{SCREENS}}", blk)
        out.append(body.rstrip() + "\n")
        foot = (t["foot"] if r["personal"] else t["cfoot"]).format(upd=DATE[lang])
        out.append(f'---\n\n<div align="center">\n\n<sub>{foot}</sub>\n\n</div>\n')
        text = "\n".join(out)
        if lang == "en" and herdr:
            text += herdr
        (repo / fname).write_text(text, encoding="utf-8")
    return r["key"]


if __name__ == "__main__":
    only = A.only
    for r in REPOS:
        if only and r["key"] not in only:
            continue
        print("ok", build(r))

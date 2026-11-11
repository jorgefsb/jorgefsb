#!/usr/bin/env python3
"""Genera los SVG del perfil de GitHub en español e inglés.

Sigue el BrandKit de JorgeSuarez.com.mx (Kit 0.6, Maestros 1.0): Outfit 700,
Inter 400, base negra, naranja y ámbar, papel solo como acento. Las fuentes van
embebidas (subset por archivo) para que el perfil se vea igual en cualquier
navegador. Animaciones de una sola vez, solo transform y opacity, apagadas con
prefers-reduced-motion. Moki entra desde su PNG aprobado, sin espejar.

Uso:
  python3 tools/build_assets.py --outfit Outfit-Bold.woff2 \
      --inter Inter-Regular.woff2 --moki moki-parche-derecho.webp

Los textos de cada idioma viven en el diccionario T. Cada cambio de copy se
hace ahí, en los dos idiomas, y se vuelve a generar.
"""
import argparse
import base64
import io
import math
import random
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools import subset
from fontTools.ttLib import TTFont

# BrandKit: base heredada + papel, kraft y tinta (propuestos)
BG = "#0A0A0A"
SURFACE = "#161616"
ACCENT = "#FF6B35"
AMBER = "#FFA500"
TEXT = "#FFFFFF"
MUTED = "#B7B3AD"
BORDER = "#8A7E70"
PAPER = "#F4E8D5"   # solo partículas y rellenos, nunca texto
KRAFT = "#B99168"
INK = "#22211F"

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

REDUCED = """
@media (prefers-reduced-motion: reduce){*{animation:none!important}}
"""

COMMON_CSS = """
.o{font-family:JzOutfit,Outfit,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:700}
.i{font-family:JzInter,Inter,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:400}
.pop{transform-box:fill-box;transform-origin:center;animation:pop .55s cubic-bezier(.34,1.56,.64,1) both}
.rise{animation:rise .6s cubic-bezier(.22,1,.36,1) both}
.fade{animation:fade .5s ease-out both}
.grow{transform-box:fill-box;transform-origin:left center;animation:grow 1.1s cubic-bezier(.22,1,.36,1) both}
.flash{opacity:0;animation:flash .45s ease-out both}
.pt{opacity:0}
@keyframes pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:scale(1)}}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes flash{0%{opacity:0}25%{opacity:1}100%{opacity:0}}
"""


class Fonts:
    def __init__(self, outfit, inter):
        self.paths = {"o": outfit, "i": inter}
        self.tt = {k: TTFont(v) for k, v in self.paths.items()}
        self.cmap = {k: t.getBestCmap() for k, t in self.tt.items()}
        self.upm = {k: t["head"].unitsPerEm for k, t in self.tt.items()}
        self.hmtx = {k: t["hmtx"] for k, t in self.tt.items()}

    def width(self, s, f, size, ls=0.0):
        w = 0
        for ch in s:
            g = self.cmap[f].get(ord(ch))
            if g is None:
                raise ValueError(f"glifo faltante {ch!r} en {f}")
            w += self.hmtx[f][g][0]
        return w * size / self.upm[f] + ls * max(len(s) - 1, 0)

    def face(self, f, chars):
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["kern", "liga"]
        font = TTFont(self.paths[f])
        sub = subset.Subsetter(opts)
        sub.populate(text="".join(sorted(chars)) + " ")
        sub.subset(font)
        buf = io.BytesIO()
        font.flavor = "woff2"
        font.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        fam = "JzOutfit" if f == "o" else "JzInter"
        weight = 700 if f == "o" else 400
        return (f"@font-face{{font-family:{fam};font-weight:{weight};"
                f"src:url(data:font/woff2;base64,{b64}) format('woff2')}}")


class Svg:
    def __init__(self, fonts, w, h, title, desc):
        self.F, self.w, self.h = fonts, w, h
        self.title, self.desc = title, desc
        self.used = {"o": set(), "i": set()}
        self.parts = []
        self.css = []

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, f="o", size=16, fill=TEXT, ls=0, anchor="start",
             cls="", style=""):
        self.used[f].update(s)
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        l = f' letter-spacing="{ls}"' if ls else ""
        st = f' style="{style}"' if style else ""
        c = f"{f} {cls}".strip()
        return (f'<text class="{c}" x="{x:.1f}" y="{y:.1f}" font-size="{size}" '
                f'fill="{fill}"{a}{l}{st}>{escape(s)}</text>')

    def tw(self, s, f="o", size=16, ls=0):
        return self.F.width(s, f, size, ls)

    def render(self):
        faces = [self.F.face(f, ch) for f, ch in self.used.items() if ch]
        css = "\n".join(faces) + COMMON_CSS + "\n".join(self.css) + REDUCED
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" '
            f'height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" '
            f'aria-labelledby="t d">\n'
            f'<title id="t">{escape(self.title)}</title>\n'
            f'<desc id="d">{escape(self.desc)}</desc>\n'
            f"<style>{css}</style>\n" + "\n".join(self.parts) + "\n</svg>\n"
        )


def d(sec):
    return f"animation-delay:{sec:.2f}s"


def particles(svg, cx, cy, n, spread, start, seed, size=(4, 8), dur=0.9):
    """Ráfaga de una sola vez: naranja, ámbar y papel, detrás del texto."""
    rnd = random.Random(seed)
    colors = [ACCENT, AMBER, PAPER]
    out = []
    for k in range(n):
        ang = rnd.uniform(0, 2 * math.pi)
        dist = rnd.uniform(spread * 0.45, spread)
        dx, dy = math.cos(ang) * dist, math.sin(ang) * dist * 0.8
        s = rnd.randint(*size)
        name = f"p{seed}_{k}"
        svg.css.append(
            f"@keyframes {name}{{0%{{opacity:0;transform:translate(0,0) rotate(0)}}"
            f"15%{{opacity:1}}100%{{opacity:0;transform:translate({dx:.0f}px,{dy:.0f}px) "
            f"rotate({rnd.choice([90, 180, -90])}deg)}}}}"
            f".{name}{{transform-box:fill-box;transform-origin:center;"
            f"animation:{name} {dur + rnd.uniform(0, .35):.2f}s cubic-bezier(.16,1,.3,1) "
            f"{start + rnd.uniform(0, .15):.2f}s both}}"
        )
        out.append(f'<rect class="pt {name}" x="{cx - s / 2:.0f}" y="{cy - s / 2:.0f}" '
                   f'width="{s}" height="{s}" fill="{rnd.choice(colors)}"/>')
    return "\n".join(out)


def diamond(x, y, r, fill, cls="", style=""):
    st = f' style="{style}"' if style else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<path{c}{st} d="M{x} {y - r}L{x + r} {y}L{x} {y + r}L{x - r} {y}Z" '
            f'fill="{fill}"/>')


def play_icon(x, y, s, fill):
    return f'<path d="M{x} {y}L{x + s} {y + s / 2}L{x} {y + s}Z" fill="{fill}"/>'


def monogram(svg, x, y, size, delay=0.1):
    r = 18
    fs = size * 0.44
    return f"""
<g class="pop" style="{d(delay)}">
  <rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{r}" fill="{SURFACE}"/>
  <rect x="{x + 1.5}" y="{y + 1.5}" width="{size - 3}" height="{size - 3}" rx="{r - 1.5}" fill="none" stroke="{ACCENT}" stroke-width="3"/>
  {svg.text(x + size / 2, y + size * 0.6, "JS", "o", round(fs), TEXT, anchor="middle")}
  <rect x="{x + size * 0.28:.1f}" y="{y + size * 0.73:.1f}" width="{size * 0.44:.1f}" height="{max(4, size * 0.035):.1f}" rx="2" fill="{ACCENT}"/>
  <rect x="{x + size * 0.28:.1f}" y="{y + size * 0.73:.1f}" width="{size * 0.44:.1f}" height="{max(4, size * 0.035):.1f}" rx="2" fill="{AMBER}" class="grow" style="{d(delay + .5)}"/>
</g>"""


def press_start(svg, x, y, delay):
    label = "PRESS START"
    fs = 14
    w = svg.tw(label, "o", fs, 2) + 46
    svg.css.append(
        "@keyframes blink{0%,100%{opacity:1}50%{opacity:.15}}"
        f".ps{{animation:pop .5s cubic-bezier(.34,1.56,.64,1) {delay:.2f}s both,"
        f"blink .5s steps(1,end) {delay + .6:.2f}s 3}}"
    )
    return f"""
<g class="ps" style="transform-box:fill-box;transform-origin:center">
  <rect x="{x}" y="{y}" width="{w:.1f}" height="32" rx="16" fill="{ACCENT}"/>
  {play_icon(x + 16, y + 10, 12, INK)}
  {svg.text(x + 34, y + 21, label, "o", fs, INK, ls=2)}
</g>""", w


def xp_bar(svg, x, y, w, h, delay):
    return f"""
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{SURFACE}" stroke="{BORDER}" stroke-width="1"/>
<g class="grow" style="{d(delay)};animation-duration:1.4s">
  <rect x="{x + 3}" y="{y + 3}" width="{w - 6}" height="{h - 6}" rx="{(h - 6) / 2}" fill="url(#xp)"/>
</g>
<rect class="flash" style="{d(delay + 1.35)}" x="{x - 1.5}" y="{y - 1.5}" width="{w + 3}" height="{h + 3}" rx="{h / 2 + 1.5}" fill="none" stroke="{ACCENT}" stroke-width="3"/>"""


GRAD = f"""<defs>
<linearGradient id="xp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{ACCENT}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>
<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{ACCENT}" stroke-opacity=".07"/></pattern>
</defs>"""


def frame(w, h, r=18, draw=True):
    per = 2 * (w + h)
    css = (f".frame{{stroke-dasharray:{per};stroke-dashoffset:{per};"
           f"animation:draw 1.3s cubic-bezier(.65,0,.35,1) .05s forwards}}"
           f"@keyframes draw{{to{{stroke-dashoffset:0}}}}"
           f"@media (prefers-reduced-motion: reduce){{.frame{{stroke-dashoffset:0}}}}")
    body = f"""
<rect width="{w}" height="{h}" rx="{r}" fill="{BG}"/>
<rect width="{w}" height="{h}" rx="{r}" fill="url(#grid)"/>
<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="{r - 1.5}" fill="none" stroke="{BORDER}" stroke-opacity=".5" stroke-width="1"/>
<rect class="frame" x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="{r - 1.5}" fill="none" stroke="{ACCENT}" stroke-width="3" pathLength="{per}"/>"""
    return body, css


# ---------- botones sociales ----------

def icon_youtube(x, y, c):
    return (f'<rect x="{x}" y="{y + 3}" width="24" height="18" rx="5" fill="{c}"/>'
            f'<path d="M{x + 10} {y + 8}L{x + 17} {y + 12}L{x + 10} {y + 16}Z" fill="{SURFACE}"/>')


def icon_globe(x, y, c):
    cx, cy = x + 12, y + 12
    return (f'<g fill="none" stroke="{c}" stroke-width="2"><circle cx="{cx}" cy="{cy}" r="10"/>'
            f'<path d="M{cx - 10} {cy}h20M{cx} {cy - 10}c4 3 4 17 0 20M{cx} {cy - 10}c-4 3-4 17 0 20"/></g>')


def icon_linkedin(x, y, c, bg):
    return (f'<rect x="{x + 1}" y="{y + 1}" width="22" height="22" rx="4" fill="{c}"/>'
            f'<rect x="{x + 5}" y="{y + 10}" width="3.4" height="9" fill="{bg}"/>'
            f'<circle cx="{x + 6.7}" cy="{y + 6.4}" r="2" fill="{bg}"/>'
            f'<path d="M{x + 10.5} {y + 10}h3.2v1.4c.6-1 1.7-1.7 3.2-1.7 2.4 0 3.4 1.5 3.4 4.1V{y + 19}h-3.4v-4.7c0-1.3-.4-2-1.5-2s-1.5.8-1.5 2V{y + 19}h-3.4Z" fill="{bg}"/>')


def icon_x(x, y, c):
    return (f'<path d="M{x + 3} {y + 3}h5.6l12.4 18h-5.6Z" fill="{c}"/>'
            f'<path d="M{x + 20} {y + 3}L{x + 4.5} {y + 21}" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>')


def arrow_ne(x, y, c):
    return (f'<path d="M{x} {y + 10}L{x + 10} {y}M{x + 3} {y}h7v7" fill="none" stroke="{c}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')


def social(F, label, handle, icon, aria, primary=False, delay=0.0, arrow=False):
    H = 44
    fs, hs = 15, 13
    s = Svg(F, 10, H, aria, aria)
    lw = s.tw(label, "o", fs, 1.2)
    hw = s.tw(handle, "i", hs) if handle else 0
    W = int(16 + 24 + 12 + lw + (12 + hw if handle else 0) + (22 if arrow else 0) + 18)
    s.w = W
    bg = ACCENT if primary else SURFACE
    fg = INK if primary else TEXT
    ic = INK if primary else ACCENT
    sub = INK if primary else MUTED
    stroke = "none" if primary else BORDER
    s.add(f'<g class="pop" style="{d(delay)}">')
    s.add(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="6" fill="{bg}" stroke="{stroke}" stroke-width="1.5"/>')
    if icon == "yt":
        s.add(icon_youtube(16, 10, ic))
    elif icon == "web":
        s.add(icon_globe(16, 10, ic))
    elif icon == "in":
        s.add(icon_linkedin(16, 10, ic, bg))
    elif icon == "x":
        s.add(icon_x(16, 10, ic))
    tx = 52
    s.add(s.text(tx, 28, label, "o", fs, fg, ls=1.2))
    tx += lw + 12
    if handle:
        s.add(s.text(tx, 28, handle, "i", hs, sub))
        tx += hw
    if arrow:
        s.add(arrow_ne(tx + 10, 16, ic))
    s.add("</g>")
    s.add(f'<rect class="flash" style="{d(delay + .45)}" x="1.5" y="1.5" width="{W - 3}" height="{H - 3}" rx="6" fill="none" stroke="{AMBER if primary else ACCENT}" stroke-width="3"/>')
    return s.render()


def trophy(x, y, c):
    return (f'<path d="M{x + 6} {y}h20v8c0 6-4 11-10 11s-10-5-10-11Z" fill="{c}"/>'
            f'<path d="M{x + 6} {y + 3}H{x}c0 6 3 9 7 9M{x + 26} {y + 3}h6c0 6-3 9-7 9" fill="none" stroke="{c}" stroke-width="2.5"/>'
            f'<rect x="{x + 13}" y="{y + 19}" width="6" height="6" fill="{c}"/>'
            f'<rect x="{x + 8}" y="{y + 25}" width="16" height="5" rx="1.5" fill="{c}"/>')


def icon_spark(x, y, c):
    return (f'<path d="M{x + 12} {y}C{x + 13} {y + 7} {x + 17} {y + 11} {x + 24} {y + 12}C{x + 17} {y + 13} {x + 13} {y + 17} {x + 12} {y + 24}'
            f'C{x + 11} {y + 17} {x + 7} {y + 13} {x} {y + 12}C{x + 7} {y + 11} {x + 11} {y + 7} {x + 12} {y}Z" fill="{c}"/>')


def icon_code(x, y, c):
    return (f'<path d="M{x + 7} {y + 5}L{x} {y + 12}L{x + 7} {y + 19}M{x + 17} {y + 5}L{x + 24} {y + 12}L{x + 17} {y + 19}M{x + 14} {y + 2}L{x + 10} {y + 22}" '
            f'fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')


def icon_cloud(x, y, c):
    return (f'<path d="M{x + 6} {y + 20}h13a5 5 0 0 0 0-10 7 7 0 0 0-13-1 5.5 5.5 0 0 0 0 11Z" fill="none" '
            f'stroke="{c}" stroke-width="2.6" stroke-linejoin="round"/>')


def icon_pad(x, y, c):
    return (f'<path d="M{x + 3} {y + 9}C{x + 4} {y + 5} {x + 6} {y + 4} {x + 9} {y + 4}h6c3 0 5 1 6 5l2 9c.4 2.4-2 3.6-3.6 2l-3.4-3.4h-8L{x + 4.6} {y + 20}C{x + 3} {y + 21.6} {x + .6} {y + 20.4} {x + 1} {y + 18}Z" '
            f'fill="none" stroke="{c}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<path d="M{x + 8} {y + 8}v5M{x + 5.5} {y + 10.5}h5" stroke="{c}" stroke-width="2.2"/>'
            f'<circle cx="{x + 16.5}" cy="{y + 9.5}" r="1.6" fill="{c}"/><circle cx="{x + 19}" cy="{y + 12.5}" r="1.6" fill="{c}"/>')


ICONS = {"spark": icon_spark, "code": icon_code, "cloud": icon_cloud, "pad": icon_pad}


# ---------- textos por idioma ----------

T = {
    "es": {
        "hero_desc": "Videojuegos, negocios e IA desde Guadalajara, México. 20+ años haciendo industria.",
        "loc": "PLAYER ONE // GUADALAJARA, MÉXICO",
        "loc1": "PLAYER ONE //", "loc2": "GUADALAJARA, MÉXICO",
        "sub": "VIDEOJUEGOS · NEGOCIOS · IA",
        "xp": "20+ AÑOS HACIENDO INDUSTRIA",
        "roles": ["FUNDADOR", "OPERADOR", "JUGADOR"],
        "ach": "LOGRO DESBLOQUEADO", "ach_aria": "Logro desbloqueado",
        "slot": "SLOT", "loadout_aria": "Loadout, slot",
        "loadout": [
            ("Videojuegos", ["Unreal Engine", "Unity", "Roblox"], "pad"),
            ("IA y agentes", ["Claude Code", "Codex", "Cursor", "MCP", "sistemas multiagente"], "spark"),
            ("Producto web", ["TypeScript", "JavaScript", "Node.js", "Next.js", "Python"], "code"),
            ("Plataforma", ["Cloudflare", "GitHub Pages", "Supabase"], "cloud"),
        ],
        "pillar_kicker": "FUERTE",
        "pillars": [
            ("VIDEOJUEGOS", "LV 20+", 1.0, False, "pad",
             ["20+ años en la industria", "GM de Amber Studio México", "Fundé KaraOkulta en 2004"]),
            ("NEGOCIOS", "LV 25+", 1.0, False, "flag",
             ["Emprendo desde 1999", "Shark Tank México 2016", "Forbes 30 Promesas 2015"]),
            ("IA", "NEW GAME+", 0.58, True, "spark",
             ["Productos hechos con agentes", "Claude Code · Codex · Cursor", "Aprendo en público"]),
        ],
        "close_kicker": "MODO CO-OP",
        "close_title": "¿CONSTRUIMOS ALGO?",
        "close_sub": "Videojuegos, negocios o IA. Escríbeme.",
        "close_aria": "¿Construimos algo? Escríbeme a jorgefsb@gmail.com",
        "close_desc": "Moki, el astronauta de cartón naranja, junto a la invitación a escribir a jorgefsb@gmail.com.",
    },
    "en": {
        "hero_desc": "Video games, business and AI from Guadalajara, Mexico. 20+ years building the industry.",
        "loc": "PLAYER ONE // GUADALAJARA, MEXICO",
        "loc1": "PLAYER ONE //", "loc2": "GUADALAJARA, MEXICO",
        "sub": "VIDEO GAMES · BUSINESS · AI",
        "xp": "20+ YEARS BUILDING THE INDUSTRY",
        "roles": ["FOUNDER", "OPERATOR", "PLAYER"],
        "ach": "ACHIEVEMENT UNLOCKED", "ach_aria": "Achievement unlocked",
        "slot": "SLOT", "loadout_aria": "Loadout, slot",
        "loadout": [
            ("Video games", ["Unreal Engine", "Unity", "Roblox"], "pad"),
            ("AI & agents", ["Claude Code", "Codex", "Cursor", "MCP", "multi-agent systems"], "spark"),
            ("Web product", ["TypeScript", "JavaScript", "Node.js", "Next.js", "Python"], "code"),
            ("Platform", ["Cloudflare", "GitHub Pages", "Supabase"], "cloud"),
        ],
        "pillar_kicker": "STRENGTH",
        "pillars": [
            ("VIDEO GAMES", "LV 20+", 1.0, False, "pad",
             ["20+ years in the industry", "GM, Amber Studio México", "Founded KaraOkulta in 2004"]),
            ("BUSINESS", "LV 25+", 1.0, False, "flag",
             ["Entrepreneur since 1999", "Shark Tank México 2016", "Forbes 30 Promesas 2015"]),
            ("AI", "NEW GAME+", 0.58, True, "spark",
             ["Products built with AI agents", "Claude Code · Codex · Cursor", "Learning in public"]),
        ],
        "close_kicker": "CO-OP MODE",
        "close_title": "WANT TO BUILD SOMETHING?",
        "close_sub": "Video games, business or AI. Write me.",
        "close_aria": "Want to build something? Write me at jorgefsb@gmail.com",
        "close_desc": "Moki, the orange cardboard astronaut, next to an invitation to write to jorgefsb@gmail.com.",
    },
}

ACHIEVEMENTS = [
    ("shark-tank", "Shark Tank México", "2016"),
    ("forbes", "Forbes 30 Promesas", "2015"),
    ("cinepolis-accelerator", "Cinépolis Accelerator Alumni", "2015"),
    ("cinepolis-seedcamp", "Cinépolis Seedcamp Winner", "2014"),
]
MAIL = "jorgefsb@gmail.com"


def fit(s, text, f, size, maxw, ls=0, floor=11):
    while s.tw(text, f, size, ls) > maxw and size > floor:
        size -= 0.5
    return size


def roles_row(svg, x, y, size, delay, items, gap=16):
    out, cx = [], x
    for k, it in enumerate(items):
        out.append(f'<g class="rise" style="{d(delay + k * .12)}">'
                   + svg.text(cx, y, it, "i", size, MUTED, ls=1.5) + "</g>")
        cx += svg.tw(it, "i", size, 1.5) + gap
        if k < len(items) - 1:
            out.append(f'<g class="pop" style="{d(delay + k * .12 + .08)}">'
                       + diamond(cx, y - size * 0.36, size * 0.33, ACCENT if k == 0 else AMBER)
                       + "</g>")
            cx += gap
    return "\n".join(out)


def press_start_fix(s, x, y, delay):
    g, _ = press_start(s, x, y, delay)
    return g


def hero_desktop(F, L):
    W, H = 1000, 300
    s = Svg(F, W, H, "Jorge Suárez Basáñez", L["hero_desc"])
    body, css = frame(W, H)
    s.css.append(css)
    s.add(GRAD)
    s.add(body)
    s.add(f'<g fill="{AMBER}" class="fade" style="{d(1.2)}"><rect x="24" y="24" width="8" height="8"/><rect x="40" y="24" width="8" height="8"/></g>')
    s.add(f'<g fill="{ACCENT}" class="fade" style="{d(1.3)}"><rect x="952" y="268" width="8" height="8"/><rect x="968" y="268" width="8" height="8"/></g>')
    s.add(particles(s, 132, 150, 22, 230, .45, 1))
    s.add(monogram(s, 52, 70, 160))
    x = 252
    s.add(f'<g class="rise" style="{d(.3)}">' + s.text(x, 74, L["loc"], "o", 14, ACCENT, ls=3) + "</g>")
    pw = s.tw("PRESS START", "o", 14, 2) + 46
    s.add(press_start_fix(s, round(W - 50 - pw, 1), 52, 1.7))
    s.add(f'<g class="rise" style="{d(.45)}">' + s.text(x, 128, "JORGE SUÁREZ BASÁÑEZ", "o", 48, TEXT, ls=-0.5) + "</g>")
    sub = L["sub"]
    subw = s.tw(sub, "i", 19, 1)
    s.add(f'<clipPath id="type"><rect class="grow" style="{d(.75)};animation-duration:.9s;animation-timing-function:steps(24,end)" x="{x}" y="146" width="{subw + 4:.0f}" height="30"/></clipPath>')
    s.add('<g clip-path="url(#type)">' + s.text(x, 166, sub, "i", 19, MUTED, ls=1) + "</g>")
    s.add(f'<g class="fade" style="{d(.9)}">' + s.text(x, 212, "XP", "o", 15, ACCENT, ls=2) + "</g>")
    s.add(f'<g class="fade" style="{d(.9)}">' + xp_bar(s, x + 34, 198, 330, 18, 1.0) + "</g>")
    xs = fit(s, L["xp"], "o", 16, W - 50 - (x + 34 + 330 + 18), ls=1)
    s.add(f'<g class="pop" style="{d(2.2)}">' + s.text(x + 34 + 330 + 18, 213, L["xp"], "o", xs, TEXT, ls=1) + "</g>")
    s.add(roles_row(s, x, 256, 15, 1.35, L["roles"]))
    return s.render()


def hero_mobile(F, L):
    W, H = 600, 506
    s = Svg(F, W, H, "Jorge Suárez Basáñez", L["hero_desc"])
    body, css = frame(W, H)
    s.css.append(css)
    s.add(GRAD)
    s.add(body)
    s.add(f'<g fill="{ACCENT}" class="fade" style="{d(1.3)}"><rect x="552" y="474" width="8" height="8"/><rect x="568" y="474" width="8" height="8"/></g>')
    s.add(particles(s, 100, 100, 18, 220, .45, 2))
    s.add(monogram(s, 40, 40, 120))
    x = 186
    s.add(f'<g class="rise" style="{d(.3)}">' + s.text(x, 74, L["loc1"], "o", 20, ACCENT, ls=2.5) + "</g>")
    s.add(f'<g class="rise" style="{d(.38)}">' + s.text(x, 102, L["loc2"], "o", 20, ACCENT, ls=2.5) + "</g>")
    s.add(press_start_fix(s, x, 122, 1.7))
    s.add(f'<g class="rise" style="{d(.45)}">' + s.text(40, 238, "JORGE SUÁREZ", "o", 64, TEXT, ls=-0.5) + "</g>")
    s.add(f'<g class="rise" style="{d(.55)}">' + s.text(40, 304, "BASÁÑEZ", "o", 64, TEXT, ls=-0.5) + "</g>")
    ss = fit(s, L["sub"], "i", 26, 520, ls=1)
    s.add(f'<g class="rise" style="{d(.8)}">' + s.text(40, 352, L["sub"], "i", ss, MUTED, ls=1) + "</g>")
    s.add(f'<g class="fade" style="{d(.9)}">' + s.text(40, 398, "XP", "o", 20, ACCENT, ls=2) + "</g>")
    s.add(f'<g class="fade" style="{d(.9)}">' + xp_bar(s, 84, 380, 476, 22, 1.0) + "</g>")
    xs = fit(s, L["xp"], "o", 24, 520, ls=1)
    s.add(f'<g class="pop" style="{d(2.2)}">' + s.text(40, 442, L["xp"], "o", xs, TEXT, ls=1) + "</g>")
    s.add(roles_row(s, 40, 478, 20, 1.35, L["roles"], gap=14))
    return s.render()


# ---------- tarjetas ----------

CARD_W = 400
PILLAR_W = 272


def card_base(s, h, delay, w=CARD_W):
    s.add(f'<g class="rise" style="{d(delay)}">')
    s.add(f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="12" fill="{BG}" stroke="{BORDER}" stroke-opacity=".7" stroke-width="1.5"/>')
    s.add(f'<path d="M1 30V13Q1 1 13 1H70" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>')
    s.add(f'<path d="M{w - 70} {h - 1}H{w - 13}Q{w - 1} {h - 1} {w - 1} {h - 13}V{h - 30}" fill="none" stroke="{AMBER}" stroke-width="3" stroke-linecap="round"/>')


def icon_flag(x, y, c):
    return (f'<path d="M{x + 5} {y + 2}V{y + 23}" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/>'
            f'<path d="M{x + 5} {y + 3}H{x + 21}L{x + 17} {y + 8.5}L{x + 21} {y + 14}H{x + 5}Z" fill="{c}"/>')


ICONS["flag"] = icon_flag


def achievement(F, L, title, year, delay, seed):
    H = 84
    s = Svg(F, CARD_W, H, f"{L['ach_aria']}: {title} ({year})", f"{title}, {year}.")
    s.add(particles(s, 44, 42, 12, 70, delay + .35, seed, size=(3, 6), dur=.8))
    card_base(s, H, delay)
    s.add(f'<rect x="18" y="16" width="52" height="52" rx="12" fill="{SURFACE}" stroke="{BORDER}" stroke-opacity=".6"/>')
    s.add(f'<g class="pop" style="{d(delay + .3)}">' + trophy(28, 27, AMBER) + "</g>")
    s.add(s.text(88, 38, L["ach"], "o", 11, ACCENT, ls=2.2))
    fs = 19
    while s.tw(title, "o", fs) > CARD_W - 88 - 82 and fs > 13:
        fs -= 1
    s.add(s.text(88, 63, title, "o", fs, TEXT))
    yw = s.tw(year, "o", 14, 1) + 22
    s.add(f'<g class="pop" style="{d(delay + .5)}"><rect x="{CARD_W - 18 - yw:.1f}" y="29" width="{yw:.1f}" height="26" rx="13" fill="{SURFACE}" stroke="{BORDER}"/>'
          + s.text(CARD_W - 18 - yw / 2, 47, year, "o", 14, TEXT, ls=1, anchor="middle") + "</g>")
    s.add("</g>")
    s.add(f'<rect class="flash" style="{d(delay + .55)}" x="1.5" y="1.5" width="{CARD_W - 3}" height="{H - 3}" rx="12" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    return s.render()


def loadout(F, L, slot, label, items, icon, delay, min_h=158):
    s = Svg(F, CARD_W, 10, f"{L['loadout_aria']} {slot}: {label}", f"{label}: {' · '.join(items)}.")
    fs, ch, padx, gap = 14, 30, 13, 8
    x0, xmax = 20, CARD_W - 20
    cx, cy = x0, 70
    chips = []
    for it in items:
        w = s.tw(it, "i", fs) + padx * 2
        if cx + w > xmax:
            cx, cy = x0, cy + ch + gap
        chips.append((cx, cy, w, it))
        cx += w + gap
    H = max(cy + ch + 20, min_h)
    s.h = H
    card_base(s, H, delay)
    s.add(f'<rect x="18" y="16" width="36" height="36" rx="8" fill="{SURFACE}" stroke="{BORDER}" stroke-opacity=".6"/>')
    s.add(f'<g class="pop" style="{d(delay + .25)}">' + ICONS[icon](24, 22, ACCENT) + "</g>")
    s.add(s.text(66, 32, f"{L['slot']} {slot}", "o", 11, MUTED, ls=2.2))
    s.add(s.text(66, 50, label.upper(), "o", 17, TEXT, ls=1))
    for k, (x, y, w, it) in enumerate(chips):
        s.add(f'<g class="pop" style="{d(delay + .4 + k * .09)}">'
              f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{ch}" rx="15" fill="{SURFACE}" stroke="{BORDER}"/>'
              + s.text(x + w / 2, y + 20, it, "i", fs, TEXT, anchor="middle") + "</g>")
    s.add("</g>")
    return s.render()


def pillar(F, L, n, title, chip, fill, hot, icon, lines, delay):
    """Uno de los tres fuertes: videojuegos, negocios, IA (en ese orden)."""
    W, H = PILLAR_W, 214
    s = Svg(F, W, H, f"{L['pillar_kicker']} {n}: {title}", f"{title}. " + ". ".join(lines) + ".")
    s.add(GRAD)
    card_base(s, H, delay, W)
    s.add(f'<rect x="18" y="16" width="40" height="40" rx="9" fill="{SURFACE}" stroke="{BORDER}" stroke-opacity=".6"/>')
    s.add(f'<g class="pop" style="{d(delay + .25)}">' + ICONS[icon](26, 24, ACCENT) + "</g>")
    s.add(s.text(70, 31, f"{L['pillar_kicker']} {n}", "o", 11, MUTED, ls=2.2))
    s.add(s.text(70, 52, title, "o", 19, TEXT, ls=.8))
    cw = s.tw(chip, "o", 12, 1) + 20
    cx = W - 18 - cw
    bw = cx - 10 - 18
    s.add(f'<rect x="18" y="82" width="{bw:.1f}" height="12" rx="6" fill="{SURFACE}" stroke="{BORDER}" stroke-opacity=".6"/>')
    s.add(f'<rect class="grow" style="{d(delay + .45)}" x="18" y="82" width="{bw * fill:.1f}" height="12" rx="6" fill="url(#xp)"/>')
    cbg, cfg, cst = (ACCENT, INK, "none") if hot else (SURFACE, TEXT, BORDER)
    s.add(f'<g class="pop" style="{d(delay + .7)}"><rect x="{cx:.1f}" y="76" width="{cw:.1f}" height="24" rx="12" fill="{cbg}" stroke="{cst}"/>'
          + s.text(cx + cw / 2, 92.5, chip, "o", 12, cfg, ls=1, anchor="middle") + "</g>")
    for k, ln in enumerate(lines):
        y = 132 + k * 27
        fs = fit(s, ln, "i", 14, W - 40 - 18, floor=12)
        s.add(f'<g class="rise" style="{d(delay + .8 + k * .1)}">'
              + diamond(24, y - 5, 4, ACCENT if k == 0 else AMBER)
              + s.text(40, y, ln, "i", fs, TEXT) + "</g>")
    s.add("</g>")
    if hot:
        s.add(f'<rect class="flash" style="{d(delay + 1.2)}" x="1.5" y="1.5" width="{W - 3}" height="{H - 3}" rx="12" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
    return s.render()


def lang_pill(F, label, aria, active):
    H = 44
    s = Svg(F, 10, H, aria, aria)
    lw = s.tw(label, "o", 14, 1.4)
    W = int(16 + 22 + 10 + lw + 18)
    s.w = W
    # Activo: borde naranja. Inactivo: discreto. El único botón relleno es el del sitio.
    bg, fg, st, sw, ic = (SURFACE, TEXT, ACCENT, 2.5, ACCENT) if active else (BG, MUTED, BORDER, 1.5, MUTED)
    s.add(f'<rect x="1.5" y="1.5" width="{W - 3}" height="{H - 3}" rx="20.5" fill="{bg}" stroke="{st}" stroke-width="{sw}"/>')
    cx, cy = 27, 22
    s.add(f'<g fill="none" stroke="{ic}" stroke-width="2"><circle cx="{cx}" cy="{cy}" r="9"/>'
          f'<path d="M{cx - 9} {cy}h18M{cx} {cy - 9}c3.6 2.7 3.6 15.3 0 18M{cx} {cy - 9}c-3.6 2.7-3.6 15.3 0 18"/></g>')
    s.add(s.text(48, 27, label, "o", 14, fg, ls=1.4))
    return s.render()


def moki_img(x, y, h, data, ratio):
    w = h * ratio
    return (f'<image x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'href="data:image/webp;base64,{data}" preserveAspectRatio="xMidYMid meet"/>'), w


def mail_pill(s, x, y, h, fs, delay):
    mw = s.tw(MAIL, "i", fs)
    ic = h * 0.3
    w = h * 0.5 + ic + h * 0.3 + mw + h * 0.55
    g = (f'<g class="pop" style="{d(delay)}">'
         f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{ACCENT}"/>'
         + play_icon(round(x + h * 0.5, 1), round(y + (h - ic) / 2, 1), round(ic, 1), INK)
         + s.text(x + h * 0.5 + ic + h * 0.3, y + h / 2 + fs * 0.35, MAIL, "i", fs, INK) + "</g>")
    return g, w


def closing_desktop(F, L, moki, ratio):
    W, H = 1000, 230
    s = Svg(F, W, H, L["close_aria"], L["close_desc"])
    body, css = frame(W, H)
    s.css.append(css)
    s.add(GRAD)
    s.add(body)
    s.add(particles(s, 130, 120, 16, 170, .5, 21))
    img, mw = moki_img(58, 18, 194, moki, ratio)
    s.add(f'<ellipse cx="{58 + mw / 2 + 4:.1f}" cy="209" rx="{mw * .36:.1f}" ry="7" fill="{PAPER}" fill-opacity=".10"/>')
    s.add(f'<g class="rise" style="{d(.2)}">{img}</g>')
    x = 58 + mw + 48
    s.add(f'<g class="rise" style="{d(.35)}">' + s.text(x, 62, L["close_kicker"], "o", 14, ACCENT, ls=3) + "</g>")
    ts = fit(s, L["close_title"], "o", 42, W - 60 - x, ls=-0.3, floor=28)
    s.add(f'<g class="rise" style="{d(.45)}">' + s.text(x, 110, L["close_title"], "o", ts, TEXT, ls=-0.3) + "</g>")
    s.add(f'<g class="rise" style="{d(.55)}">' + s.text(x, 142, L["close_sub"], "i", 18, MUTED) + "</g>")
    pill, _ = mail_pill(s, x, 162, 42, 16, .8)
    s.add(pill)
    s.add(f'<g fill="{AMBER}" class="fade" style="{d(1.2)}"><rect x="952" y="24" width="8" height="8"/><rect x="968" y="24" width="8" height="8"/></g>')
    return s.render()


def closing_mobile(F, L, moki, ratio):
    W, H = 600, 590
    s = Svg(F, W, H, L["close_aria"], L["close_desc"])
    body, css = frame(W, H)
    s.css.append(css)
    s.add(GRAD)
    s.add(body)
    mh = 250
    mw = mh * ratio
    s.add(particles(s, W / 2, 160, 16, 200, .5, 22))
    s.add(f'<ellipse cx="{W / 2 + 4:.1f}" cy="{32 + mh - 2}" rx="{mw * .36:.1f}" ry="8" fill="{PAPER}" fill-opacity=".10"/>')
    img, _ = moki_img((W - mw) / 2, 32, mh, moki, ratio)
    s.add(f'<g class="rise" style="{d(.2)}">{img}</g>')
    s.add(f'<g class="rise" style="{d(.35)}">' + s.text(W / 2, 338, L["close_kicker"], "o", 20, ACCENT, ls=3, anchor="middle") + "</g>")
    ts = fit(s, L["close_title"], "o", 46, 520, ls=-0.3, floor=30)
    s.add(f'<g class="rise" style="{d(.45)}">' + s.text(W / 2, 394, L["close_title"], "o", ts, TEXT, ls=-0.3, anchor="middle") + "</g>")
    ss = fit(s, L["close_sub"], "i", 24, 520, floor=18)
    s.add(f'<g class="rise" style="{d(.55)}">' + s.text(W / 2, 436, L["close_sub"], "i", ss, MUTED, anchor="middle") + "</g>")
    h, fs = 64, 24
    pw = h * 0.5 + h * 0.3 + h * 0.3 + s.tw(MAIL, "i", fs) + h * 0.55
    pill, _ = mail_pill(s, (W - pw) / 2, 472, h, fs, .8)
    s.add(pill)
    return s.render()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outfit", required=True)
    ap.add_argument("--inter", required=True)
    ap.add_argument("--moki", required=True, help="WebP de Moki (parche derecho, sin espejar)")
    a = ap.parse_args()
    F = Fonts(a.outfit, a.inter)
    raw = Path(a.moki).read_bytes()
    from PIL import Image
    with Image.open(io.BytesIO(raw)) as im:
        ratio = im.width / im.height
    moki = base64.b64encode(raw).decode()

    out = {
        "social/youtube.svg": social(F, "YOUTUBE", "@jorgefsb", "yt", "YouTube: @jorgefsb", delay=.05),
        "social/website.svg": social(F, "JORGESUAREZ.COM.MX", "", "web", "jorgesuarez.com.mx", primary=True, delay=.15),
        "social/linkedin.svg": social(F, "LINKEDIN", "", "in", "LinkedIn: Jorge Suárez", delay=.25, arrow=True),
        "social/x.svg": social(F, "X", "@jorgefsb", "x", "X / Twitter: @jorgefsb", delay=.35),
        "lang/es.svg": lang_pill(F, "ESPAÑOL", "Leer en español", False),
        "lang/es-on.svg": lang_pill(F, "ESPAÑOL", "Español, idioma actual", True),
        "lang/en.svg": lang_pill(F, "ENGLISH", "Read in English", False),
        "lang/en-on.svg": lang_pill(F, "ENGLISH", "English, current language", True),
    }
    for lang, L in T.items():
        out[f"{lang}/hero.svg"] = hero_desktop(F, L)
        out[f"{lang}/hero-mobile.svg"] = hero_mobile(F, L)
        for k, (title, chip, fill, hot, icon, lines) in enumerate(L["pillars"]):
            out[f"{lang}/pillar-{k + 1}.svg"] = pillar(F, L, f"0{k + 1}", title, chip, fill, hot, icon, lines, .05 + k * .15)
        for k, (label, items, icon) in enumerate(L["loadout"]):
            out[f"{lang}/loadout-{k + 1}.svg"] = loadout(F, L, f"0{k + 1}", label, items, icon, .05 + k * .15)
        for k, (slug, title, year) in enumerate(ACHIEVEMENTS):
            out[f"{lang}/achievement-{slug}.svg"] = achievement(F, L, title, year, .05 + k * .2, 11 + k)
        out[f"{lang}/closing.svg"] = closing_desktop(F, L, moki, ratio)
        out[f"{lang}/closing-mobile.svg"] = closing_mobile(F, L, moki, ratio)
    for name, svg in out.items():
        p = ASSETS / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(svg, encoding="utf-8")
        print(f"{name:42s} {len(svg.encode()) / 1024:6.1f} KB")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""About de cada repo: descripción, sitio y topics, desde los mismos datos del README.

  python3 tools/readme-kit/about.py            # lista lo que debe decir cada About
  python3 tools/readme-kit/about.py --check    # compara contra GitHub (solo lectura, usa gh)
  python3 tools/readme-kit/about.py --apply    # lo escribe con gh (pide permiso de administración del repo)

Si --apply responde 403, el About se pone a mano en GitHub: engrane junto a
"About" en la página del repo, con los valores que imprime este comando.
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from data1 import REPOS1
from data2 import REPOS2
from data3 import REPOS3

OWNER = "jorgefsb"
mode = sys.argv[1] if len(sys.argv) > 1 else ""
only = [a for a in sys.argv[1:] if not a.startswith("--")]
bad = 0


def sitio(r):
    live = r.get("homepage", r["live"])
    return "" if live.startswith(".") or "github.com/" in live else live.rstrip("/")


for r in REPOS1 + REPOS2 + REPOS3:
    if only and r["key"] not in only:
        continue
    want = dict(description=r["about"], homepage=sitio(r), topics=sorted(r["topics"]))
    errs = []
    if len(r["about"]) > 350: errs.append("descripción de más de 350 caracteres")
    if not 3 <= len(r["topics"]) <= 12: errs.append("deben ser de 3 a 12 topics")
    if r["personal"] and "jorgesuarez" not in r["topics"]: errs.append("falta el topic jorgesuarez")
    if mode == "--check":
        got = json.loads(subprocess.run(["gh", "api", f"repos/{OWNER}/{r['key']}"], capture_output=True, text=True, check=True).stdout)
        if (got.get("description") or "") != want["description"]: errs.append("descripción distinta en GitHub")
        if (got.get("homepage") or "").rstrip("/") != want["homepage"]: errs.append(f"sitio distinto en GitHub: {got.get('homepage')!r}")
        if sorted(got.get("topics") or []) != want["topics"]: errs.append(f"topics distintos en GitHub: {sorted(got.get('topics') or [])}")
    elif mode == "--apply":
        cmd = ["gh", "repo", "edit", f"{OWNER}/{r['key']}", "--description", want["description"], "--homepage", want["homepage"]]
        got = json.loads(subprocess.run(["gh", "api", f"repos/{OWNER}/{r['key']}"], capture_output=True, text=True, check=True).stdout)
        for t in want["topics"]: cmd += ["--add-topic", t]
        for t in sorted(set(got.get("topics") or []) - set(want["topics"])): cmd += ["--remove-topic", t]  # los que ya no están en los datos
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode: errs.append("gh no pudo escribir: " + res.stderr.strip()[:160])
    print(("FALLA " if errs else "ok    ") + r["key"])
    if errs or mode not in ("--check", "--apply"):
        print("   descripción:", want["description"]); print("   sitio:", want["homepage"] or "(vacío)"); print("   topics:", ", ".join(want["topics"]))
    for e in errs: print("   !", e)
    bad += bool(errs)
sys.exit(1 if bad else 0)

"""Captura escritorio, móvil y un recorrido (GIF y MP4) de cada producto en vivo.

Uso: python3 tools/readme-kit/capture.py DIR_SALIDA [repo ...]
Requiere Playwright con Chrome y ffmpeg. Respeta HTTPS_PROXY si existe.
"""
import asyncio, os, sys, subprocess, pathlib, shutil
from playwright.async_api import async_playwright
OUT = pathlib.Path(sys.argv[1])
TARGETS = {
 "game-industry-resources": "https://gamedev.jorgesuarez.com.mx/",
 "jorgesuarez.com.mx": "https://jorgesuarez.com.mx/",
 "master-prompt-builder": "https://mpb.jorgesuarez.com.mx/",
 "echomentor-ai": "https://echomentor.uetc.mx/",
 "sparkcrew-landing": "https://sparkcrew.jorgesuarez.com.mx/",
 "moki-pixel": "https://moki.jorgesuarez.com.mx/pixel/",
 "tecnimotostatus-site": "https://status.tecnimoto.mx/",
 "ardenstatus-site": "https://ardenstatus.jorgesuarez.com.mx/",
}
only = sys.argv[2:] 
async def main():
    async with async_playwright() as p:
        kw = {"proxy": {"server": os.environ["HTTPS_PROXY"]}} if os.environ.get("HTTPS_PROXY") else {}
        b = await p.chromium.launch(channel="chrome", **kw)
        for key, url in TARGETS.items():
            if only and key not in only: continue
            d = OUT / key; d.mkdir(parents=True, exist_ok=True)
            vd = d / "_v"; shutil.rmtree(vd, ignore_errors=True)
            ctx = await b.new_context(viewport={"width":1280,"height":720}, record_video_dir=str(vd), record_video_size={"width":1280,"height":720}, locale="es-MX")
            pg = await ctx.new_page()
            try:
                r = await pg.goto(url, wait_until="load", timeout=60000)
                await pg.wait_for_timeout(3000)
                await pg.screenshot(path=str(d/"desktop.png"))
                H = await pg.evaluate("Math.max(document.documentElement.scrollHeight, document.body.scrollHeight)")
                total = max(0, min(H-720, 4400)); y = 0
                while y < total:
                    y += 36; await pg.mouse.wheel(0, 36); await pg.wait_for_timeout(45)
                await pg.wait_for_timeout(900)
                title = await pg.title()
                print(key, r.status, "H", H, "|", title)
            except Exception as e:
                print(key, "ERROR", str(e)[:200])
            await ctx.close()
            vids = list(vd.glob("*.webm"))
            if vids:
                src = str(vids[0])
                subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","2.2","-i",src,"-t","9","-an","-vf","scale=1280:-2","-c:v","libx264","-crf","30","-pix_fmt","yuv420p","-movflags","+faststart",str(d/"tour.mp4")])
                subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","2.2","-i",src,"-t","7","-vf","fps=6,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=96[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4",str(d/"tour.gif")])
            shutil.rmtree(vd, ignore_errors=True)
            m = await b.new_context(viewport={"width":390,"height":780}, device_scale_factor=2, is_mobile=True, has_touch=True, locale="es-MX",
                 user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
            mp = await m.new_page()
            try:
                await mp.goto(url, wait_until="load", timeout=60000); await mp.wait_for_timeout(3000)
                await mp.screenshot(path=str(d/"mobile.png"))
            except Exception as e:
                print(key, "MOBILE ERROR", str(e)[:200])
            await m.close()
        await b.close()
asyncio.run(main())

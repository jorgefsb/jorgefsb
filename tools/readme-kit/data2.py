CAP = dict(
    es="Grabación real, sin retoque. Chromium con WebGL por software; no es una prueba en un teléfono físico.",
    en="Real recording, no retouching. Chromium with software WebGL; this is not a test on a physical phone.",
)

REPOS2 = [
    dict(
        key="moki-pixel", personal=True, media="custom", guide="docs/GUIA.md",
        title="Moki Pixel", live="https://moki.jorgesuarez.com.mx/pixel/",
        kicker=dict(es="VIDEOJUEGOS // KIT ABIERTO DE ANIMACIÓN", en="VIDEO GAMES // OPEN ANIMATION KIT"),
        promise=dict(es="Moki en pixel art, listo para jugar: 43 animaciones para tu juego, tu página y tu escritorio.",
                     en="Moki in pixel art, ready to play: 43 animations for your game, your page and your desktop."),
        chip=dict(es="V0.1.0 · PROPUESTA", en="V0.1.0 · PROPOSAL"),
        cta=dict(es="Verlo en vivo", en="See it live"),
        about="👾 Moki in pixel art, ready to play: an open animation kit (43 clips, 4 views, 3 sizes) for games, web and desktop pets, wallpapers and videos. · Moki en pixel art, listo para jugar.",
        topics=["pixel-art", "sprites", "gamedev", "animation", "moki", "jorgesuarez"],
        top=dict(es="""<p align="center">
  <img src="dist/gif/moki_wave_front.gif" width="120" alt="Moki saluda">
  <img src="dist/gif/moki_walk_right.gif" width="120" alt="Moki camina">
  <img src="dist/gif/moki_juggling_right.gif" width="120" alt="Moki hace malabares">
  <img src="dist/gif/moki_celebrate_right.gif" width="120" alt="Moki celebra">
  <img src="dist/gif/moki_sleep_right.gif" width="120" alt="Moki duerme">
</p>
<p align="center"><sub>Animaciones reales del kit, tal como salen de <code>dist/gif</code>.</sub></p>
""", en="""<p align="center">
  <img src="dist/gif/moki_wave_front.gif" width="120" alt="Moki waves">
  <img src="dist/gif/moki_walk_right.gif" width="120" alt="Moki walks">
  <img src="dist/gif/moki_juggling_right.gif" width="120" alt="Moki juggles">
  <img src="dist/gif/moki_celebrate_right.gif" width="120" alt="Moki celebrates">
  <img src="dist/gif/moki_sleep_right.gif" width="120" alt="Moki sleeps">
</p>
<p align="center"><sub>Real animations from the kit, straight out of <code>dist/gif</code>.</sub></p>
"""),
        body=dict(es="""## ¿Qué es?

Un kit abierto de animación para usar a Moki en juegos, páginas, apps, wallpapers, videos y en tu escritorio. Moki es el alter ego explorador de Jorge Suárez: descubre, se equivoca y construye mundos mientras aprende.

## ¿Para quién es?

- Para quien hace juegos en Phaser, Godot, Unity o GameMaker y quiere un personaje ya animado.
- Para quien tiene una página y quiere una mascota que camine por ella.
- Para quien usa Claude Code y quiere a Moki en su escritorio reaccionando a lo que hace.
- Para quien quiere hacer GIFs y videos con un personaje desde un guion.

## ¿Qué dolor resuelve?

Un personaje que solo existe como ilustración no se puede jugar. Para meterlo a un juego o a una página hay que dibujar cada cuadro, cada vista y cada tamaño, y al voltear el sprite se rompen detalles como el parche de la oreja.

## La propuesta

Moki no está dibujado cuadro por cuadro. Vive como un maniquí 3D sencillo que se convierte a pixel art, así que cualquier vista o tamaño sale consistente y el parche nunca cambia de lado. Lo hicimos para explorar y jugar con IA y videojuegos, y lo abrimos para que cualquiera pueda hacer lo mismo.

| Qué trae | Detalle |
|---|---|
| 43 animaciones | Locomoción, salto, gestos, emociones, actividades, descanso y modo mascota |
| 4 vistas | Derecha, izquierda, frente y espalda |
| 3 tamaños | 32, 64 y 128 px |
| 12 emotes y FX | Burbujas sobre el casco, polvo, chispas, confeti y sombra |
| Exportes para motores | Aseprite JSON (Phaser), Godot 4, GameMaker y Unity |
| Mascota web y de escritorio | macOS, Windows y Linux, con hooks de Claude Code |
| Videos y wallpapers | Guion JSON a MP4, WebM o GIF; 4 escenas en 6 tamaños |

<p align="center"><img src="dist/moki-hoja-de-personaje.png" width="640" alt="Hoja de personaje pixel art de Moki: vuelta completa, proporciones, paleta y expresiones"></p>

## ¿Cómo se usa?

En tu página, con una línea:

```html
<script src="https://moki.jorgesuarez.com.mx/pixel/dist/runtime/moki-pet.js" data-juice="poquito"></script>
```

En tu juego con Phaser 3:

```js
this.load.aseprite('moki', 'moki-64-right.png', 'moki-64-right.json');
this.anims.createFromAseprite('moki');
this.add.sprite(160, 120, 'moki').play({ key: 'walk', repeat: -1 });
```

En tu escritorio: descarga el instalador en [Releases](https://github.com/jorgefsb/moki-pixel/releases).

Componente web, Godot, Unity, GameMaker, videos y la skill para Claude están en la [guía completa](./docs/GUIA.md).

## ¿Cuándo conviene y cuándo no?

Conviene si quieres un personaje con animaciones listas para un prototipo, una página, un stream o un video.

Ten en cuenta:

- El arte de Moki no es para uso comercial sin permiso (CC BY-NC 4.0).
- Nunca espejes el sprite: usa el atlas `left`. El parche MOKI vive solo en su oreja derecha.
- Los instaladores de escritorio todavía no están firmados: macOS y Windows muestran un aviso.

## ¿Dónde lo pruebo?

En vivo: **[moki.jorgesuarez.com.mx/pixel](https://moki.jorgesuarez.com.mx/pixel/)**

{{SCREENS}}

## Hasta dónde llegamos

Versión 0.1.0. El diseño de Moki está aprobado desde el 12 de octubre de 2026; esta adaptación a pixel art es una propuesta sobre ese diseño.

Pendiente, con corte al 30 de octubre de 2026: la aprobación del kit, la prueba física de la mascota de escritorio en macOS, Windows y Linux, y la firma de los instaladores. El detalle vive en [docs/estado.md](./docs/estado.md).

## Para quien construye

```bash
npm install
npm run build        # sprites, tiras, Godot, GIFs, FX, runtime, hoja y wallpapers
npm run site         # sitio para moki.jorgesuarez.com.mx/pixel
```

Cómo está hecho, el canon de Moki y todas las integraciones: [guía completa](./docs/GUIA.md). Guías por tema: [personaje](./docs/guia-de-personaje.md), [arte pixel](./docs/guia-de-arte-pixel.md), [animación](./docs/animacion.md) y [escenas y video](./docs/escenas.md).

## Licencia y créditos

- Código: [MIT](./LICENSE).
- Arte de Moki: [CC BY-NC 4.0](./LICENSE-ART.md). Da crédito a «Moki por JorgeSuarez.com.mx» y escríbenos para usos comerciales.
- La idea nació viendo [Clawd](https://github.com/KebeliSamet0/clawd) de KebeliSamet0, una mascota pixel art de Claude para Windows.
""", en="""## What is it?

An open animation kit to use Moki in games, pages, apps, wallpapers, videos and on your desktop. Moki is Jorge Suárez's explorer alter ego: he discovers, gets things wrong and builds worlds while he learns.

## Who is it for?

- People making games in Phaser, Godot, Unity or GameMaker who want a character that is already animated.
- People with a website who want a pet walking around it.
- People who use Claude Code and want Moki on their desktop reacting to what they do.
- People who want to make GIFs and videos with a character from a script.

## What pain does it solve?

A character that only exists as an illustration cannot be played. To put it in a game or on a page you have to draw every frame, every view and every size, and flipping the sprite breaks details like the ear patch.

## The proposal

Moki is not drawn frame by frame. He lives as a simple 3D mannequin that is converted to pixel art, so every view and size comes out consistent and the patch never changes sides. We made it to explore and play with AI and video games, and we opened it so anyone can do the same.

| What you get | Detail |
|---|---|
| 43 animations | Locomotion, jump, gestures, emotions, activities, rest and pet mode |
| 4 views | Right, left, front and back |
| 3 sizes | 32, 64 and 128 px |
| 12 emotes and FX | Bubbles over the helmet, dust, sparks, confetti and shadow |
| Engine exports | Aseprite JSON (Phaser), Godot 4, GameMaker and Unity |
| Web and desktop pet | macOS, Windows and Linux, with Claude Code hooks |
| Videos and wallpapers | JSON script to MP4, WebM or GIF; 4 scenes in 6 sizes |

<p align="center"><img src="dist/moki-hoja-de-personaje.png" width="640" alt="Moki pixel art character sheet: full turnaround, proportions, palette and expressions"></p>

## How do I use it?

On your page, with one line:

```html
<script src="https://moki.jorgesuarez.com.mx/pixel/dist/runtime/moki-pet.js" data-juice="poquito"></script>
```

In your game with Phaser 3:

```js
this.load.aseprite('moki', 'moki-64-right.png', 'moki-64-right.json');
this.anims.createFromAseprite('moki');
this.add.sprite(160, 120, 'moki').play({ key: 'walk', repeat: -1 });
```

On your desktop: download the installer from [Releases](https://github.com/jorgefsb/moki-pixel/releases).

The web component, Godot, Unity, GameMaker, videos and the Claude skill are covered in the [full guide](./docs/GUIA.md) (in Spanish).

## When it fits and when it doesn't

It fits if you want a character with ready-made animations for a prototype, a page, a stream or a video.

Keep in mind:

- Moki's art is not for commercial use without permission (CC BY-NC 4.0).
- Never mirror the sprite: use the `left` atlas. The MOKI patch lives only on his right ear.
- The desktop installers are not signed yet: macOS and Windows show a warning.

## Where can I try it?

Live: **[moki.jorgesuarez.com.mx/pixel](https://moki.jorgesuarez.com.mx/pixel/)**

{{SCREENS}}

## How far we got

Version 0.1.0. Moki's design has been approved since 12 October 2026; this pixel art adaptation is a proposal built on that design.

Pending as of 30 October 2026: approval of the kit, a physical test of the desktop pet on macOS, Windows and Linux, and signing the installers. Details live in [docs/estado.md](./docs/estado.md) (in Spanish).

## For builders

```bash
npm install
npm run build        # sprites, strips, Godot, GIFs, FX, runtime, sheet and wallpapers
npm run site         # site for moki.jorgesuarez.com.mx/pixel
```

How it is made, Moki's canon and every integration: [full guide](./docs/GUIA.md). Guides by topic, in Spanish: [character](./docs/guia-de-personaje.md), [pixel art](./docs/guia-de-arte-pixel.md), [animation](./docs/animacion.md) and [scenes and video](./docs/escenas.md).

## License and credits

- Code: [MIT](./LICENSE).
- Moki's art: [CC BY-NC 4.0](./LICENSE-ART.md). Credit "Moki by JorgeSuarez.com.mx" and write to us for commercial use.
- The idea came from [Clawd](https://github.com/KebeliSamet0/clawd) by KebeliSamet0, a pixel art Claude pet for Windows.
"""),
    ),
    dict(
        key="cursor-liquido", personal=True, media="custom", guide="docs/GUIA-TECNICA.md",
        title="Cursor líquido", live="https://github.com/jorgefsb/cursor-liquido/releases/tag/v1.0.1",
        kicker=dict(es="VIDEOJUEGOS // EFECTO WEB ABIERTO", en="VIDEO GAMES // OPEN WEB EFFECT"),
        promise=dict(es="Una estela para el puntero de tu sitio que no estorba: tu cursor sigue siendo tu cursor.",
                     en="A pointer trail for your site that stays out of the way: your cursor is still your cursor."),
        chip=dict(es="V1.0.1 · MIT", en="V1.0.1 · MIT"),
        cta=dict(es="Descargar la versión 1.0.1", en="Download version 1.0.1"),
        about="✨ A pointer trail for your website: light dots or a WebGL2 fluid that flows around your page blocks. Native cursor stays, no runtime deps, MIT. · Una estela para el puntero de tu sitio.",
        topics=["cursor-effect", "webgl", "game-feel", "web-interaction", "javascript", "jorgesuarez"],
        top=dict(es="""<p align="center"><img src="docs/media/cursor-liquido-demo.gif" width="720" alt="Cursor líquido en intensidad Hardcore: un fluido de colores sigue al puntero y rodea un bloque de la página"></p>
<p align="center"><sub>Grabación real, sin retoque. Chromium con WebGL por software. <a href="docs/media/cursor-liquido-restaurado-real.mp4">Ver el video MP4</a></sub></p>
""", en="""<p align="center"><img src="docs/media/cursor-liquido-demo.gif" width="720" alt="Cursor líquido at Hardcore intensity: a colorful fluid follows the pointer and flows around a block on the page"></p>
<p align="center"><sub>Real recording, no retouching. Chromium with software WebGL. <a href="docs/media/cursor-liquido-restaurado-real.mp4">Watch the MP4 video</a></sub></p>
"""),
        body=dict(es="""## ¿Qué es?

Una estela para el puntero de tu sitio web. Puede ser de puntitos ligeros o un fluido WebGL2 que choca con los bloques de tu página.

## ¿Para quién es?

Para quien tiene un sitio y quiere que se sienta vivo sin contratar a nadie ni cargar una librería pesada. Si te gustan los efectos de las páginas de Jorge, este es ese cursor, gratis.

## ¿Qué dolor resuelve?

Los efectos de cursor suelen estorbar: reemplazan el puntero, tapan clics, traen dependencias o marean a quien pidió menos movimiento.

## La propuesta

Un efecto que acompaña y no manda:

- El cursor del sistema no cambia.
- La capa decorativa no intercepta clics.
- No hay dependencias en runtime.
- Con movimiento reducido no hay efecto.
- Tú eliges la intensidad al integrar. No se le pregunta nada al visitante.

| Intensidad | Qué dibuja |
|---|---|
| `nada` | Nada |
| `poquito` | Puntitos de 7 px que caen y se apagan. Sin WebGL |
| `mucho` | Fluido WebGL2 multicolor, radio de 10 px |
| `hardcore` | Fluido WebGL2 multicolor, radio de 18 px |

| Poquito | Mucho | Hardcore | Choque con un bloque |
|---|---|---|---|
| ![Poquito](docs/media/poquito-real.png) | ![Mucho](docs/media/mucho-real.png) | ![Hardcore](docs/media/hardcore-real.png) | ![Contacto](docs/media/contact-real.png) |

## ¿Cómo se usa?

1. Descarga la [versión 1.0.1](https://github.com/jorgefsb/cursor-liquido/releases/tag/v1.0.1).
2. Copia `dist/` a tu sitio como `/vendor/cursor-liquido/`.
3. Pega esto en tu página:

```html
<link rel="stylesheet" href="/vendor/cursor-liquido/cursor-liquido.css">
<script src="/vendor/cursor-liquido/cursor-liquido.js"></script>
<script>
  LiquidCursor.mount({ intensity: 'poquito' })
</script>
```

4. Marca los bloques que el fluido debe rodear:

```html
<aside data-liquid-obstacle>…</aside>
```

## ¿Cuándo conviene y cuándo no?

Conviene en sitios de fondo oscuro, donde el fluido se aprecia mejor, y cuando quieres decidir tú la intensidad.

Límites de hoy:

- No está publicado en npm. No uses `npm install cursor-liquido`.
- No hay demo pública todavía. Abre `demo/index.html` en tu navegador; funciona sin servidor.
- El tacto viene apagado y no se probó en teléfonos físicos.
- Sin WebGL2, `mucho` y `hardcore` se apagan y `poquito` sigue.

## ¿Dónde lo pruebo?

Descarga: **[versión 1.0.1](https://github.com/jorgefsb/cursor-liquido/releases/tag/v1.0.1)**. Demo local: `demo/index.html`.

## Hasta dónde llegamos

Versión 1.0.1 estable, con licencia MIT. La suite corre 42 casos en navegador real y 8 comparaciones de calidad.

En ideas, sin implementar: una intensidad más, «Legendario». Está en [docs/roadmap.md](./docs/roadmap.md).

## Para quien construye

```sh
npm ci
npm test               # hash del motor, build determinista, manifest, sintaxis y privacidad
npm run test:browser   # navegador real sobre dist/
npm run test:quality   # comparaciones de reducción de calidad
```

API, opciones, integración con Juice y Game Feel, accesibilidad y rollback: [guía técnica](./docs/GUIA-TECNICA.md) y [docs/api.md](./docs/api.md).

## Licencia y créditos

Código MIT, (c) 2026 Jorge Suárez ([LICENSE](./LICENSE)). El sombreado del fluido está adaptado de WebGL Fluid Simulation de Pavel Dobryakov (MIT); ver [THIRD_PARTY_NOTICES](./THIRD_PARTY_NOTICES). Este repo no incluye ni licencia a Moki ni otros recursos de marca.
""", en="""## What is it?

A pointer trail for your website. It can be light dots or a WebGL2 fluid that collides with the blocks on your page.

## Who is it for?

For anyone with a site who wants it to feel alive without hiring anyone or loading a heavy library. If you like the effects on Jorge's pages, this is that cursor, for free.

## What pain does it solve?

Cursor effects tend to get in the way: they replace the pointer, cover clicks, bring dependencies or make people who asked for less motion feel sick.

## The proposal

An effect that follows along and does not take over:

- The system cursor does not change.
- The decorative layer never intercepts clicks.
- No runtime dependencies.
- With reduced motion there is no effect.
- You choose the intensity when you integrate it. The visitor is never asked anything.

| Intensity | What it draws |
|---|---|
| `nada` | Nothing |
| `poquito` | 7 px dots that fall and fade. No WebGL |
| `mucho` | Multicolor WebGL2 fluid, 10 px radius |
| `hardcore` | Multicolor WebGL2 fluid, 18 px radius |

| Poquito | Mucho | Hardcore | Hitting a block |
|---|---|---|---|
| ![Poquito](docs/media/poquito-real.png) | ![Mucho](docs/media/mucho-real.png) | ![Hardcore](docs/media/hardcore-real.png) | ![Contact](docs/media/contact-real.png) |

## How do I use it?

1. Download [version 1.0.1](https://github.com/jorgefsb/cursor-liquido/releases/tag/v1.0.1).
2. Copy `dist/` to your site as `/vendor/cursor-liquido/`.
3. Paste this into your page:

```html
<link rel="stylesheet" href="/vendor/cursor-liquido/cursor-liquido.css">
<script src="/vendor/cursor-liquido/cursor-liquido.js"></script>
<script>
  LiquidCursor.mount({ intensity: 'poquito' })
</script>
```

4. Mark the blocks the fluid should flow around:

```html
<aside data-liquid-obstacle>…</aside>
```

## When it fits and when it doesn't

It fits on dark sites, where the fluid shows best, and when you want to decide the intensity yourself.

Today's limits:

- It is not published on npm. Do not run `npm install cursor-liquido`.
- There is no public demo yet. Open `demo/index.html` in your browser; it works without a server.
- Touch is off by default and it was not tested on physical phones.
- Without WebGL2, `mucho` and `hardcore` turn off and `poquito` keeps working.

## Where can I try it?

Download: **[version 1.0.1](https://github.com/jorgefsb/cursor-liquido/releases/tag/v1.0.1)**. Local demo: `demo/index.html`.

## How far we got

Stable version 1.0.1 under the MIT license. The suite runs 42 cases in a real browser and 8 quality comparisons.

An idea that is not implemented: one more intensity, "Legendario". It is in [docs/roadmap.md](./docs/roadmap.md) (in Spanish).

## For builders

```sh
npm ci
npm test               # engine hash, deterministic build, manifest, syntax and privacy
npm run test:browser   # real browser on dist/
npm run test:quality   # quality reduction comparisons
```

API, options, Juice and Game Feel integration, accessibility and rollback: [technical guide](./docs/GUIA-TECNICA.md) and [docs/api.md](./docs/api.md) (in Spanish, with an English usage section).

## License and credits

MIT code, (c) 2026 Jorge Suárez ([LICENSE](./LICENSE)). The fluid shader is adapted from WebGL Fluid Simulation by Pavel Dobryakov (MIT); see [THIRD_PARTY_NOTICES](./THIRD_PARTY_NOTICES). This repo does not include or license Moki or any other brand asset.
"""),
    ),
    dict(
        key="game-feel", personal=True, media="custom", guide="docs/GUIA-TECNICA.md",
        title="Game Feel", live="https://github.com/jorgefsb/game-feel/releases/tag/v1.0.1",
        kicker=dict(es="VIDEOJUEGOS // MÉTODO Y ADAPTADOR", en="VIDEO GAMES // METHOD AND ADAPTER"),
        promise=dict(es="Que tu página responda como responde un juego, y que cada quien elija cuánto.",
                     en="Make your page respond the way a game does, and let each person choose how much."),
        chip=dict(es="V1.0.1 · MIT", en="V1.0.1 · MIT"),
        cta=dict(es="Ver la versión 1.0.1", en="See version 1.0.1"),
        about="🕹️ Make a web page respond like a game: a method and adapter where each visitor chooses the intensity. No mascot required, MIT. · Que tu página responda como responde un juego.",
        topics=["game-feel", "gamedev", "web-interaction", "microinteractions", "javascript", "jorgesuarez"],
        top=dict(es="""<p align="center"><img src="docs/media/demo.gif" width="720" alt="Demo real de Game Feel: el menú Juega cambia la intensidad y la estela del cursor responde"></p>
<p align="center"><sub>Grabación real de <code>examples/</code>, con eventos reales del puntero. Chromium con WebGL por software. <a href="docs/media/demo.mp4">Ver el video MP4</a></sub></p>
""", en="""<p align="center"><img src="docs/media/demo.gif" width="720" alt="Real Game Feel demo: the Juega menu changes the intensity and the cursor trail responds"></p>
<p align="center"><sub>Real recording of <code>examples/</code>, with real pointer events. Chromium with software WebGL. <a href="docs/media/demo.mp4">Watch the MP4 video</a></sub></p>
"""),
        body=dict(es="""## ¿Qué es?

Un método y un adaptador genérico para que una página responda a lo que haces. Conecta el menú «Juega» de juice con [Cursor líquido](https://github.com/jorgefsb/cursor-liquido), sin mascota obligatoria.

## ¿Para quién es?

Para equipos y marcas con sitio propio que quieren microinteracciones, sonido y estela de cursor con su propia identidad.

## ¿Qué dolor resuelve?

La mayoría de las páginas no responden: tocas, escribes o guardas y no pasa nada. Y cuando alguien les mete efectos, deciden por la persona: suenan sin permiso, tapan clics o no respetan a quien pidió menos movimiento.

## La propuesta

Tratar una página como se trata un juego. La persona abre «Juega» y elige cuánto responde el sitio. El adaptador respeta su elección de nivel y sonido, y nunca bloquea clics, escritura ni scroll.

| Juega | Valor | Qué pasa con el cursor |
|---|---|---|
| Nada | `off` | Sin efecto. Movimiento reducido fuerza este nivel |
| Poquito | `subtle` | Puntos de 7 px, sin WebGL |
| Mucho | `full` | Fluido con radio de 10 px |
| Hardcore | `hard` | Fluido con radio de 18 px |

| Poquito | Mucho | Hardcore |
|---|---|---|
| ![Poquito: puntos](docs/media/poquito.png) | ![Mucho: fluido de 10 px](docs/media/mucho.png) | ![Hardcore: fluido de 18 px](docs/media/hardcore.png) |

## ¿Cómo se usa?

Para probarlo en tu máquina necesitas Node.js 20 o posterior:

```sh
npm ci
npm run setup
npm run demo
```

Abre la dirección que imprime el servidor y entra a `/examples/`.

Para ponerlo en otra página, sirve desde tu propio dominio juice 1.2.0, Cursor líquido 1.0.1 y `src/game-feel-cursor.{js,css}`, y llama:

```js
GameFeelCursor.mount({ requireJuice: true })
```

Ponerlo en un sitio requiere integración técnica. El orden de scripts y las opciones están en [docs/integration.md](./docs/integration.md).

## ¿Cuándo conviene y cuándo no?

Conviene cuando tienes una marca propia y quieres que tu sitio se sienta al tocarlo.

No conviene si lo que quieres es a Moki: eso es [Papacito Juice](https://github.com/jorgefsb/papacito-juice), y Moki no se licencia. Tampoco hay paquete en npm ni prueba en teléfonos físicos.

## ¿Dónde lo pruebo?

**[Versión 1.0.1](https://github.com/jorgefsb/game-feel/releases/tag/v1.0.1)** y la demo local de `examples/`. En vivo lo ves funcionando en [jorgesuarez.com.mx](https://jorgesuarez.com.mx), con el perfil de la marca personal.

## Hasta dónde llegamos

Versión 1.0.1, MIT. Cuatro niveles estables; no hay quinto. La suite cubre niveles, controles, desmontaje, móvil emulado, movimiento reducido y preferencias.

Límite conocido: en WebGL por software el motor puede bajar la calidad o pausarse si se pasa de su presupuesto.

## Para quien construye

```sh
npm run verify        # compara los archivos en disco contra hashes fijados
npm test
npm run test:browser
```

Versiones fijadas, garantías, arquitectura y principios: [guía técnica](./docs/GUIA-TECNICA.md), [arquitectura](./docs/architecture.md) y [principios](./docs/design-principles.md).

## Licencia

Código e instrucciones: [MIT](./LICENSE). Moki, su arte y la marca personal no son MIT y no se concede permiso de reutilización. Ver [NOTICES](./NOTICES).
""", en="""## What is it?

A method and a generic adapter that make a page respond to what you do. It connects the juice «Juega» menu with [Cursor líquido](https://github.com/jorgefsb/cursor-liquido), with no mascot required.

## Who is it for?

For teams and brands with their own site who want microinteractions, sound and a cursor trail in their own identity.

## What pain does it solve?

Most pages do not respond: you tap, type or save and nothing happens. And when someone adds effects, they decide for the person: they play sound without permission, cover clicks or ignore people who asked for less motion.

## The proposal

Treat a page the way you treat a game. The person opens «Juega» and chooses how much the site responds. The adapter respects their level and sound choice, and never blocks clicks, typing or scrolling.

| Juega | Value | What the cursor does |
|---|---|---|
| Nada | `off` | No effect. Reduced motion forces this level |
| Poquito | `subtle` | 7 px dots, no WebGL |
| Mucho | `full` | Fluid with a 10 px radius |
| Hardcore | `hard` | Fluid with an 18 px radius |

| Poquito | Mucho | Hardcore |
|---|---|---|
| ![Poquito: dots](docs/media/poquito.png) | ![Mucho: 10 px fluid](docs/media/mucho.png) | ![Hardcore: 18 px fluid](docs/media/hardcore.png) |

## How do I use it?

To try it on your machine you need Node.js 20 or later:

```sh
npm ci
npm run setup
npm run demo
```

Open the address the server prints and go to `/examples/`.

To put it on another page, serve juice 1.2.0, Cursor líquido 1.0.1 and `src/game-feel-cursor.{js,css}` from your own domain, then call:

```js
GameFeelCursor.mount({ requireJuice: true })
```

Putting it on a site takes technical integration. Script order and options are in [docs/integration.md](./docs/integration.md) (in Spanish).

## When it fits and when it doesn't

It fits when you have your own brand and want your site to respond to touch.

It does not fit if what you want is Moki: that is [Papacito Juice](https://github.com/jorgefsb/papacito-juice), and Moki is not licensed. There is no npm package and no test on physical phones.

## Where can I try it?

**[Version 1.0.1](https://github.com/jorgefsb/game-feel/releases/tag/v1.0.1)** and the local demo in `examples/`. You can see it working live at [jorgesuarez.com.mx](https://jorgesuarez.com.mx), with the personal brand profile.

## How far we got

Version 1.0.1, MIT. Four stable levels; there is no fifth. The suite covers levels, controls, unmounting, emulated mobile, reduced motion and preferences.

Known limit: on software WebGL the engine may lower quality or pause if it goes over its budget.

## For builders

```sh
npm run verify        # compares files on disk against pinned hashes
npm test
npm run test:browser
```

Pinned versions, guarantees, architecture and principles, in Spanish: [technical guide](./docs/GUIA-TECNICA.md), [architecture](./docs/architecture.md) and [principles](./docs/design-principles.md).

## License

Code and instructions: [MIT](./LICENSE). Moki, his art and the personal brand are not MIT and no reuse permission is granted. See [NOTICES](./NOTICES).
"""),
    ),
    dict(
        key="papacito-juice", personal=True, media="custom", guide="docs/GUIA-TECNICA.md",
        title="Papacito Juice", live="https://jorgesuarez.com.mx",
        kicker=dict(es="VIDEOJUEGOS // PERFIL DE MARCA", en="VIDEO GAMES // BRAND PROFILE"),
        promise=dict(es="Lo que hace que los sitios de Jorge se sientan al tocarlos: sonido, Moki y cursor en un solo menú.",
                     en="What makes Jorge's sites respond to touch: sound, Moki and cursor in a single menu."),
        chip=dict(es="V1.0.1 · MIT (SIN MOKI)", en="V1.0.1 · MIT (NO MOKI)"),
        cta=dict(es="Verlo en vivo en jorgesuarez.com.mx", en="See it live at jorgesuarez.com.mx"),
        about="🧃 The Game Feel profile of Jorge Suárez's personal brand: microinteractions, sound, Moki and Liquid Cursor from one «Juega» menu. · Lo que hace que los sitios de Jorge se sientan al tocarlos.",
        topics=["game-feel", "microinteractions", "moki", "web-interaction", "javascript", "jorgesuarez"],
        top=dict(es="""<p align="center"><img src="docs/media/demo.gif" width="720" alt="Demo real de Papacito Juice: el menú Juega cambia la intensidad y la estela del cursor responde"></p>
<p align="center"><sub>Grabación real de <code>examples/</code>, con eventos reales del puntero. Chromium con WebGL por software. <a href="docs/media/demo.mp4">Ver el video MP4</a></sub></p>
""", en="""<p align="center"><img src="docs/media/demo.gif" width="720" alt="Real Papacito Juice demo: the Juega menu changes the intensity and the cursor trail responds"></p>
<p align="center"><sub>Real recording of <code>examples/</code>, with real pointer events. Chromium with software WebGL. <a href="docs/media/demo.mp4">Watch the MP4 video</a></sub></p>
"""),
        body=dict(es="""## ¿Qué es?

El perfil de [Game Feel](https://github.com/jorgefsb/game-feel) de la marca personal de Jorge Suárez. Coordina microinteracciones, sonido, Moki y [Cursor líquido](https://github.com/jorgefsb/cursor-liquido) desde el menú «Juega».

## ¿Para quién es?

Para los sitios de la marca personal de Jorge y para quien mantiene esos sitios. También sirve de ejemplo si quieres ver cómo se arma un perfil de marca encima de Game Feel.

Si lo quieres en tu propio sitio, usa Game Feel. Moki no se licencia.

## ¿Qué dolor resuelve?

Cada sitio de la marca tiene que sentirse igual: los mismos niveles, el mismo sonido, el mismo Moki. Copiar piezas sueltas de un sitio a otro termina en versiones distintas que ya nadie puede comparar.

## La propuesta

Un solo paquete, con versiones fijadas y verificadas por hash, que cualquier sitio de la marca instala igual.

- Exige a Moki real: comprueba sus 12 poses y, si falta algo, no se monta.
- Moki se queda quieto en Nada y conserva sus escondidas diarias.
- Hardcore se desbloquea al encontrar a los Mokis del día.
- El perfil nunca escribe por su cuenta el nivel, el sonido ni el desbloqueo: eso lo decide la persona.

| Poquito | Mucho | Hardcore | Moki |
|---|---|---|---|
| ![Poquito](docs/media/poquito.png) | ![Mucho](docs/media/mucho.png) | ![Hardcore](docs/media/hardcore.png) | ![Moki en la demo](docs/media/moki.png) |

## ¿Cómo se usa?

Como visitante: abre «Juega» en cualquier sitio de la marca y elige Nada, Poquito o Mucho. Busca a Moki en los bordes.

Como quien integra, con Node.js 20 o posterior:

```sh
npm ci
npm run setup
npm run demo
```

Y en la página:

```js
await PapacitoJuice.mount({ page: 'page' })
```

El orden de scripts y las opciones están en [docs/integration.md](./docs/integration.md).

## ¿Cuándo conviene y cuándo no?

Conviene solo en sitios de la marca personal de Jorge.

No va en sitios de Amber, Arden, Sparkplug o TecniMoto, ni en documentos formales, legales o páginas de pago. Así lo marca el [BrandKit](https://brandkit.jorgesuarez.com.mx/#juega).

## ¿Dónde lo pruebo?

En vivo: **[jorgesuarez.com.mx](https://jorgesuarez.com.mx)** y **[brandkit.jorgesuarez.com.mx](https://brandkit.jorgesuarez.com.mx/#juega)**.

## Hasta dónde llegamos

Versión 1.0.1. Trabaja sobre juice 1.2.0, Cursor líquido 1.0.1 y Game Feel 1.0.1, todos verificados contra sus hashes.

Mismo límite que Game Feel: en WebGL por software el motor puede bajar la calidad o pausarse, y no se probó en teléfonos físicos.

## Para quien construye

```sh
npm run verify
npm test
npm run test:browser
```

Versiones, garantías, arquitectura y principios: [guía técnica](./docs/GUIA-TECNICA.md), [arquitectura](./docs/architecture.md) y [principios](./docs/design-principles.md).

## Licencia

Código e instrucciones: [MIT](./LICENSE). Moki, su arte y la marca personal no son MIT y no se concede permiso de reutilización. Los archivos de Moki no vienen en este repo. Ver [NOTICES](./NOTICES).
""", en="""## What is it?

The [Game Feel](https://github.com/jorgefsb/game-feel) profile of Jorge Suárez's personal brand. It coordinates microinteractions, sound, Moki and [Cursor líquido](https://github.com/jorgefsb/cursor-liquido) from the «Juega» menu.

## Who is it for?

For the sites of Jorge's personal brand and the people who maintain them. It also works as an example if you want to see how a brand profile is built on top of Game Feel.

If you want this on your own site, use Game Feel. Moki is not licensed.

## What pain does it solve?

Every site of the brand has to feel the same: the same levels, the same sound, the same Moki. Copying loose pieces from one site to another ends in different versions nobody can compare anymore.

## The proposal

One package, with pinned versions verified by hash, that every site of the brand installs the same way.

- It requires the real Moki: it checks his 12 poses and refuses to mount if anything is missing.
- Moki stays still on Nada and keeps his daily hiding spots.
- Hardcore unlocks when you find the Mokis of the day.
- The profile never writes the level, the sound or the unlock by itself: the person decides that.

| Poquito | Mucho | Hardcore | Moki |
|---|---|---|---|
| ![Poquito](docs/media/poquito.png) | ![Mucho](docs/media/mucho.png) | ![Hardcore](docs/media/hardcore.png) | ![Moki in the demo](docs/media/moki.png) |

## How do I use it?

As a visitor: open «Juega» on any site of the brand and choose Nada, Poquito or Mucho. Look for Moki at the edges.

As an integrator, with Node.js 20 or later:

```sh
npm ci
npm run setup
npm run demo
```

And on the page:

```js
await PapacitoJuice.mount({ page: 'page' })
```

Script order and options are in [docs/integration.md](./docs/integration.md) (in Spanish).

## When it fits and when it doesn't

It fits only on sites of Jorge's personal brand.

It does not go on Amber, Arden, Sparkplug or TecniMoto sites, or on formal documents, legal pages or payment pages. The [BrandKit](https://brandkit.jorgesuarez.com.mx/#juega) says so.

## Where can I try it?

Live: **[jorgesuarez.com.mx](https://jorgesuarez.com.mx)** and **[brandkit.jorgesuarez.com.mx](https://brandkit.jorgesuarez.com.mx/#juega)**.

## How far we got

Version 1.0.1. It runs on juice 1.2.0, Cursor líquido 1.0.1 and Game Feel 1.0.1, all verified against their hashes.

Same limit as Game Feel: on software WebGL the engine may lower quality or pause, and it was not tested on physical phones.

## For builders

```sh
npm run verify
npm test
npm run test:browser
```

Versions, guarantees, architecture and principles, in Spanish: [technical guide](./docs/GUIA-TECNICA.md), [architecture](./docs/architecture.md) and [principles](./docs/design-principles.md).

## License

Code and instructions: [MIT](./LICENSE). Moki, his art and the personal brand are not MIT and no reuse permission is granted. Moki's files do not ship in this repo. See [NOTICES](./NOTICES).
"""),
    ),
]

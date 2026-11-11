G = "https://gamedev.jorgesuarez.com.mx"

REPOS1 = [
    dict(
        key="game-industry-resources", personal=True, media="capture",
        title="Game Industry Resources", live=G,
        kicker=dict(es="VIDEOJUEGOS // RECURSOS ABIERTOS", en="VIDEO GAMES // OPEN RESOURCES"),
        promise=dict(es="El mapa para hacer juegos en Latinoamérica: cifras, estudios, chamba y herramientas.",
                     en="The map for making games in Latin America: numbers, studios, jobs and tools."),
        chip=dict(es="EN LÍNEA · GRATIS", en="LIVE · FREE"),
        cta=dict(es="Abrir el sitio", en="Open the site"),
        about="🎮 The map for making games in LATAM: industry numbers, studios, jobs, tools, marketing and an AI tools directory. Free. · El mapa para hacer juegos en Latinoamérica.",
        topics=["gamedev", "video-games", "latam", "game-industry", "jorgesuarez"],
        body=dict(es=f"""## ¿Qué es?

Un sitio gratis con el mapa para hacer videojuegos en Latinoamérica: cifras del sector, estudios de la región, trabajo y carrera, herramientas de producción, marketing y un directorio de herramientas de IA. Está en español, con versión en inglés.

## ¿Para quién es?

Para quien ya hace videojuegos en la región o quiere entrar: estudiantes, devs indie, gente que busca su primera chamba en la industria y quienes están fundando un estudio.

## ¿Qué dolor resuelve?

La información para vivir de hacer videojuegos en LATAM está regada. Saber qué estudios existen, dónde hay trabajo, cómo armar un CV para la industria o qué herramienta de IA le sirve a tu juego obliga a juntar piezas de muchos lados.

## La propuesta

Juntarlo en un solo mapa, curado desde más de dos décadas de hacer videojuegos, estudios y comunidad en México, y dejarlo abierto. Cada sección contesta una pregunta:

| Sección | Qué contesta |
|---|---|
| [Production Tools]({G}/tools) | ¿Con qué herramientas se produce un juego? |
| [Jobs & Career]({G}/jobs) | ¿Dónde hay trabajo y cómo me preparo? |
| [El CV Perfecto]({G}/guides/cv) | ¿Cómo armo un currículum para la industria? |
| [Studios DB]({G}/database) | ¿Qué estudios hay en Latinoamérica? |
| [Marketing Playbook]({G}/marketing) | ¿Cómo vendo mi juego y gano visibilidad? |
| [Pulso de la industria MX]({G}/industria) | ¿Cómo se ve el sector? Corte 2024-2025. |
| [Ecosistema MX]({G}/ecosistema) | ¿Qué estudios, comunidades, eventos y escuelas hay en México? |
| [Ciclo de producción]({G}/ciclo) | ¿Dónde encaja un gamedev de LATAM en pre, producción y post? |
| [Directorio de IA]({G}/ia/) | ¿Qué herramientas de IA sirven para arte, código, audio, 3D, QA y marketing? |

## ¿Cómo se usa?

1. Entra a [gamedev.jorgesuarez.com.mx]({G}).
2. Elige la sección que contesta tu pregunta.
3. No pide registro ni instalación.

## ¿Cuándo conviene y cuándo no?

Conviene cuando quieres orientarte, encontrar estudios, prepararte para una vacante o elegir herramientas.

No es un censo ni el pulso en vivo del sector: las cifras son un corte histórico 2024-2025 y el sitio lo marca así. Tampoco es una bolsa de trabajo oficial.

## ¿Dónde lo pruebo?

En vivo: **[gamedev.jorgesuarez.com.mx]({G})**

{{{{SCREENS}}}}

## Hasta dónde llegamos

En línea y en crecimiento. Hoy tiene nueve secciones y el directorio de IA.

Este repo también guarda `juice`, el paquete de interacción que usan los sitios de la marca (menú «Juega», sonido y Moki escondido), en sus versiones 1.0.0 a 1.2.0.

Lo que falta es seguir llenando el mapa. Si conoces un recurso que debería estar, abre un issue o manda un pull request.

## Para quien construye

Sitio estático, sin paso de build.

```bash
git clone https://github.com/jorgefsb/game-industry-resources.git
cd game-industry-resources
python3 -m http.server 3000
```

En producción se sirve como assets estáticos de un Worker de Cloudflare; `.assetsignore` lista lo que no se sube. Más contexto en [WALKTHROUGH.md](./WALKTHROUGH.md) y [BRAND-GUIDELINES.md](./BRAND-GUIDELINES.md).

## Licencia

Este repo no tiene archivo de licencia, así que el contenido conserva todos los derechos. Si quieres reutilizar algo, escríbenos a [jorgefsb@gmail.com](mailto:jorgefsb@gmail.com).
""", en=f"""## What is it?

A free site with the map for making video games in Latin America: industry numbers, studios in the region, jobs and careers, production tools, marketing and a directory of AI tools. It is written in Spanish and has an English version.

## Who is it for?

For people who already make games in the region or want to get in: students, indie devs, people looking for their first job in the industry and founders starting a studio.

## What pain does it solve?

The information you need to make a living making games in LATAM is scattered. Finding out which studios exist, where the jobs are, how to write a CV for the industry or which AI tool fits your game means collecting pieces from many places.

## The proposal

Put it on one map, curated from more than two decades of building games, studios and community in Mexico, and keep it open. Each section answers one question:

| Section | The question it answers |
|---|---|
| [Production Tools]({G}/tools) | Which tools do you use to produce a game? |
| [Jobs & Career]({G}/jobs) | Where are the jobs and how do I prepare? |
| [The Perfect CV]({G}/guides/cv) | How do I write a CV for the industry? |
| [Studios DB]({G}/database) | Which studios exist in Latin America? |
| [Marketing Playbook]({G}/marketing) | How do I sell my game and get visibility? |
| [Mexico industry pulse]({G}/industria) | What does the sector look like? 2024-2025 snapshot. |
| [Mexico ecosystem]({G}/ecosistema) | Which studios, communities, events and schools exist in Mexico? |
| [Production cycle]({G}/ciclo) | Where does a LATAM gamedev fit in pre-production, production and post? |
| [AI directory]({G}/ia/) | Which AI tools help with art, code, audio, 3D, QA and marketing? |

## How do I use it?

1. Go to [gamedev.jorgesuarez.com.mx]({G}).
2. Pick the section that answers your question.
3. No sign-up and nothing to install.

## When it fits and when it doesn't

It fits when you want to get oriented, find studios, prepare for a job opening or choose tools.

It is not a census or a live pulse of the sector: the numbers are a historical 2024-2025 snapshot and the site labels them that way. It is not an official job board either.

## Where can I try it?

Live: **[gamedev.jorgesuarez.com.mx]({G})**

{{{{SCREENS}}}}

## How far we got

Live and growing. Today it has nine sections plus the AI directory.

This repo also holds `juice`, the interaction package used by the brand's sites (the «Juega» menu, sound and hidden Moki), in versions 1.0.0 to 1.2.0.

What is missing is more of the map. If you know a resource that belongs here, open an issue or send a pull request.

## For builders

Static site, no build step.

```bash
git clone https://github.com/jorgefsb/game-industry-resources.git
cd game-industry-resources
python3 -m http.server 3000
```

In production it is served as the static assets of a Cloudflare Worker; `.assetsignore` lists what is not uploaded. More context in [WALKTHROUGH.md](./WALKTHROUGH.md) and [BRAND-GUIDELINES.md](./BRAND-GUIDELINES.md) (both in Spanish).

## License

This repo has no license file, so all rights are reserved on the content. If you want to reuse something, write to [jorgefsb@gmail.com](mailto:jorgefsb@gmail.com).
"""),
    ),
    dict(
        key="jorgesuarez.com.mx", personal=True, media="capture",
        title="JorgeSuarez.com.mx", live="https://jorgesuarez.com.mx",
        kicker=dict(es="NEGOCIOS // SITIO PERSONAL", en="BUSINESS // PERSONAL SITE"),
        promise=dict(es="Más de 20 años haciendo videojuegos, estudios y comunidad, contados en un solo lugar.",
                     en="20+ years building games, studios and community, told in one place."),
        chip=dict(es="V2.0 EN PRODUCCIÓN", en="V2.0 IN PRODUCTION"),
        cta=dict(es="Visitar el sitio", en="Visit the site"),
        about="🎮 Personal site of Jorge Suárez: 20+ years building games, studios and community from Guadalajara, told like a game. · Sitio personal: trayectoria, productos y laboratorio.",
        topics=["personal-site", "video-games", "entrepreneurship", "jorgesuarez"],
        body=dict(es="""## ¿Qué es?

El sitio personal de Jorge Suárez. Reúne su trayectoria, su trabajo en Amber México, sus productos, sus frameworks, su laboratorio y cómo contactarlo. Está en español e inglés.

## ¿Para quién es?

Para quien quiere saber quién es Jorge, qué ha construido y cómo jugar o trabajar con él: gamers, gente que hace videojuegos, emprendedores, prensa y organizadores de eventos.

## ¿Qué dolor resuelve?

Más de 20 años de trabajo estaban repartidos entre redes, notas de prensa, canales y proyectos. Quien llegaba a un pedazo no veía el resto.

## La propuesta

Un solo lugar que cuenta la historia completa y manda a cada proyecto. Está hecho para sentirse como un juego: scroll narrativo, el menú «Juega» para elegir cuánto responde la página, y Moki escondido en los bordes.

## ¿Cómo se usa?

1. Entra a [jorgesuarez.com.mx](https://jorgesuarez.com.mx).
2. Cambia de idioma con ES / EN.
3. Con «Juega» subes o bajas la intensidad. Si tu sistema pide movimiento reducido, la página se queda quieta.

## ¿Cuándo conviene y cuándo no?

Conviene para conocer a Jorge, llegar a sus proyectos o escribirle.

No es el sitio de Amber ni de sus otras empresas: cada una tiene el suyo. Tampoco busques aquí el código fuente del sitio; este repo recibe el build ya armado.

## ¿Dónde lo pruebo?

En vivo: **[jorgesuarez.com.mx](https://jorgesuarez.com.mx)**

{{SCREENS}}

## Hasta dónde llegamos

La versión 2.0 está en producción desde el 12 de octubre de 2026 y se sirve con GitHub Pages detrás de Cloudflare.

El v1 quedó respaldado en el tag `v1-final-2026-10-12` y en la rama `v1-legacy`.

## Para quien construye

- El código fuente del v2 vive en un repo privado. Este repo recibe el build y lo publica.
- Rollback al v1: el deploy del v2 es un solo commit. `git revert` de ese commit y push a `main`.
- Candado de caché: si cambias un CSS o JS que carga `index.html`, súbele su `?v=` en `index.html`. El workflow `version-assets` revisa eso en cada pull request.
- Identidad y voz: [brand-guidelines.md](./brand-guidelines.md) y el [BrandKit](https://brandkit.jorgesuarez.com.mx).

## Licencia

Sin licencia abierta. El contenido, el retrato y la marca conservan todos los derechos.
""", en="""## What is it?

The personal site of Jorge Suárez. It brings together his story, his work at Amber México, his products, his frameworks, his lab and how to reach him. It is available in Spanish and English.

## Who is it for?

For anyone who wants to know who Jorge is, what he has built and how to play or work with him: gamers, people who make games, entrepreneurs, press and event organizers.

## What pain does it solve?

More than 20 years of work were spread across social networks, press clips, channels and projects. People who found one piece did not see the rest.

## The proposal

One place that tells the whole story and sends you to each project. It is built to feel like a game: narrative scroll, the «Juega» menu to choose how much the page responds, and Moki hiding at the edges.

## How do I use it?

1. Go to [jorgesuarez.com.mx](https://jorgesuarez.com.mx).
2. Switch language with ES / EN.
3. Use «Juega» to turn the intensity up or down. If your system asks for reduced motion, the page stays still.

## When it fits and when it doesn't

It fits when you want to get to know Jorge, reach his projects or write to him.

It is not the site of Amber or his other companies: each has its own. Do not look for the site's source code here either; this repo receives the finished build.

## Where can I try it?

Live: **[jorgesuarez.com.mx](https://jorgesuarez.com.mx)**

{{SCREENS}}

## How far we got

Version 2.0 has been in production since 12 October 2026, served with GitHub Pages behind Cloudflare.

The v1 is backed up in the `v1-final-2026-10-12` tag and the `v1-legacy` branch.

## For builders

- The v2 source code lives in a private repo. This repo receives the build and publishes it.
- Rollback to v1: the v2 deploy is a single commit. `git revert` that commit and push to `main`.
- Cache lock: if you change a CSS or JS file loaded by `index.html`, bump its `?v=` in `index.html`. The `version-assets` workflow checks this on every pull request.
- Identity and voice: [brand-guidelines.md](./brand-guidelines.md) and the [BrandKit](https://brandkit.jorgesuarez.com.mx) (both in Spanish).

## License

No open license. All rights are reserved on the content, the portrait and the brand.
"""),
    ),
    dict(
        key="master-prompt-builder", personal=True, media="capture", herdr=True,
        title="Master Prompt Builder", live="https://mpb.jorgesuarez.com.mx",
        kicker=dict(es="IA // HERRAMIENTA WEB", en="AI // WEB TOOL"),
        promise=dict(es="Deja de presentarte en cada chat. Arma tu Master Prompt y tu IA por fin te conoce.",
                     en="Stop introducing yourself in every chat. Build your Master Prompt so your AI knows you."),
        chip=dict(es="EN LÍNEA · GRATIS", en="LIVE · FREE"),
        cta=dict(es="Probar MPB", en="Try MPB"),
        about="🤖 Stop introducing yourself to every AI chat. Build your Master Prompt in 7 steps and export it to ChatGPT, Claude or any AI. · Arma tu Master Prompt y deja de presentarte en cada chat.",
        topics=["ai", "prompt-engineering", "ai-tools", "chatgpt", "claude", "jorgesuarez"],
        body=dict(es="""## ¿Qué es?

Una web app que te guía paso a paso para crear, mantener y exportar tu Master Prompt: el documento que le dice a una IA quién eres, cómo trabajas y cómo te gusta que te respondan.

## ¿Para quién es?

Para cualquiera que usa ChatGPT, Claude u otra IA seguido en su trabajo y ya se cansó de explicarse desde cero.

## ¿Qué dolor resuelve?

Cada vez que abres un chat nuevo, la IA no sabe quién eres. O vuelves a explicar tu rol, tus proyectos y tus reglas, o recibes respuestas genéricas.

## La propuesta

Escribirlo una sola vez. Un wizard de 7 pasos arma el prompt con ejemplos que puedes tocar, y lo exportas para pegarlo donde quieras.

| Paso | Qué captura |
|---|---|
| 1. Identidad | Nombre, rol, empresa |
| 2. Contexto | Industria y responsabilidades |
| 3. Stack | Herramientas y tecnologías |
| 4. Comunicación | Cómo te gusta que te respondan |
| 5. Reglas | Lo que siempre o nunca quieres |
| 6. Proyectos | En qué estás trabajando |
| 7. Revisión | Editas y cierras |

## ¿Cómo se usa?

1. Abre [mpb.jorgesuarez.com.mx](https://mpb.jorgesuarez.com.mx).
2. Elige cómo empezar: de cero, pegando un prompt que ya tengas o con tus memorias de ChatGPT.
3. Completa los pasos y revisa la vista previa.
4. Copia el resultado, descárgalo en Markdown o expórtalo a PDF.
5. Pégalo en las instrucciones de tu IA.

## ¿Cuándo conviene y cuándo no?

Conviene si usas una IA varias veces por semana y quieres respuestas a tu medida desde el primer mensaje.

Todavía no hay cuentas: tu avance se guarda solo en tu navegador, así que no se sincroniza entre dispositivos. Importar desde LinkedIn y sincronizar con GitHub están marcados como próximamente.

## ¿Dónde lo pruebo?

En vivo: **[mpb.jorgesuarez.com.mx](https://mpb.jorgesuarez.com.mx)**

{{SCREENS}}

## Hasta dónde llegamos

Funciona hoy: wizard de 7 pasos, ejemplos clicables, vista previa en tiempo real, exportación a PDF, Markdown y texto, guardado local con versiones.

Pendiente en el roadmap: cuentas, panel de administración, sincronización con GitHub, API pública y app móvil.

## Para quien construye

JavaScript sin framework (ES Modules), CSS con variables y `localStorage`. No hay paso de build.

```bash
git clone https://github.com/jorgefsb/master-prompt-builder.git
cd master-prompt-builder
python3 -m http.server 3000
npm test   # integridad de marca y aislamiento de idioma del wizard
```

| Ruta | Qué hay |
|---|---|
| `index.html` | Punto de entrada |
| `js/app.js`, `js/wizard.js` | Aplicación y pasos del wizard |
| `js/generator.js`, `js/export.js` | Generación y exportación del prompt |
| `js/storage.js` | Guardado local y versiones |
| `css/` | Sistema visual y animaciones |

## Licencia

Este repo no tiene archivo de licencia, así que el código conserva todos los derechos. Úsalo libremente en [mpb.jorgesuarez.com.mx](https://mpb.jorgesuarez.com.mx).
""", en="""## What is it?

A web app that walks you through creating, maintaining and exporting your Master Prompt: the document that tells an AI who you are, how you work and how you like to be answered.

## Who is it for?

For anyone who uses ChatGPT, Claude or another AI often at work and is tired of explaining themselves from scratch.

## What pain does it solve?

Every time you open a new chat, the AI does not know who you are. You either explain your role, your projects and your rules again, or you get generic answers.

## The proposal

Write it once. A 7-step wizard builds the prompt with examples you can click, and you export it to paste wherever you want.

| Step | What it captures |
|---|---|
| 1. Identity | Name, role, company |
| 2. Context | Industry and responsibilities |
| 3. Stack | Tools and technologies |
| 4. Communication | How you like to be answered |
| 5. Rules | What you always or never want |
| 6. Projects | What you are working on |
| 7. Review | Edit and finish |

## How do I use it?

1. Open [mpb.jorgesuarez.com.mx](https://mpb.jorgesuarez.com.mx).
2. Choose how to start: from scratch, by pasting a prompt you already have, or with your ChatGPT memories.
3. Complete the steps and check the live preview.
4. Copy the result, download it as Markdown or export it to PDF.
5. Paste it into your AI's instructions.

## When it fits and when it doesn't

It fits if you use an AI several times a week and want tailored answers from the first message.

There are no accounts yet: your progress is saved only in your browser, so it does not sync across devices. Importing from LinkedIn and syncing with GitHub are marked as coming soon. The interface is in Spanish.

## Where can I try it?

Live: **[mpb.jorgesuarez.com.mx](https://mpb.jorgesuarez.com.mx)**

{{SCREENS}}

## How far we got

Working today: the 7-step wizard, clickable examples, live preview, export to PDF, Markdown and text, and local saving with versions.

Still on the roadmap: accounts, an admin panel, GitHub sync, a public API and a mobile app.

## For builders

Framework-free JavaScript (ES Modules), CSS custom properties and `localStorage`. There is no build step.

```bash
git clone https://github.com/jorgefsb/master-prompt-builder.git
cd master-prompt-builder
python3 -m http.server 3000
npm test   # brand integrity and wizard language isolation
```

| Path | What lives there |
|---|---|
| `index.html` | Entry point |
| `js/app.js`, `js/wizard.js` | App and wizard steps |
| `js/generator.js`, `js/export.js` | Prompt generation and export |
| `js/storage.js` | Local saving and versions |
| `css/` | Visual system and animations |

## License

This repo has no license file, so all rights are reserved on the code. Use it freely at [mpb.jorgesuarez.com.mx](https://mpb.jorgesuarez.com.mx).
"""),
    ),
]

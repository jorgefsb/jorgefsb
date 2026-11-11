REPOS3 = [
    dict(
        key="linkedin-automation-template", personal=True, media="flow", guide="docs/GUIDE.md",
        title="LinkedIn Automation Template", live="./docs/SETUP.md",
        kicker=dict(es="IA // PLANTILLA ABIERTA", en="AI // OPEN TEMPLATE"),
        promise=dict(es="Una infografía entra, cuatro borradores de LinkedIn salen. Tú pones el criterio.",
                     en="One infographic goes in, four LinkedIn drafts come out. You bring the judgment."),
        chip=dict(es="PLANTILLA V1.0 · MIT", en="TEMPLATE V1.0 · MIT"),
        cta=dict(es="Empezar con la guía de 15 minutos", en="Start with the 15-minute guide"),
        about="📝 Open template: turn one infographic into four LinkedIn post drafts with AI, keeping attribution and your own voice. MIT. · Una infografía entra, cuatro borradores de LinkedIn salen.",
        topics=["ai", "automation", "chatgpt", "claude", "content-marketing", "jorgesuarez", "linkedin", "open-source", "productivity", "social-media", "templates"],
        flow=dict(es=["1 INFOGRAFÍA", ["EDUCATIVO", "CON DATOS", "OPINIÓN", "CASO"], "TU EDICIÓN", "LINKEDIN"],
                  en=["1 INFOGRAPHIC", ["EDUCATIONAL", "DATA-DRIVEN", "HOT TAKE", "CASE STUDY"], "YOUR EDIT", "LINKEDIN"]),
        flow_cap=dict(es="Diagrama del flujo. No es una captura: esta plantilla son carpetas, plantillas y prompts, no una app.",
                      en="Flow diagram. This is not a screenshot: the template is folders, templates and prompts, not an app."),
        body=dict(es="""## ¿Qué es?

Una plantilla abierta para convertir una infografía o imagen en cuatro borradores de post para LinkedIn, sin perder el crédito a la fuente ni tu voz.

## ¿Para quién es?

Para profesionales y equipos chicos que publican en LinkedIn, ya usan una IA como Claude o ChatGPT y tienen material visual guardado sin aprovechar.

## ¿Qué dolor resuelve?

Publicar seguido quita tiempo. Y cuando se le encarga a una IA sin sistema, sale contenido genérico, con la misma voz que todos y sin crédito a quien hizo la fuente.

## La propuesta

Un sistema de carpetas, plantillas y prompts. Entra una fuente visual y salen cuatro borradores en formatos distintos, cada uno con sus créditos. La IA acelera el primer borrador; tú pones criterio, experiencia, edición y la conversación con tu comunidad.

| Formato | Plantilla |
|---|---|
| Educativo | [`educational.md`](./02-templates/post-templates/educational.md) |
| Con datos | [`data-driven.md`](./02-templates/post-templates/data-driven.md) |
| Opinión | [`hot-take.md`](./02-templates/post-templates/hot-take.md) |
| Caso | [`case-study.md`](./02-templates/post-templates/case-study.md) |

## ¿Cómo se usa?

1. Clona el repo o usa «Use this template».
2. Pon tus infografías en `01-infographics/` y llena sus créditos con el ejemplo `credits-EXAMPLE.json`.
3. Describe tu voz en `02-templates/brand-adapters/`.
4. Corre el prompt de `06-prompts/batch-generator.md` en tu IA.
5. Edita los borradores y publica tú.

La guía paso a paso está en [docs/SETUP.md](./docs/SETUP.md), en inglés.

## ¿Cuándo conviene y cuándo no?

Conviene si ya tienes infografías, gráficas o láminas y quieres sacarles más provecho con un método repetible.

No publica por ti ni se conecta a LinkedIn: genera borradores que tú revisas. Tampoco promete resultados; este repo no trae métricas verificadas.

## ¿Dónde lo pruebo?

Aquí mismo: **[docs/SETUP.md](./docs/SETUP.md)**. No hay nada que instalar.

## Hasta dónde llegamos

Plantilla 1.0 con cuatro formatos de post, un adaptador de voz, un generador por lotes, un traductor y un sistema de créditos. Última actualización del contenido: 22 de agosto de 2026.

Pendiente: traducir la guía completa al español.

## Para quien construye

No hay código que correr: son archivos Markdown y un JSON de ejemplo. La [guía completa](./docs/GUIDE.md) (en inglés) explica la estructura, la estrategia de publicación y cómo adaptarla a tu nicho. También hay [FAQ](./docs/FAQ.md), [flujos](./docs/WORKFLOWS.md) y [personalización](./docs/CUSTOMIZATION.md).

## Licencia

[MIT](./LICENSE). Úsala, cámbiala y compártela.
""", en="""## What is it?

An open template that turns one infographic or image into four LinkedIn post drafts without losing credit to the source or your own voice.

## Who is it for?

For professionals and small teams who post on LinkedIn, already use an AI like Claude or ChatGPT and have visual material sitting unused.

## What pain does it solve?

Posting often takes time. And when you hand it to an AI with no system, you get generic content in the same voice as everyone else and with no credit to whoever made the source.

## The proposal

A system of folders, templates and prompts. One visual source goes in and four drafts in different formats come out, each with its credits. The AI speeds up the first draft; you bring judgment, experience, editing and the conversation with your community.

| Format | Template |
|---|---|
| Educational | [`educational.md`](./02-templates/post-templates/educational.md) |
| Data-driven | [`data-driven.md`](./02-templates/post-templates/data-driven.md) |
| Hot take | [`hot-take.md`](./02-templates/post-templates/hot-take.md) |
| Case study | [`case-study.md`](./02-templates/post-templates/case-study.md) |

## How do I use it?

1. Clone the repo or click "Use this template".
2. Put your infographics in `01-infographics/` and fill in their credits using `credits-EXAMPLE.json`.
3. Describe your voice in `02-templates/brand-adapters/`.
4. Run the prompt in `06-prompts/batch-generator.md` in your AI.
5. Edit the drafts and publish them yourself.

The step-by-step guide is in [docs/SETUP.md](./docs/SETUP.md).

## When it fits and when it doesn't

It fits if you already have infographics, charts or slides and want to get more out of them with a repeatable method.

It does not post for you or connect to LinkedIn: it produces drafts that you review. It does not promise results either; this repo ships no verified metrics.

## Where can I try it?

Right here: **[docs/SETUP.md](./docs/SETUP.md)**. There is nothing to install.

## How far we got

Template 1.0 with four post formats, a voice adapter, a batch generator, a translator and a credits system. Content last updated on 22 August 2026.

Pending: a full Spanish translation of the guide.

## For builders

There is no code to run: it is Markdown files and one example JSON. The [full guide](./docs/GUIDE.md) explains the structure, the publishing strategy and how to adapt it to your niche. There is also an [FAQ](./docs/FAQ.md), [workflows](./docs/WORKFLOWS.md) and [customization](./docs/CUSTOMIZATION.md).

## License

[MIT](./LICENSE). Use it, change it and share it.
"""),
    ),
    dict(
        key="echomentor-ai", personal=False, media="capture", herdr=True,
        title="EchoMentor AI · landing", live="https://echomentor.uetc.mx", live_en="https://echomentor.uetc.mx/?lang=en",
        owner=dict(es="UETC · Arden A.C.", en="UETC · Arden A.C."),
        tagline=dict(es="Landing pública de EchoMentor AI, la plataforma de aprendizaje adaptativo con IA de UETC · Arden A.C.",
                     en="Public landing page for EchoMentor AI, the adaptive learning platform with AI by UETC · Arden A.C."),
        cta=dict(es="Abrir la landing", en="Open the landing page"),
        about="🎓 Landing page for EchoMentor AI, the adaptive learning platform with AI by UETC · Arden A.C. It behaves like the product: a class already running. · Landing de EchoMentor AI, aprendizaje adaptativo con IA.",
        topics=["edtech", "ai", "adaptive-learning", "landing-page", "uetc"],
        body=dict(es="""## ¿Qué es?

La landing pública de **EchoMentor AI**, la plataforma de aprendizaje adaptativo con IA de **UETC · Arden A.C.** Este repo es solo la landing; el código de la plataforma es privado.

## ¿Para quién es?

Para quien quiere entender qué hace EchoMentor antes de entrar, y para los miembros del [Club UETC](https://club.uetc.mx) que ya tienen código de acceso.

## ¿Qué dolor resuelve?

Explicar con texto una plataforma que adapta la clase a cada persona no alcanza: hay que verla funcionando.

## La propuesta

La página se comporta como el producto: una clase ya corriendo, un temario que se arma solo, un perfil del Aprendiz que reescribe el curso, un pizarrón que se dibuja y actividades que funcionan de verdad. Todo usa datos de ejemplo y la propia página lo marca como demo.

## ¿Cómo se usa?

1. Abre [echomentor.uetc.mx](https://echomentor.uetc.mx) y baja por la página.
2. Cambia de idioma con ES · EN · RO, o entra directo con `?lang=es`, `?lang=en` o `?lang=ro`.
3. Si tienes código de acceso, escríbelo en el formulario y entras a la plataforma.
4. Si no tienes código, únete gratis al [Club UETC](https://club.uetc.mx).

## ¿Cuándo conviene y cuándo no?

Conviene para conocer el producto y para que los miembros entren.

La landing no es la plataforma: lo que ves aquí es una demostración con datos de ejemplo y no prueba la disponibilidad de la app.

## ¿Dónde lo pruebo?

En vivo: **[echomentor.uetc.mx](https://echomentor.uetc.mx)**

{{SCREENS}}

## Hasta dónde llegamos

La landing está publicada en español, inglés y rumano. La plataforma está en beta dentro del Club UETC.

## Para quien construye

Sitio estático servido con GitHub Pages. El formulario de acceso hace un `POST` normal al conector de la plataforma, funciona sin JavaScript y el código nunca viaja en la URL. La landing no tiene backend.

```bash
npx serve .   # o cualquier servidor estático
```

| Archivo | Qué es |
|---|---|
| `index.html` | La página completa: marcado, estilos y lógica de la demo |
| `i18n.js` | Traducciones (es · en · ro) y datos de la demo por idioma |
| `scrollcraft.js` / `scrollcraft.css` | Motor de scroll, sin modificar |
| `assets/` | Símbolo oficial UETC, ícono, fuentes e imagen para compartir |
| `BRIEF.md` | Brief de diseño |
| `FINGERPRINTS.md` | Registro de huellas para que la siguiente landing no sea un calco |

## Marca, licencia y créditos

- Sigue el [brandkit de Arden v2.4](https://brandkit.uetc.mx) como pieza de UETC. No usa la identidad personal de Jorge Suárez.
- Hecha con [scroll-craft](https://github.com/nateherkai/scroll-craft) (MIT, © Nate Herk). Ver `THIRD_PARTY_LICENSE-scrollcraft.txt`.
- Tipografías Montserrat y Rubik (OFL), autoalojadas.
- © 2026 UETC · Arden A.C. Todos los derechos reservados sobre marca y contenido.
""", en="""## What is it?

The public landing page for **EchoMentor AI**, the adaptive learning platform with AI by **UETC · Arden A.C.** This repo is only the landing page; the platform's code is private.

## Who is it for?

For anyone who wants to understand what EchoMentor does before joining, and for [Club UETC](https://club.uetc.mx) members who already have an access code.

## What pain does it solve?

Text alone cannot explain a platform that adapts the class to each person: you have to see it working.

## The proposal

The page behaves like the product: a class already running, a syllabus that builds itself, a Learner profile that rewrites the course, a whiteboard that draws itself and activities that actually work. Everything uses sample data and the page itself labels it as a demo.

## How do I use it?

1. Open [echomentor.uetc.mx](https://echomentor.uetc.mx/?lang=en) and scroll down the page.
2. Switch language with ES · EN · RO, or go straight in with `?lang=es`, `?lang=en` or `?lang=ro`.
3. If you have an access code, type it into the form and you enter the platform.
4. If you do not have a code, join [Club UETC](https://club.uetc.mx) for free.

## When it fits and when it doesn't

It fits for getting to know the product and for members to sign in.

The landing page is not the platform: what you see here is a demonstration with sample data and it does not prove the app's availability.

## Where can I try it?

Live: **[echomentor.uetc.mx](https://echomentor.uetc.mx/?lang=en)**

{{SCREENS}}

## How far we got

The landing page is published in Spanish, English and Romanian. The platform is in beta inside Club UETC.

## For builders

Static site served with GitHub Pages. The access form sends a regular `POST` to the platform's connector, works without JavaScript, and the code never travels in the URL. The landing page has no backend.

```bash
npx serve .   # or any static server
```

| File | What it is |
|---|---|
| `index.html` | The whole page: markup, styles and demo logic |
| `i18n.js` | Translations (es · en · ro) and demo data per language |
| `scrollcraft.js` / `scrollcraft.css` | Scroll engine, unmodified |
| `assets/` | Official UETC symbol, icon, fonts and share image |
| `BRIEF.md` | Design brief (in Spanish) |
| `FINGERPRINTS.md` | Fingerprint log so the next landing page is not a copy of this one |

## Brand, license and credits

- It follows the [Arden brandkit v2.4](https://brandkit.uetc.mx) as a UETC piece. It does not use Jorge Suárez's personal identity.
- Made with [scroll-craft](https://github.com/nateherkai/scroll-craft) (MIT, © Nate Herk). See `THIRD_PARTY_LICENSE-scrollcraft.txt`.
- Montserrat and Rubik typefaces (OFL), self-hosted.
- © 2026 UETC · Arden A.C. All rights reserved on brand and content.
"""),
    ),
    dict(
        key="sparkcrew-landing", personal=False, media="capture",
        title="SparkCrew · landing", live="https://sparkcrew.jorgesuarez.com.mx",
        owner=dict(es="Sparkplug Technologies", en="Sparkplug Technologies"),
        tagline=dict(es="Landing y lista de espera de SparkCrew, un experimento de producto de Sparkplug Technologies.",
                     en="Landing page and waitlist for SparkCrew, a product experiment by Sparkplug Technologies."),
        cta=dict(es="Visitar SparkCrew", en="Visit SparkCrew"),
        about="⚡ Landing page and waitlist for SparkCrew, a Sparkplug Technologies experiment: AI partners with C-suite roles inside Bitrix24 for small businesses. · Landing y lista de espera de SparkCrew.",
        topics=["ai-agents", "landing-page", "bitrix24", "smb"],
        body=dict(es="""## ¿Qué es?

La landing pública y la lista de espera de **SparkCrew**, un experimento de producto de [Sparkplug Technologies](https://getsparkplug.com). Este repo contiene la landing, no el producto.

## ¿Para quién es?

Para dueños y directores de PyMEs que ya trabajan en Bitrix24 y quieren conocer la propuesta.

## ¿Qué dolor resuelve?

Una PyME toma decisiones de estrategia, tecnología, ventas, marketing y finanzas sin tener un equipo directivo completo para cada área.

## La propuesta

Explorar una idea concreta: llevar un equipo de partners de IA, con roles directivos, al espacio de trabajo de la empresa en Bitrix24.

| Rol | Enfoque |
|---|---|
| CEO Partner | Decisiones y dirección estratégica |
| CTO Partner | Arquitectura y estrategia tecnológica |
| CRO Partner | Ventas, oferta y crecimiento de ingresos |
| CMO Partner | Marketing y adquisición |
| CFO Partner | Planeación y claridad financiera |

## ¿Cómo se usa?

1. Abre [sparkcrew.jorgesuarez.com.mx](https://sparkcrew.jorgesuarez.com.mx).
2. Lee la propuesta y conoce los perfiles del crew.
3. Si te interesa, déjanos tus datos en la lista de espera.

## ¿Cuándo conviene y cuándo no?

Conviene para conocer la idea y apuntarte.

Es una propuesta, no un servicio contratado ni una prueba del producto funcionando. La landing está en inglés.

## ¿Dónde lo pruebo?

En vivo: **[sparkcrew.jorgesuarez.com.mx](https://sparkcrew.jorgesuarez.com.mx)**

{{SCREENS}}

## Hasta dónde llegamos

Landing pública con flujo de lista de espera y página de confirmación. El producto no vive en este repo.

## Para quien construye

HTML, CSS y JavaScript sin framework. El formulario usa Formspree.

```bash
git clone https://github.com/jorgefsb/sparkcrew-landing.git
cd sparkcrew-landing
python3 -m http.server 3000
```

| Archivo | Qué es |
|---|---|
| `index.html` | Landing principal |
| `thank-you.html` | Confirmación de la lista de espera |
| `style.css` | Sistema visual y responsive |
| `script.js` | Interacciones y animación |
| `CNAME` | Dominio público |

## Marca y créditos

SparkCrew es un experimento de producto de [Sparkplug Technologies](https://getsparkplug.com) y usa su identidad, no la marca personal de Jorge Suárez.

## Licencia

Este repo no tiene archivo de licencia, así que Sparkplug Technologies conserva todos los derechos sobre el código, el contenido y la marca. Si quieres reutilizar algo, pide permiso primero abriendo un issue.
""", en="""## What is it?

The public landing page and waitlist for **SparkCrew**, a product experiment by [Sparkplug Technologies](https://getsparkplug.com). This repo holds the landing page, not the product.

## Who is it for?

For owners and directors of small businesses who already work in Bitrix24 and want to learn about the proposal.

## What pain does it solve?

A small business makes strategy, technology, sales, marketing and finance decisions without a full leadership team for each area.

## The proposal

Explore one concrete idea: bring a team of AI partners, with leadership roles, into the company's Bitrix24 workspace.

| Role | Focus |
|---|---|
| CEO Partner | Decisions and strategic direction |
| CTO Partner | Architecture and technology strategy |
| CRO Partner | Sales, offer and revenue growth |
| CMO Partner | Marketing and acquisition |
| CFO Partner | Planning and financial clarity |

## How do I use it?

1. Open [sparkcrew.jorgesuarez.com.mx](https://sparkcrew.jorgesuarez.com.mx).
2. Read the proposal and meet the crew profiles.
3. If you are interested, leave your details on the waitlist.

## When it fits and when it doesn't

It fits for learning about the idea and signing up.

It is a proposal, not a contracted service or proof of a working product.

## Where can I try it?

Live: **[sparkcrew.jorgesuarez.com.mx](https://sparkcrew.jorgesuarez.com.mx)**

{{SCREENS}}

## How far we got

A public landing page with a waitlist flow and a confirmation page. The product does not live in this repo.

## For builders

Framework-free HTML, CSS and JavaScript. The form uses Formspree.

```bash
git clone https://github.com/jorgefsb/sparkcrew-landing.git
cd sparkcrew-landing
python3 -m http.server 3000
```

| File | What it is |
|---|---|
| `index.html` | Main landing page |
| `thank-you.html` | Waitlist confirmation |
| `style.css` | Visual system and responsive layout |
| `script.js` | Interactions and animation |
| `CNAME` | Public domain |

## Brand and credits

SparkCrew is a product experiment by [Sparkplug Technologies](https://getsparkplug.com) and uses its identity, not Jorge Suárez's personal brand.

## License

This repo has no license file, so Sparkplug Technologies keeps all rights to the code, the content and the brand. If you want to reuse something, ask first by opening an issue.
"""),
    ),
    dict(
        key="tecnimotostatus-site", personal=False, media="lock",
        title="TecniMoto Status", live="https://status.tecnimoto.mx/",
        owner=dict(es="Tecni Moto Garage", en="Tecni Moto Garage"),
        tagline=dict(es="Página de estatus cifrada para los socios de Tecni Moto.",
                     en="Encrypted status page for Tecni Moto partners."),
        cta=dict(es="Abrir la página", en="Open the page"),
        about="🔒 Encrypted status page for Tecni Moto partners. Opens only with the access password. · Página de estatus cifrada para socios de Tecni Moto.",
        topics=["status-page", "encryption", "cloudflare-workers"],
        body=dict(es="""## ¿Qué es?

Una página de estatus para los socios de Tecni Moto, servida en [status.tecnimoto.mx](https://status.tecnimoto.mx/). El contenido va cifrado y solo abre con la contraseña de acceso.

## ¿Para quién es?

Para los socios de Tecni Moto que tienen la contraseña. Nadie más puede leerla.

## ¿Qué dolor resuelve?

Compartir el estatus del negocio con los socios sin dejarlo en un chat ni exponerlo en una página pública.

## La propuesta

Una sola página, siempre en la misma dirección, con el contenido cifrado con AES-256-GCM. Sin la contraseña no hay cifras.

## ¿Cómo se usa?

1. Abre [status.tecnimoto.mx](https://status.tecnimoto.mx/).
2. Escribe la contraseña.
3. Lee el estatus. La página muestra la fecha de su última actualización.

## ¿Cuándo conviene y cuándo no?

Conviene para consulta de socios. No es un sitio público de la empresa: el sitio del taller es [tecnimoto.mx](https://tecnimoto.mx).

## ¿Dónde lo pruebo?

{{SCREENS}}

## Hasta dónde llegamos

En línea. Este repo solo tiene la página y el Worker que la sirve; el contenido legible no vive aquí.

## Para quien construye

Worker de Cloudflare `tecnimoto-status` (`worker.mjs`, `wrangler.jsonc`). El estilo sigue [brandkit.tecnimoto.mx](https://brandkit.tecnimoto.mx) (`tokens.css`), no la marca personal de Jorge Suárez.

## Licencia

Este repo no tiene archivo de licencia, así que Tecni Moto Garage conserva todos los derechos sobre el código, el contenido y la marca. Si quieres reutilizar algo, pide permiso primero abriendo un issue.
""", en="""## What is it?

A status page for Tecni Moto partners, served at [status.tecnimoto.mx](https://status.tecnimoto.mx/). The content is encrypted and opens only with the access password.

## Who is it for?

For Tecni Moto partners who have the password. Nobody else can read it.

## What pain does it solve?

Sharing the state of the business with partners without leaving it in a chat or exposing it on a public page.

## The proposal

One page, always at the same address, with the content encrypted with AES-256-GCM. Without the password there are no figures.

## How do I use it?

1. Open [status.tecnimoto.mx](https://status.tecnimoto.mx/).
2. Type the password.
3. Read the status. The page shows the date of its last update.

## When it fits and when it doesn't

It fits for partner lookups. It is not the company's public site: the shop's site is [tecnimoto.mx](https://tecnimoto.mx).

## Where can I try it?

{{SCREENS}}

## How far we got

Live. This repo only holds the page and the Worker that serves it; the readable content does not live here.

## For builders

Cloudflare Worker `tecnimoto-status` (`worker.mjs`, `wrangler.jsonc`). The skin follows [brandkit.tecnimoto.mx](https://brandkit.tecnimoto.mx) (`tokens.css`), not Jorge Suárez's personal brand.

## License

This repo has no license file, so Tecni Moto Garage keeps all rights to the code, the content and the brand. If you want to reuse something, ask first by opening an issue.
"""),
    ),
    dict(
        key="ardenstatus-site", personal=False, media="lock",
        title="Arden Status", live="https://ardenstatus.jorgesuarez.com.mx",
        owner=dict(es="Arden", en="Arden"),
        tagline=dict(es="Página de estatus cifrada para patrocinadores de Arden.",
                     en="Encrypted status page for Arden sponsors."),
        cta=dict(es="Abrir la página", en="Open the page"),
        about="🔒 Encrypted status page for Arden sponsors. Opens only with the access password. · Página de estatus cifrada para patrocinadores de Arden.",
        topics=["status-page", "encryption", "static-site"],
        body=dict(es="""## ¿Qué es?

Una página de estatus para patrocinadores de Arden, servida en [ardenstatus.jorgesuarez.com.mx](https://ardenstatus.jorgesuarez.com.mx). El contenido va cifrado y solo abre con la contraseña de acceso.

## ¿Para quién es?

Para los patrocinadores que tienen la contraseña. Nadie más puede leerla.

## ¿Qué dolor resuelve?

Compartir el estatus con los patrocinadores sin dejarlo en un chat ni exponerlo en una página pública.

## La propuesta

Una sola página, siempre en la misma dirección, con el contenido cifrado con AES-256-GCM. Sin la contraseña no hay cifras.

## ¿Cómo se usa?

1. Abre [ardenstatus.jorgesuarez.com.mx](https://ardenstatus.jorgesuarez.com.mx).
2. Escribe la contraseña.
3. Lee el estatus. La página muestra la fecha de su última actualización.

## ¿Cuándo conviene y cuándo no?

Conviene para consulta de patrocinadores. No es el sitio público de Arden.

## ¿Dónde lo pruebo?

{{SCREENS}}

## Hasta dónde llegamos

En línea. Este repo solo tiene la página; el contenido legible no vive aquí.

## Para quien construye

Un `index.html` estático con el contenido cifrado. Usa la identidad de Arden, no la marca personal de Jorge Suárez.

## Licencia

Este repo no tiene archivo de licencia, así que Arden conserva todos los derechos sobre el código, el contenido y la marca. Si quieres reutilizar algo, pide permiso primero abriendo un issue.
""", en="""## What is it?

A status page for Arden sponsors, served at [ardenstatus.jorgesuarez.com.mx](https://ardenstatus.jorgesuarez.com.mx). The content is encrypted and opens only with the access password.

## Who is it for?

For sponsors who have the password. Nobody else can read it.

## What pain does it solve?

Sharing the status with sponsors without leaving it in a chat or exposing it on a public page.

## The proposal

One page, always at the same address, with the content encrypted with AES-256-GCM. Without the password there are no figures.

## How do I use it?

1. Open [ardenstatus.jorgesuarez.com.mx](https://ardenstatus.jorgesuarez.com.mx).
2. Type the password.
3. Read the status. The page shows the date of its last update.

## When it fits and when it doesn't

It fits for sponsor lookups. It is not Arden's public site.

## Where can I try it?

{{SCREENS}}

## How far we got

Live. This repo only holds the page; the readable content does not live here.

## For builders

A static `index.html` with the encrypted content. It uses Arden's identity, not Jorge Suárez's personal brand.

## License

This repo has no license file, so Arden keeps all rights to the code, the content and the brand. If you want to reuse something, ask first by opening an issue.
"""),
    ),
]

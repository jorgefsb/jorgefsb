# Estándar de README y About · README and About standard

[Español](#español) · [English](#english)

---

## Español

Así se documenta cada repositorio público de [jorgefsb](https://github.com/jorgefsb). Sirve para personas y para agentes. Vigente desde el 10 de noviembre de 2026.

### La regla

Todo repo público original tiene tres cosas, siempre juntas:

1. **About** lleno: descripción, sitio y topics.
2. **`README.md` en inglés** y **`README.es.md` en español**, equivalentes, con enlaces visibles para cambiar de idioma.
3. **Imágenes o video reales del producto**, con su pie que dice qué son y de cuándo.

Un repo sin alguna de las tres no está terminado.

### El About

- Una línea en inglés y una en español, separadas por ` · `. Máximo 350 caracteres.
- Dice qué es y para quién. Sin adjetivos que no se puedan probar.
- Un emoji al inicio, uno solo.
- Sitio: la dirección donde se prueba hoy. Si no hay, se deja vacío.
- Topics: de 3 a 6, en minúsculas. Los repos de la marca personal llevan `jorgesuarez`.

### El README: mismas preguntas, mismo orden

| Sección | Qué contesta |
|---|---|
| ¿Qué es? | En dos o tres líneas, sin jerga |
| ¿Para quién es? | A quién le sirve |
| ¿Qué dolor resuelve? | El problema que nos hizo construirlo |
| La propuesta | Cómo lo resolvimos |
| ¿Cómo se usa? | Pasos numerados; la primera acción no es clonar código |
| ¿Cuándo conviene y cuándo no? | Límites dichos de frente |
| ¿Dónde lo pruebo? | Liga en vivo y capturas reales |
| Hasta dónde llegamos | Qué funciona hoy y qué falta |
| Para quien construye | Comandos, estructura y ligas a la guía técnica |
| Licencia | La real del repo; si no hay archivo de licencia, se dice |

### Reglas que no se rompen

- **Solo hechos verificables.** Nada de cifras, testimonios ni funciones que no existan. Lo que está en roadmap se llama roadmap.
- **Medios reales.** Capturas y recorridos del producto en vivo, con fecha. Un diagrama se etiqueta como diagrama. Un banner no sustituye una demostración.
- **El trabajo anterior se conserva.** Si un README técnico se reemplaza, pasa íntegro a `docs/`.
- **Marca.** Los repos de la marca personal usan el [BrandKit](https://brandkit.jorgesuarez.com.mx): Outfit 700, Inter 400, negro, naranja, ámbar y la firma oficial. Moki nunca se espeja.
- **Fronteras.** Los repos de empresas (Arden / UETC, Sparkplug, Tecni Moto) siguen la misma estructura, pero sin banner, firma ni Moki de la marca personal. Conservan su propia identidad y su crédito.
- **Terceros.** Un fork o una copia de trabajo ajeno no se presenta como original. El About dice de quién es.

### Cómo se regenera

```bash
python3 tools/readme-kit/capture.py CAPTURAS            # capturas y recorrido del producto en vivo
python3 tools/readme-kit/mkdocs.py --repos REPOS --captures CAPTURAS \
    --outfit Outfit-Bold.woff2 --inter Inter-Regular.woff2 \
    --signature JorgeSuarez-A-oscuro-bicolor.svg
```

Los textos viven en `tools/readme-kit/data1.py`, `data2.py` y `data3.py`. Cada cambio se hace ahí, en los dos idiomas, y se vuelve a generar. Las fuentes y la firma salen del BrandKit (Maestros 1.0).

Cada publicación sale con rama de respaldo, pull request y verificación en vivo.

---

## English

This is how every public repository of [jorgefsb](https://github.com/jorgefsb) is documented. It is written for people and for agents. In effect since 10 November 2026.

### The rule

Every original public repo has three things, always together:

1. A filled-in **About**: description, website and topics.
2. **`README.md` in English** and **`README.es.md` in Spanish**, equivalent, with visible links to switch language.
3. **Real images or video of the product**, with a caption saying what they are and when they were taken.

A repo missing any of the three is not finished.

### The About

- One line in English and one in Spanish, separated by ` · `. 350 characters at most.
- It says what it is and who it is for. No adjectives that cannot be proven.
- One emoji at the start, only one.
- Website: the address where it can be tried today. If there is none, leave it empty.
- Topics: 3 to 6, lowercase. Personal brand repos carry `jorgesuarez`.

### The README: same questions, same order

| Section | What it answers |
|---|---|
| What is it? | Two or three lines, no jargon |
| Who is it for? | Who benefits |
| What pain does it solve? | The problem that made us build it |
| The proposal | How we solved it |
| How do I use it? | Numbered steps; the first action is not cloning code |
| When it fits and when it doesn't | Limits stated plainly |
| Where can I try it? | Live link and real screenshots |
| How far we got | What works today and what is missing |
| For builders | Commands, structure and links to the technical guide |
| License | The repo's real one; if there is no license file, say so |

### Rules that do not bend

- **Verifiable facts only.** No numbers, testimonials or features that do not exist. Roadmap items are called roadmap.
- **Real media.** Screenshots and walkthroughs of the live product, dated. A diagram is labeled as a diagram. A banner does not replace a demonstration.
- **Earlier work is kept.** When a technical README is replaced, it moves intact into `docs/`.
- **Brand.** Personal brand repos use the [BrandKit](https://brandkit.jorgesuarez.com.mx): Outfit 700, Inter 400, black, orange, amber and the official signature. Moki is never mirrored.
- **Boundaries.** Company repos (Arden / UETC, Sparkplug, Tecni Moto) follow the same structure, without the personal brand's banner, signature or Moki. They keep their own identity and credit.
- **Third parties.** A fork or a copy of someone else's work is not presented as original. The About says whose it is.

### How to regenerate

```bash
python3 tools/readme-kit/capture.py CAPTURES            # screenshots and walkthrough of the live product
python3 tools/readme-kit/mkdocs.py --repos REPOS --captures CAPTURES \
    --outfit Outfit-Bold.woff2 --inter Inter-Regular.woff2 \
    --signature JorgeSuarez-A-oscuro-bicolor.svg
```

The copy lives in `tools/readme-kit/data1.py`, `data2.py` and `data3.py`. Every change is made there, in both languages, and then regenerated. Fonts and signature come from the BrandKit (Masters 1.0).

Every publication ships with a backup branch, a pull request and a live check.

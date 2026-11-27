# Design

## Direction

The site keeps the **Architect's Flight Case** identity: graphite case, off-white trays and rose actions. The metaphor stays visual and never drives the navigation. Navigation follows the content: keynotes, prototypes, speaker.

## Theme

- Graphite and near-black carry most of the page.
- Crisp off-white trays hold the keynotes and the podcast, and the bios on the speaker page.
- Deep rose is the identity and action colour. The headline accent uses the bright rose.
- Safety yellow is reserved for small status signals, such as readiness badges.
- Licensing is quiet metadata.

## Typography

- Display and labels: Barlow Condensed.
- Body: Atkinson Hyperlegible.
- Commands use the system monospace font, only for literal commands.

## Information Architecture

1. Home: headline "Keynotes and prototypes for the agentic enterprise", the latest keynote on a tray with one action and a PDF chip, three selected prototypes, Frontier-podden, courses and programmes with Frontier Consultancy last, and a speaker band.
2. `/talks/` (talks repository): every talk with Open the deck and Download PDF, grouped deliveries for repeated talks, and a language filter.
3. `/prototypes/`: Azure prototypes, Copilot skills and event kits, with readiness badges, filters and foldouts.
4. `/speaker/`: bios in English and Swedish with copy buttons and word counts, three headshots with downloads, talk topics, experience, facts and an invitation block.
5. `/links/`: a link-in-bio page.

## Components

- Header with the name plate, three page links, and GitHub and Spotify icons.
- Feature keynote with the real title slide.
- Prototype cards with an SVG architecture preview or a real screenshot, readiness badge, stack chips, foldout and actions.
- A numbered three-step strip, used once per page because it is a real sequence.
- Programme rows, podcast tile, bio cards, experience list and catalogue filters with live counts.

## Motion

The home hero rises once on load. Reduced-motion users get the complete layout immediately. Hover movement is limited to small button lifts.

## Imagery

Use real title slides, real screenshots and Johan's own photos. Architecture previews are drawn in SVG. No generated people, stock photography or decorative AI imagery.

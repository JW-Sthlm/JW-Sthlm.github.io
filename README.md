# Johan Wallquist: keynotes and prototypes

Source for [jw-sthlm.github.io](https://jw-sthlm.github.io/): keynotes and prototypes for the agentic enterprise, the Frontier-podden podcast and a speaker page for event organisers.

## Pages

| Path | Source | Job |
|---|---|---|
| `/` | `index.html` | Latest keynote, selected prototypes, Frontier-podden, courses and programmes |
| `/talks/` | [JW-Sthlm/talks](https://github.com/JW-Sthlm/talks) | Every talk with the interactive deck and the PDF |
| `/prototypes/` | `prototypes/index.html` | Selected prototypes with repository links and readiness badges |
| `/speaker/` | `speaker/index.html` | Bios in English and Swedish, headshots, talk topics, experience and contact |
| `/links/` | `links/index.html` | Self-hosted link page for social profiles |

Shared styles and behaviour are in `assets/site.css` and `assets/site.js`. The keynotes page in the talks repository loads the same files from `/assets/`.

The site calls published builds **prototypes**. A prototype is listed only when its repository is public, licensed and passes the weekly audit.

## Badges on the prototypes page

- **Template and deploy guide:** a GitHub template with deploy steps in the README.
- **Live:** a public URL that works without sign-in.
- **Runs in Copilot:** a skill or plugin installed in the visitor's own Copilot.

## Local preview

```powershell
python -m http.server 8080
```

Open `http://localhost:8080`. Keynote thumbnails come from `/talks/`, so they only load on the live domain or when a local server also maps the talks repository.

## Publishing

GitHub Pages serves the repository root from the `main` branch.

## Disclaimer

These are personal projects and community assets. They are not Microsoft products.

See [PUBLIC-RELEASE-CHECKLIST.md](PUBLIC-RELEASE-CHECKLIST.md) for the publishing and reuse review applied to featured repositories, and for the projects that are held back.

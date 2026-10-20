# Certification Learning Guides

Lightweight static site for GitHub Pages — **one markdown file per cert**, shared UI, fetch-on-demand (no giant `content.js`).

| Guide | Page | Source |
| --- | --- | --- |
| AWS AI Practitioner (AIF-C01) | `/` | `guides/aif-c01.md` |
| AWS Cloud Practitioner (CLF-C02) | `/clf/` | `guides/clf-c02.md` |
| Claude Certified Architect – Foundations | `/cca/` | `guides/cca-foundations.md` |

## How loading works

1. Each HTML shell loads small `app.js` + `styles.css`.
2. `app.js` fetches **only that cert’s** `.md` (browser-cached).
3. Marked + DOMPurify render it.

## Repo layout

```
index.html / clf/ / cca/   page shells + cert switcher
app.js · styles.css        shared UI
guides/*.md                edit these
images/                    AIF diagrams
scripts/                   optional AIF import/enrich helpers
```

## Run locally

```sh
python -m http.server 8000
```

Open `/`, `/clf/`, or `/cca/` (needs a local server — not `file://`).

## Edit a guide

1. Change the matching file under `guides/`.
2. Bump `?v=` in that page’s HTML if caches stick.
3. Commit and push.

## Publish

https://divyanshudhiman.github.io/aws_learning/  
https://divyanshudhiman.github.io/aws_learning/clf/  
https://divyanshudhiman.github.io/aws_learning/cca/

## Notes

- AIF content: MIT study-note sources — see `THIRD_PARTY_NOTICES.md`.
- CLF + CCA Foundations guides: original unofficial study notes (not exam dumps).
- CCA eligibility is often partner-network limited — confirm with Anthropic before registering.

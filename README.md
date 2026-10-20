# AWS Certification Learning Guides

Lightweight static site for GitHub Pages — **two markdown guides**, shared UI, no giant `content.js` embed.

| Guide | Page | Source |
| --- | --- | --- |
| AI Practitioner (AIF-C01) | `/` | `guides/aif-c01.md` |
| Cloud Practitioner (CLF-C02) | `/clf/` | `guides/clf-c02.md` |

## How loading works

1. `index.html` / `clf/index.html` load small `app.js` + `styles.css`.
2. `app.js` **fetches only the active guide’s `.md`** (browser-cached).
3. Marked + DOMPurify render it in the page.

That avoids parsing a ~600KB JavaScript string on every visit and keeps **one source file per cert**.

## Repo layout

```
index.html          AIF-C01 shell
clf/index.html      CLF-C02 shell
app.js              Nav, search, fetch+render
styles.css          Shared theme
guides/aif-c01.md   AIF study guide (edit here)
guides/clf-c02.md   CLF study guide (edit here)
images/             AIF diagrams
scripts/            Optional import/enrich helpers
```

## Run locally

```sh
python -m http.server 8000
```

Open `http://localhost:8000` or `http://localhost:8000/clf/`  
(Fetching markdown needs a local server — don’t open as `file://`.)

## Edit a guide

1. Change `guides/aif-c01.md` or `guides/clf-c02.md`.
2. Bump `?v=slim1` in the HTML if browsers cache an old copy.
3. Commit and push.

Optional AIF upstream refresh (MIT sources):

```sh
python scripts/import-kananinirav-aif.py
python scripts/enrich-guide.py
```

## Publish

Repo: [divyanshudhiman/aws_learning](https://github.com/divyanshudhiman/aws_learning)  
Pages: branch `main`, folder `/ (root)`  
Live: https://divyanshudhiman.github.io/aws_learning/

## Attribution

AIF content primarily from MIT-licensed study notes — see `THIRD_PARTY_NOTICES.md`.  
CLF guide is original study notes (not exam dumps).

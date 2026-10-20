# AWS Certification Learning Guides

Static JavaScript site for GitHub Pages with two companion study guides:

| Guide | URL path | Exam |
| --- | --- | --- |
| AI Practitioner | [`/`](https://divyanshudhiman.github.io/aws_learning/) | AIF-C01 |
| Cloud Practitioner | [`/clf/`](https://divyanshudhiman.github.io/aws_learning/clf/) | CLF-C02 |

Same layout for both: essential definitions → domain Parts → glossary → scenario practice with expandable answers.

## AIF-C01 sources

Primarily adapted from [kananinirav/aws-certified-ai-practitioner-study-notes](https://github.com/kananinirav/aws-certified-ai-practitioner-study-notes) (MIT), with earlier material from [jwalsh/aif-c01](https://github.com/jwalsh/aif-c01) (MIT). See `THIRD_PARTY_NOTICES.md`.

Refresh AIF from upstream:

```sh
python scripts/import-kananinirav-aif.py
python scripts/enrich-guide.py
node scripts/embed-guides.js
```

## CLF-C02 sources

Original study notes under `guides/clf-c02/` (Parts 0–7), assembled into `guides/CLF-C02 Study Guide.md` and `clf/content.js`. Not copied from exam dumps.

## Files

| Path | Role |
| --- | --- |
| `index.html` | AIF-C01 page shell |
| `clf/index.html` | CLF-C02 page shell |
| `styles.css` / `app.js` | Shared UI |
| `content.js` | Embedded AIF guide |
| `clf/content.js` | Embedded CLF guide |
| `scripts/embed-guides.js` | Rebuild both `content.js` files |
| `.nojekyll` | Disable Jekyll on Pages |

## Run locally

```sh
python -m http.server 8000
```

Open `http://localhost:8000` (AIF) or `http://localhost:8000/clf/` (CLF).

## Publish on GitHub Pages

Repo: [divyanshudhiman/aws_learning](https://github.com/divyanshudhiman/aws_learning)

1. Push to `main`.
2. **Settings → Pages** → Deploy from branch `main` / `(root)`.
3. Live: `https://divyanshudhiman.github.io/aws_learning/`

## Updating guides

**AIF:** edit `Comprehensive Scenario-Based Practice Question Bank.md`, then:

```sh
node scripts/embed-guides.js
```

**CLF:** edit files in `guides/clf-c02/`, then:

```sh
node scripts/embed-guides.js
```

Commit and push. Hard-refresh the live site after deploy.

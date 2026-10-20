# AWS AI Learning Guide

Static JavaScript site for AWS Certified AI Practitioner (AIF-C01) study notes. No build step, no server — works on GitHub Pages.

## Files

| File | Role |
|------|------|
| `index.html` | Page shell |
| `styles.css` | Layout and theme |
| `app.js` | Navigation, search, progress |
| `content.js` | Embedded study guide (generated from the Markdown source) |
| `.nojekyll` | Tells GitHub Pages not to run Jekyll |

## Run locally

```sh
python -m http.server 8000
```

Open `http://localhost:8000`.

## Publish on GitHub Pages

Repo: [divyanshudhiman/aws_learning](https://github.com/divyanshudhiman/aws_learning)

1. Push these files to the `main` branch.
2. In GitHub: **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Branch: `main`, folder: `/ (root)` → Save.
5. Site URL: `https://divyanshudhiman.github.io/aws_learning/`

Optional: keep **GitHub Actions** as the source if you prefer the workflow in `.github/workflows/pages.yml`.

## Updating the guide

1. Edit `Comprehensive Scenario-Based Practice Question Bank.md`.
2. Regenerate the embedded content:

```sh
node scripts/embed-guide.js
```

3. Commit and push. The live site updates after Pages rebuilds.

The Markdown renderer and sanitizer load from jsDelivr, so readers need internet access for those two scripts.

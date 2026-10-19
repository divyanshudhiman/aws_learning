# AWS AI Learning Guide

A mobile-friendly learning website for the AWS Certified AI Practitioner (AIF-C01) study guide.

## Run locally

The site is static and needs no build step. Serve this folder over HTTP so the browser can fetch the Markdown file. For example, with Python installed:

```sh
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Publish with GitHub Pages

The workflow in `.github/workflows/pages.yml` publishes the site whenever changes are pushed to `main`.

1. Push the contents of this project to the `main` branch of `divyanshudhiman/aws_learning`.
2. In the repository, open **Settings → Pages** and select **GitHub Actions** as the build and deployment source.
3. Wait for the **Publish learning site to GitHub Pages** workflow to finish. GitHub will show the published URL in the Pages settings and deployment.

The source study guide remains `Comprehensive Scenario-Based Practice Question Bank.md`. The website loads and renders that file directly, so edits to the guide appear on the site without copying the content elsewhere.

The Markdown renderer and HTML sanitizer are loaded from jsDelivr; readers need an internet connection to load the guide.

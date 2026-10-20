#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir);
  }
}

function writeContent(targetRel, markdown) {
  const target = path.join(root, targetRel);
  ensureDir(path.dirname(target));
  fs.writeFileSync(target, `window.GUIDE_MARKDOWN = ${JSON.stringify(markdown)};\n`);
  console.log(`Wrote ${targetRel} (${Buffer.byteLength(markdown)} source bytes).`);
}

function concatDir(dir, files) {
  return files
    .map((name) => fs.readFileSync(path.join(dir, name), "utf8").trim())
    .join("\n\n---\n\n") + "\n";
}

// AIF-C01 (existing combined markdown)
const aifSource = path.join(root, "Comprehensive Scenario-Based Practice Question Bank.md");
writeContent("content.js", fs.readFileSync(aifSource, "utf8"));

// CLF-C02 (assembled from parts)
const clfDir = path.join(root, "guides", "clf-c02");
const clfMarkdown = concatDir(clfDir, [
  "00-front-and-definitions.md",
  "01-exam-and-cloud-concepts.md",
  "02-security.md",
  "03-technology.md",
  "04-billing-glossary.md",
  "05-practice.md",
]);
const clfCombined = path.join(root, "guides", "CLF-C02 Study Guide.md");
fs.writeFileSync(clfCombined, clfMarkdown);
writeContent("clf/content.js", clfMarkdown);
console.log(`Also wrote guides/CLF-C02 Study Guide.md`);

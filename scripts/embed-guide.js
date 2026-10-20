#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const source = path.join(root, "Comprehensive Scenario-Based Practice Question Bank.md");
const target = path.join(root, "content.js");

const markdown = fs.readFileSync(source, "utf8");
fs.writeFileSync(target, `window.GUIDE_MARKDOWN = ${JSON.stringify(markdown)};\n`);
console.log(`Wrote ${path.basename(target)} (${Buffer.byteLength(markdown)} source bytes).`);

# 🕵️‍♂️ SEO Cloaking Detector (v1.0.0)

> A Python tool to detect websites performing SEO cloaking using **User-Agent** and **IP-based techniques** — built for ethical hackers, red teamers, and cybersecurity researchers.

---

## 🚀 What is SEO Cloaking?

SEO cloaking is a **black-hat technique** where a website shows different content to search engine bots than to regular users, to manipulate search rankings.

This tool helps detect such deception by comparing what a **Googlebot sees** versus what a **real user sees**.

---

## 🔧 Features

- 🧠 Simulates requests from both **Googlebot** and **normal browsers**
- 📄 Strips non-visible content (JS, CSS, meta, etc.)
- 📊 Calculates text similarity using `difflib.SequenceMatcher`
- 🔍 Flags possible cloaking if similarity falls below threshold
- 🔁 Multiple request samples to reduce false positives

---

## 📦 Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`

Install with:

```bash
pip install -r requirements.txt

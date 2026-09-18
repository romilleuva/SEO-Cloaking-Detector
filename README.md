<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:FF0000,100:0D0D0D&height=210&section=header&text=SEO%20CLOAKING%20DETECTOR&fontSize=42&fontColor=FF1A1A&animation=twinkling&fontAlignY=38&desc=Bot%20vs%20Human%20%E2%80%94%20Trust%20Nothing&descAlignY=58&descSize=16&descColor=FFFFFF" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=22&duration=2600&pause=700&color=FF0000&center=true&vCenter=true&width=680&lines=%3E+scanning+target...;Comparing+Googlebot+vs+Human+response;Calculating+similarity+score...;%E2%9A%A0%EF%B8%8F+Cloaking+behavior+flagged;%E2%9C%85+No+deception+detected" alt="Typing SVG" />

<br>

![Python](https://img.shields.io/badge/Python-3.8+-0D0D0D?style=for-the-badge&logo=python&logoColor=FF0000)
![Version](https://img.shields.io/badge/version-1.0.0-0D0D0D?style=for-the-badge&logoColor=FF0000)
![License](https://img.shields.io/badge/license-MIT-0D0D0D?style=for-the-badge&logoColor=FF0000)
![Status](https://img.shields.io/badge/status-active-0D0D0D?style=for-the-badge&logoColor=FF0000)

![Stars](https://img.shields.io/github/stars/romilleuva/SEO-Cloaking-Detector?style=for-the-badge&color=FF0000&labelColor=0D0D0D)
![Forks](https://img.shields.io/github/forks/romilleuva/SEO-Cloaking-Detector?style=for-the-badge&color=FF0000&labelColor=0D0D0D)
![Last Commit](https://img.shields.io/github/last-commit/romilleuva/SEO-Cloaking-Detector?style=for-the-badge&color=FF0000&labelColor=0D0D0D)

</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## 🕵️ &nbsp;WHAT IS SEO CLOAKING?

**SEO cloaking** is a black-hat technique where a website serves **different content to search engine bots than to real human visitors** — usually to manipulate search rankings while hiding the manipulation from anyone actually browsing the page.

**SEO Cloaking Detector** exposes that deception. It requests the same URL twice — once posing as a normal browser, once posing as **Googlebot** — strips away everything that isn't visible content (scripts, styles, meta tags), and measures how similar the two versions really are. A low similarity score means the site is showing bots and humans two different realities.

> Built for ethical hackers, red teamers, and cybersecurity researchers auditing sites for black-hat SEO manipulation.

<br>

## ⚡ &nbsp;HOW IT WORKS

```mermaid
flowchart TD
    A([Target URL]) --> B[Fetch x5 as Normal Browser]
    A --> C[Fetch x5 as Googlebot]
    B --> D[Strip script / style / meta / noscript]
    C --> D
    D --> E[difflib.SequenceMatcher\nsimilarity scoring]
    E --> F{Avg. similarity\n< 0.85 ?}
    F -->|Yes| G["⚠️ Possible SEO Cloaking Detected"]
    F -->|No| H["✅ No Cloaking Detected"]

    style A fill:#0D0D0D,color:#fff,stroke:#FF0000
    style F fill:#111,color:#fff,stroke:#FF0000
    style G fill:#FF0000,color:#000
    style H fill:#0D0D0D,color:#0f0,stroke:#0f0
```

<br>

## 🔧 &nbsp;FEATURES

<div align="center">

| | |
|---|---|
| 🧠 | Simulates requests from both **Googlebot** and a **normal browser** |
| 📄 | Strips non-visible content (`<script>`, `<style>`, `<meta>`, `<noscript>`) before comparing |
| 📊 | Scores text similarity with Python's `difflib.SequenceMatcher` |
| 🔍 | Flags possible cloaking when similarity drops below the `0.85` threshold |
| 🔁 | Pulls **5 samples per user-agent** to smooth out false positives from dynamic content |

</div>

<br>

## 📦 &nbsp;INSTALLATION

```bash
# Clone the repo
git clone https://github.com/romilleuva/SEO-Cloaking-Detector.git
cd SEO-Cloaking-Detector

# (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Requirements:** Python 3.8+ · `requests` · `beautifulsoup4`

<br>

## 🚀 &nbsp;USAGE

```bash
python Checker.py
```

You'll be prompted for a target URL:

```
Enter the URL you want to check for cloaking: https://example.com
🔍 Scanning https://example.com for SEO cloaking...
📊 Similarity score: 0.42
⚠️ Possible SEO Cloaking Detected!
```

A clean result looks like this instead:

```
🔍 Scanning https://example.com for SEO cloaking...
📊 Similarity score: 0.97
✅ No cloaking detected.
```

<br>

## 🧬 &nbsp;UNDER THE HOOD

```python
NORMAL_USER_AGENT  = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
GOOGLEBOT_USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

# 1. Fetch 5x with each user-agent
# 2. Strip script/style/meta/noscript, extract visible text
# 3. Cross-compare every (user, bot) text pair with SequenceMatcher
# 4. Average the scores → similarity_score
# 5. similarity_score < 0.85  →  cloaking flagged
```

<br>

## ⚠️ &nbsp;RESPONSIBLE USE

This tool sends repeated automated requests to whatever URL you target (5 requests per user-agent, 10 total per scan). Use it only on:

- Sites you **own**, or
- Sites you have **explicit permission** to test

Respect `robots.txt`, rate limits, and each site's terms of service. This project is for **educational and authorized security-research use only** — the author is not responsible for misuse.

<br>

## 🗺️ &nbsp;ROADMAP

- [ ] Support for additional bot user-agents (Bingbot, Yandex, etc.)
- [ ] Configurable similarity threshold via CLI flag
- [ ] Batch scanning from a URL list / CSV
- [ ] JSON/HTML report export
- [ ] Async requests for faster multi-sample scans

<br>

## 🤝 &nbsp;CONTRIBUTING

Contributions, issues, and feature requests are welcome.

1. Fork the repo
2. Create your branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<br>

## 📄 &nbsp;LICENSE

Distributed under the MIT License.

---

<div align="center">

Built by **[Romil Leuva](https://github.com/romilleuva)** 🔴

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:FF0000,100:0D0D0D&height=110&section=footer"/>

</div>

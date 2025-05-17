# SauceDemo – Playwright + Pytest Automation

Tiny demo project that automates the public site <https://www.saucedemo.com/>  
using **Python 3, Playwright, Pytest** and Page‑Object‑Model (POM).

---

## ⚡ Quick start

```bash
# 1) install dependencies
pip install -r requirements.txt

# 2) download browsers once
playwright install

# 3) run all tests in parallel + HTML report
pytest -n auto --html=report.html

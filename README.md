# 🧪 SauceDemo – Playwright + Pytest Automation

This is a test automation project that uses **Python**, **Playwright**, and **Pytest** to automate the e-commerce demo site [SauceDemo](https://www.saucedemo.com/). The goal is to demonstrate modern QA practices using the Page Object Model (POM).
---

## 🚀 Features Covered

✅ Login (valid & invalid credentials)  
✅ Product listing interaction  
✅ Add to cart  
✅ Checkout and order completion  
✅ Assertions to verify success/failure  
✅ HTML test report generation
---

## 📁 Project Structure

Pages/
    login_page.py          # POM – login screen
    product_page.py        # POM – add / remove items
    checkout_page.py       # POM – checkout flow
Tests/
    test_login.py
    test_cart.py
    test_checkout.py
conftest.py                # fixtures: credentials, product list
pytest.ini                 # common Pytest opts
requirements.txt
README.md
---


## 🧰 Tech Stack

- Python 3.x  
- Playwright  
- Pytest  
- Page Object Model (POM)  
- pytest-html (for reports)

---

## ⚙️ Getting Started

To install and run this test suite locally:

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Install Playwright browsers (one-time setup)
playwright install

# Step 3: Run all tests and generate HTML report
pytest -n auto --html=report.html

---
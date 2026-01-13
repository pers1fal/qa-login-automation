# QA Login Automation Project

This project demonstrates UI test automation for a login functionality using **Python, Selenium, Pytest**, and the **Page Object Model (POM)** design pattern.

## 🔍 Project Overview

The purpose of this project is to showcase:
- UI test automation skills
- Proper test structure and architecture
- Usage of Page Object Model (POM)
- Working with Pytest fixtures
- Git & GitHub workflow

The tests are written for the demo login page:  
https://practicetestautomation.com/practice-test-login/

---

## 🧪 Test Scenarios Covered

- ✅ Successful login with valid credentials
- ❌ Login attempt with invalid password

---

## 🏗 Project Structure

```text
qa-login-automation/
│
├── app/
│ └── init.py
│
├── tests/
│ ├── ui/
│ │ ├── pages/
│ │ │ ├── login_page.py # Page Object for Login page
│ │ │ └── init.py
│ │ ├── test_login_ui.py # UI tests for login
│ │ ├── conftest.py # Pytest fixtures (WebDriver setup)
│ │ └── init.py
│ └── init.py
│
├── .gitignore
├── README.md
└── requirements.txt

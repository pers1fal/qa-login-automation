# QA Login Automation Project

UI test automation project for login functionality using **Python, Selenium, Pytest**, and the **Page Object Model (POM)** design pattern.  
The project also includes **GitHub Actions CI** for automated test execution on every push.

---

##  Project Overview

This project demonstrates practical skills in **UI test automation** and **test framework design**, including:

- UI automation with Selenium WebDriver
- Test execution with Pytest
- Page Object Model (POM) architecture
- Pytest fixtures and test configuration
- GitHub Actions CI for automated test runs
- Debugging and fixing CI pipeline issues

Tests are written for the demo login page:  
 https://practicetestautomation.com/practice-test-login/

---

##  Test Scenarios Covered

-  Successful login with valid credentials
-  Login attempt with invalid password

---

##  Project Structure

```text
qa-login-automation/
│
├── app/
│   └── __init__.py
│
├── tests/
│   ├── ui/
│   │   ├── pages/
│   │   │   ├── login_page.py     # Page Object for Login page
│   │   │   └── __init__.py
│   │   ├── test_login_ui.py      # UI tests for login
│   │   ├── conftest.py           # Pytest fixtures (WebDriver setup)
│   │   └── __init__.py
│   └── __init__.py
│
├── .github/
│   └── workflows/
│       └── ui-tests.yml          # GitHub Actions CI workflow
│
├── .gitignore
├── README.md
└── requirements.txt
```


##  Technologies Used

- **Python 3.10+**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Git & GitHub**
- **GitHub Actions (CI)**

---

## 🧪 CI Status
CI status confirms that the tests are stable and runnable in an isolated environment.

---

##  Getting Started

###  Clone the repository

```bash
git clone https://github.com/pers1fal/qa-login-automation.git
```

```bash
cd qa-login-automation
```

---

###  Create a virtual environment

```bash
python -m venv venv
```

---

###  Activate the virtual environment

#### Windows
```bash
venv\Scripts\activate
```

#### macOS / Linux
```bash
source venv/bin/activate
```

---

###  Install dependencies

```bash
pip install -r requirements.txt
```

---

###  Run tests

```bash
pytest -v
```

---

##  Why this is important

The CI pipeline (GitHub Actions) automatically runs all tests on every push, ensuring:
- test stability
- environment independence
- continuous validation of the test framework

This setup reflects a real-world QA Automation workflow.


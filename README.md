# Conference Room Automation - SQA Engineer Guide

Welcome to the **Conference Room Booking Application (CRBA)** automation project. This guide is specifically designed for SQA Engineers to set up, execute, and analyze automated tests.

## 📌 One-Minute Overview

- **Application Under Test**: [https://muntasir101.github.io/CRBA/](https://muntasir101.github.io/CRBA/)
- **Framework**: Python + Selenium + Pytest + Page Object Model (POM)
- **Reporting**: Pytest-HTML & Console Logs
- **CI/CD Ready**: Yes (Headless mode supported)

---

## 🚀 Quick Start (Setup)

Follow these steps to get the automation running on your local machine.

### Prerequisites
- **Python 3.8+** installed ([Verify](https://python.org/downloads): `python --version`)
- **Chrome Browser** installed

### Installation

1.  **Open Terminal** in the project root:
    ```bash
    cd "Conference-room-Automation"
    ```

2.  **Create Virtual Environment** (Recommended):
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *This installs Selenium, Pytest, and reporting tools automatically.*

---

## 🧪 Running Tests

### 1. Smoke Test (Sanity Check)
Run this first to ensure the environment is stable.
```bash
pytest tests/test_smoke.py -v
```

### 2. Run All Tests
Execute the full regression suite.
```bash
pytest
```

### 3. Generate HTML Report (SQA Essential)
Run tests and generate a detailed HTML report (contains pass/fail status and logs).
```bash
pytest --html=reports/report.html --self-contained-html
```
*Open `reports/report.html` in your browser to view the results.*

### 4. Run Specific Features (Epics)
Target specific functionality using markers or file paths.

| Feature | Command |
| :--- | :--- |
| **Room Management** (Epic 1) | `pytest tests/test_epic1_room_management.py` |
| **User Management** (Epic 2) | `pytest tests/test_epic2_user_management.py` |
| **Filtering** (Epic 5) | `pytest tests/test_epic5_filtering.py` |
| **By Tag/Marker** | `pytest -m epic1` |

---

## 📂 Project Structure

A quick map of the codebase for review.

```text
Conference-room-Automation/
├── tests/
│   ├── pages/                 # Page Objects (UI Wrappers)
│   │   ├── login_page.py      # Login Modal Logic
│   │   ├── rooms_page.py      # Rooms List Logic
│   │   └── base_page.py       # Common Actions (Click, Type, Wait)
│   ├── utils/                 # Helpers
│   │   └── test_data.py       # Centralized Data (Users, Inputs)
│   ├── test_smoke.py          # Quick Sanity Tests
│   └── test_*.py              # Feature Tests (Regression)
├── reports/                   # HTML Test Reports (Generated)
├── screenshots/               # Failure Screenshots (Generated)
├── config.py                  # Global Config (URL, Timeouts)
├── locators.json              # Element Selectors (ID, CSS, XPATH)
└── requirements.txt           # Dependency List
```

---

## ⚙️ Configuration

You can adjust settings in `config.py` runs without changing code.

- **Change URL**: Update `BASE_URL` in `config.py`.
- **Headless Mode** (No UI):
    - **Windows**: `set HEADLESS=true` then run pytest
    - **Mac/Linux**: `export HEADLESS=true` then run pytest
- **Browser**: Default is Chrome. Update `BROWSER` env var to change.

---

## 🐛 Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **Driver Error** | The framework manages drivers automatically. Ensure Chrome is installed. |
| **ModuleNotFoundError** | Ensure venv is active and you ran `pip install -r requirements.txt`. |
| **Tests Fail Immediately** | Check internet connection and if `https://muntasir101.github.io/CRBA/` is accessible. |
| **Timeout/Element Not Found** | The app might be slow. Check screenshots in `screenshots/` folder. |

---

**Need specific details?**
- See `FRAMEWORK_SUMMARY.md` for architectural deep-dives.
- See `LOCATOR_REVIEW.md` for element selector audit.

# Setup and Run Tests - Step by Step Guide

## Prerequisites Check

Before running tests, ensure you have:

1. ✅ Python 3.8 or higher installed
2. ✅ Chrome browser installed
3. ✅ pip package manager

## Step 1: Verify Python Installation

Open a terminal/command prompt and check:

```bash
python --version
# OR
python3 --version
```

If Python is not found:
- **Windows**: Download from [python.org](https://www.python.org/downloads/) or install from Microsoft Store
- **Linux/Mac**: Usually pre-installed, or install via package manager

## Step 2: Navigate to Project Directory

```bash
# Windows
cd "Desktop\5th-10th class\Conferenceroom\CRBA-master\CRBA-master"

# Linux/Mac
cd ~/Desktop/5th-10th\ class/Conferenceroom/CRBA-master/CRBA-master
```

## Step 3: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- selenium==4.15.2
- pytest==7.4.3
- pytest-html==4.1.1
- webdriver-manager==4.0.1
- And other dependencies

## Step 5: Run Tests

### Option A: Run Smoke Tests (Quick Validation)
```bash
pytest tests/test_smoke.py -v
```

### Option B: Run All Tests
```bash
pytest
```

### Option C: Run with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Option D: Run Specific Test Suite
```bash
# Epic 1 - Room Management
pytest tests/test_epic1_room_management.py -v

# Epic 2 - User Management
pytest tests/test_epic2_user_management.py -v

# Epic 5 - Filtering
pytest tests/test_epic5_filtering.py -v
```

## Step 6: View Test Results

After tests complete:

1. **Console Output**: Results displayed in terminal
2. **HTML Report**: Open `reports/report.html` in browser
3. **Screenshots**: Check `screenshots/` folder for failed test screenshots

## Quick Commands Reference

```bash
# Install dependencies
pip install -r requirements.txt

# Run smoke tests
pytest tests/test_smoke.py -v

# Run all tests
pytest

# Run with report
pytest --html=reports/report.html

# Run in headless mode
set HEADLESS=true  # Windows
export HEADLESS=true  # Linux/Mac
pytest

# Run specific test
pytest tests/test_epic1_room_management.py::TestFR11RoomListDisplay::test_display_active_rooms -v
```

## Troubleshooting

### Python Not Found
- Install Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation
- Restart terminal after installation

### pip Not Found
```bash
python -m ensurepip --upgrade
```

### ChromeDriver Issues
The framework uses `webdriver-manager` which automatically downloads ChromeDriver.
- Ensure Chrome browser is installed
- Check internet connection for first run

### Module Not Found Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Tests Fail to Connect
- Verify URL is accessible: https://muntasir101.github.io/CRBA/
- Check internet connection
- Verify firewall settings

## Expected Test Results

### Smoke Tests (5 tests)
- ✅ test_application_loads
- ✅ test_dashboard_displayed
- ✅ test_rooms_section_accessible
- ✅ test_login_modal_opens
- ✅ test_register_modal_opens

### Full Test Suite
- Epic 1: 15+ tests
- Epic 2: 10+ tests
- Epic 5: 4 tests

## Test URL

All tests run against: **https://muntasir101.github.io/CRBA/**

## Next Steps After Setup

1. ✅ Verify Python installation
2. ✅ Install dependencies
3. ✅ Run smoke tests
4. ✅ Review test reports
5. ✅ Run full test suite
6. ✅ Customize tests as needed

---

**Need Help?** Check:
- `README_TESTING.md` - Detailed documentation
- `QUICK_START.md` - Quick reference
- `FRAMEWORK_SUMMARY.md` - Framework overview


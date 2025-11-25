# Quick Start Guide - Running Tests

## Test URL
**Application URL**: [https://muntasir101.github.io/CRBA/](https://muntasir101.github.io/CRBA/)

The framework is configured to test against this URL by default.

## Quick Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Smoke Tests (Recommended First)
```bash
# Windows
run_smoke_tests.bat

# Linux/Mac
chmod +x run_smoke_tests.sh
./run_smoke_tests.sh

# Or directly with pytest
pytest tests/test_smoke.py -v
```

### 3. Run All Tests
```bash
# Windows
run_tests.bat

# Linux/Mac
chmod +x run_tests.sh
./run_tests.sh

# Or directly with pytest
pytest
```

## Test Execution Examples

### Run Specific Test Suite
```bash
# Epic 1 - Room Management
pytest tests/test_epic1_room_management.py -v

# Epic 2 - User Management
pytest tests/test_epic2_user_management.py -v

# Epic 5 - Filtering
pytest tests/test_epic5_filtering.py -v
```

### Run with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run in Headless Mode
```bash
# Linux/Mac
export HEADLESS=true
pytest

# Windows
set HEADLESS=true
pytest
```

### Run Specific Test
```bash
# Example: Test room list display
pytest tests/test_epic1_room_management.py::TestFR11RoomListDisplay::test_display_active_rooms -v
```

### Run Tests with Markers
```bash
# Run only smoke tests
pytest -m smoke

# Run Epic 1 tests
pytest -m epic1

# Run regression tests
pytest -m regression
```

## Expected Test Results

### Smoke Tests (5 tests)
- ✅ Application loads
- ✅ Dashboard displayed
- ✅ Rooms section accessible
- ✅ Login modal opens
- ✅ Register modal opens

### Epic 1 Tests (15+ tests)
- Room List Display
- Room Details View
- Availability Checking
- Room Booking
- Validation tests

### Epic 2 Tests (10+ tests)
- User Registration
- User Authentication
- Booking Management

### Epic 5 Tests (4 tests)
- Room Filtering
- Combined Filters
- Search functionality

## Troubleshooting

### ChromeDriver Issues
If you see ChromeDriver errors:
```bash
# The framework uses webdriver-manager which auto-downloads ChromeDriver
# Make sure Chrome browser is installed
```

### Connection Issues
If tests fail to connect:
1. Verify the URL is accessible: https://muntasir101.github.io/CRBA/
2. Check internet connection
3. Verify firewall settings

### Element Not Found
If you see "Element not found" errors:
1. Check if the application structure has changed
2. Verify locators in `locators.json`
3. Increase wait times in `conftest.py`

## Viewing Test Reports

After running tests, view the HTML report:
```bash
# Report location
reports/report.html

# Open in browser
# Windows
start reports/report.html

# Linux/Mac
open reports/report.html
# or
xdg-open reports/report.html
```

## Configuration

### Change Test URL
Edit `config.py`:
```python
BASE_URL = "https://muntasir101.github.io/CRBA/"
```

Or use environment variable:
```bash
export BASE_URL=https://your-custom-url.com
pytest
```

## Next Steps

1. ✅ Run smoke tests to verify setup
2. ✅ Review test reports
3. ✅ Run full test suite
4. ✅ Customize tests for your needs
5. ✅ Integrate with CI/CD

## Support

- Check `README_TESTING.md` for detailed documentation
- Review `LOCATOR_REVIEW.md` for locator information
- See `FRAMEWORK_SUMMARY.md` for framework overview

---

**Ready to test!** 🚀


# Test URL Configuration Complete ✅

## Configuration Summary

The test automation framework has been configured to test against the live application:

**Test URL**: [https://muntasir101.github.io/CRBA/](https://muntasir101.github.io/CRBA/)

## What Was Updated

### 1. Configuration Files
- ✅ `config.py` - Created with default URL configuration
- ✅ `tests/conftest.py` - Updated to use GitHub Pages URL as default
- ✅ Base URL fixture now points to: `https://muntasir101.github.io/CRBA/`

### 2. New Test Files
- ✅ `tests/test_smoke.py` - Quick smoke tests for validation
- ✅ Smoke tests verify:
  - Application loads
  - Dashboard displays
  - Rooms section accessible
  - Login/Register modals work

### 3. Quick Start Scripts
- ✅ `run_smoke_tests.bat` - Windows script for smoke tests
- ✅ `run_smoke_tests.sh` - Linux/Mac script for smoke tests

### 4. Documentation
- ✅ `QUICK_START.md` - Quick start guide
- ✅ `README_TESTING.md` - Updated with test URL information

## How to Run Tests

### Quick Test (Smoke Tests)
```bash
# Windows
run_smoke_tests.bat

# Linux/Mac
chmod +x run_smoke_tests.sh
./run_smoke_tests.sh

# Or with pytest
pytest tests/test_smoke.py -v
```

### Full Test Suite
```bash
# Windows
run_tests.bat

# Linux/Mac
./run_tests.sh

# Or with pytest
pytest
```

## Test Coverage

The framework includes tests for:

1. **Epic 1: Room Management** (15+ tests)
   - Room list display
   - Room details view
   - Availability checking
   - Room booking
   - Validation tests

2. **Epic 2: User Management** (10+ tests)
   - User registration
   - User authentication
   - Booking management

3. **Epic 5: Filtering** (4 tests)
   - Room filtering
   - Combined filters
   - Search functionality

4. **Smoke Tests** (5 tests)
   - Critical functionality validation

## Configuration Options

### Using Default URL (GitHub Pages)
Tests will automatically use: `https://muntasir101.github.io/CRBA/`

### Using Custom URL
```bash
# Linux/Mac
export BASE_URL=https://your-custom-url.com
pytest

# Windows
set BASE_URL=https://your-custom-url.com
pytest
```

Or edit `config.py`:
```python
BASE_URL = "https://your-custom-url.com"
```

## Verification

To verify the configuration:

1. **Check config.py**
   ```python
   BASE_URL = "https://muntasir101.github.io/CRBA/"
   ```

2. **Run smoke test**
   ```bash
   pytest tests/test_smoke.py::TestSmokeTests::test_application_loads -v
   ```

3. **Check test output**
   - Should navigate to GitHub Pages URL
   - Should load the application successfully

## Next Steps

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Run smoke tests: `pytest tests/test_smoke.py -v`
3. ✅ Run full suite: `pytest`
4. ✅ Review reports: `reports/report.html`

## Files Modified/Created

- ✅ `config.py` - Configuration file
- ✅ `tests/conftest.py` - Updated base_url fixture
- ✅ `tests/test_smoke.py` - Smoke tests
- ✅ `QUICK_START.md` - Quick start guide
- ✅ `run_smoke_tests.bat` - Windows smoke test script
- ✅ `run_smoke_tests.sh` - Linux/Mac smoke test script

---

**Framework is ready to test the live application!** 🎉

All tests are configured to run against: https://muntasir101.github.io/CRBA/


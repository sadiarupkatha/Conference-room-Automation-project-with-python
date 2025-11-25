# Conference Room Booking Application - Test Automation Framework

## Overview
This is a Selenium Python automation framework for testing the Conference Room Booking Application (CRBA). The framework follows Page Object Model (POM) design pattern and uses pytest as the test runner.

**Test URL**: [https://muntasir101.github.io/CRBA/](https://muntasir101.github.io/CRBA/)

## Project Structure
```
CRBA-master/
├── tests/
│   ├── __init__.py
│   ├── conftest.py                    # Pytest fixtures and configuration
│   ├── pages/                         # Page Object Model classes
│   │   ├── __init__.py
│   │   ├── base_page.py              # Base page class
│   │   ├── login_page.py
│   │   ├── register_page.py
│   │   ├── dashboard_page.py
│   │   ├── rooms_page.py
│   │   ├── room_details_page.py
│   │   ├── my_bookings_page.py
│   │   ├── find_room_page.py
│   │   └── quick_book_page.py
│   ├── utils/                         # Utility functions
│   │   ├── __init__.py
│   │   ├── helpers.py                 # Helper functions
│   │   └── test_data.py               # Test data constants
│   ├── test_epic1_room_management.py
│   ├── test_epic2_user_management.py
│   └── test_epic5_filtering.py
├── locators.json                      # Locator inventory
├── LOCATOR_REVIEW.md                  # Locator review documentation
├── requirements.txt                   # Python dependencies
├── pytest.ini                        # Pytest configuration
└── README_TESTING.md                 # This file
```

## Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- pip package manager

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd CRBA-master/CRBA-master
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_epic1_room_management.py
```

### Run specific test class
```bash
pytest tests/test_epic1_room_management.py::TestFR11RoomListDisplay
```

### Run specific test
```bash
pytest tests/test_epic1_room_management.py::TestFR11RoomListDisplay::test_display_active_rooms
```

### Run tests with markers
```bash
pytest -m epic1
pytest -m smoke
```

### Run tests in parallel
```bash
pytest -n auto
```

### Run with HTML report
```bash
pytest --html=reports/report.html
```

### Run in headless mode
```bash
# Set environment variable
export HEADLESS=true  # Linux/Mac
set HEADLESS=true     # Windows

pytest
```

## Test Organization

Tests are organized by Epic and Functional Requirements:

- **Epic 1**: Room Management (FR-1.1 to FR-1.5)
- **Epic 2**: User Account & Profile Management (FR-2.1 to FR-2.4)
- **Epic 3**: Advanced Booking Management (FR-3.1 to FR-3.2)
- **Epic 4**: Admin – Room & Resource Management (FR-4.1 to FR-4.2)
- **Epic 5**: Enhanced Filtering (FR-5.1)
- **Epic 6**: Notifications & Calendar Integration (FR-6.1)
- **Epic 7**: Reporting & Analytics (FR-7.1)

## Page Object Model

The framework uses Page Object Model pattern where each page/section has its own class:

- `BasePage`: Base class with common methods
- `LoginPage`: Login modal interactions
- `RegisterPage`: Registration modal interactions
- `DashboardPage`: Dashboard section
- `RoomsPage`: Rooms listing and filtering
- `RoomDetailsPage`: Room details and booking form
- `MyBookingsPage`: User bookings management
- `FindRoomPage`: Room search functionality
- `QuickBookPage`: Quick booking modal

## Locators

All locators are documented in:
- `locators.json`: Structured JSON format
- `LOCATOR_REVIEW.md`: Comprehensive documentation

Locator strategy:
1. **Priority 1**: Use ID locators (most stable)
2. **Priority 2**: Use data attributes for dynamic content
3. **Priority 3**: Use class selectors with context

## Configuration

### Base URL
The framework defaults to the GitHub Pages URL: `https://muntasir101.github.io/CRBA/`

To use a different URL:

```bash
# Linux/Mac
export BASE_URL=http://localhost:8000
pytest

# Windows
set BASE_URL=http://localhost:8000
pytest
```

Or update `config.py` to change the default URL.

### Browser Options
Browser options can be configured in `conftest.py`:
- Headless mode
- Window size
- Chrome options

## Test Data

Test data is centralized in `tests/utils/test_data.py`:
- User credentials
- Room data
- Date/time helpers
- Validation test cases

## Utilities

Helper functions in `tests/utils/helpers.py`:
- Date/time manipulation
- Email validation
- Password validation
- Business hours checking
- Duration validation

## Screenshots

Screenshots are automatically taken on test failure and saved to `screenshots/` directory.

## Reports

Test reports are generated in HTML format:
- Location: `reports/report.html`
- Self-contained HTML file
- Includes test results, timings, and error details

## Best Practices

1. **Use Page Objects**: Always interact with pages through Page Object classes
2. **Explicit Waits**: Use WebDriverWait for element interactions
3. **Data-Driven**: Use parametrize for multiple test scenarios
4. **Clean Tests**: Keep test methods focused and readable
5. **Error Handling**: Handle exceptions gracefully
6. **Test Independence**: Each test should be independent and runnable alone

## Troubleshooting

### ChromeDriver Issues
The framework uses `webdriver-manager` to automatically download ChromeDriver. If issues occur:
1. Ensure Chrome browser is installed
2. Check Chrome version compatibility
3. Manually download ChromeDriver if needed

### Element Not Found
- Check if element is dynamically loaded (add explicit wait)
- Verify locator is correct in `locators.json`
- Check if element is in iframe (switch to iframe first)

### Tests Failing Intermittently
- Increase wait timeouts
- Add explicit waits before interactions
- Check for race conditions

## Continuous Integration

The framework can be integrated with CI/CD pipelines:

```yaml
# Example GitHub Actions
- name: Run Tests
  run: |
    pip install -r requirements.txt
    pytest --html=reports/report.html
```

## Future Enhancements

- [ ] Add API testing support
- [ ] Integrate with Allure reporting
- [ ] Add database validation
- [ ] Implement test data management
- [ ] Add visual regression testing
- [ ] Support for multiple browsers
- [ ] Mobile testing support

## Contributing

When adding new tests:
1. Follow existing naming conventions
2. Use Page Object Model pattern
3. Add appropriate markers
4. Update documentation
5. Ensure tests are independent

## Support

For issues or questions:
1. Check `LOCATOR_REVIEW.md` for locator information
2. Review test examples in existing test files
3. Check pytest documentation for advanced features

## License

This test automation framework is part of the Conference Room Booking Application project.


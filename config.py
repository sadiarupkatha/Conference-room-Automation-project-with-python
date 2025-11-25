"""
Configuration file for test automation framework
"""
import os

# Application URL
BASE_URL = os.getenv("BASE_URL", "https://muntasir101.github.io/CRBA/")

# Test Configuration
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10

# Browser Configuration
BROWSER = os.getenv("BROWSER", "chrome")
WINDOW_SIZE = "1920,1080"

# Test Data
DEFAULT_USER = {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
}

# Screenshot Configuration
SCREENSHOT_DIR = "screenshots"
SCREENSHOT_ON_FAILURE = True

# Report Configuration
REPORT_DIR = "reports"
HTML_REPORT = True


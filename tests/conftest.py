"""
Pytest configuration and fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
from datetime import datetime

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from config import BASE_URL as DEFAULT_BASE_URL
except ImportError:
    DEFAULT_BASE_URL = "https://muntasir101.github.io/CRBA/"


@pytest.fixture(scope="session")
def driver():
    """Create and configure WebDriver instance"""
    chrome_options = Options()
    
    # Add options based on environment
    if os.getenv("HEADLESS", "false").lower() == "true":
        chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Initialize driver
    try:
        # Try to use webdriver-manager first
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        # Fallback: try without service (uses system PATH)
        print(f"Warning: ChromeDriverManager failed: {e}")
        print("Attempting to use Chrome from system PATH...")
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as e2:
            raise Exception(f"Failed to initialize Chrome driver. Make sure Chrome browser is installed. Error: {e2}")
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    
    # Cleanup
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Get base URL from environment or use default"""
    return os.getenv("BASE_URL", DEFAULT_BASE_URL)


@pytest.fixture(scope="function")
def setup_driver(driver, base_url):
    """Setup driver with base URL"""
    driver.get(base_url)
    yield driver


@pytest.fixture(scope="function")
def test_user():
    """Test user credentials"""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshots on failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """Take screenshot on test failure"""
    yield
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(
            screenshot_dir, 
            f"{request.node.name}_{timestamp}.png"
        )
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")


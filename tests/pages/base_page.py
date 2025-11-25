"""
Base Page Object Model class
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator_type, locator_value, timeout=10):
        """Find element with explicit wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            if locator_type == "id":
                return wait.until(EC.presence_of_element_located((By.ID, locator_value)))
            elif locator_type == "class":
                return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
            elif locator_type == "css":
                return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
            elif locator_type == "xpath":
                return wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
            elif locator_type == "data_attribute":
                return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[{locator_value}]")))
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {locator_type}={locator_value}")
    
    def find_elements(self, locator_type, locator_value, timeout=10):
        """Find multiple elements"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            if locator_type == "id":
                return wait.until(EC.presence_of_all_elements_located((By.ID, locator_value)))
            elif locator_type == "class":
                return wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, locator_value)))
            elif locator_type == "css":
                return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator_value)))
            elif locator_type == "xpath":
                return wait.until(EC.presence_of_all_elements_located((By.XPATH, locator_value)))
            elif locator_type == "data_attribute":
                return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"[{locator_value}]")))
        except TimeoutException:
            return []
    
    def click(self, locator_type, locator_value):
        """Click on element"""
        element = self.find_element(locator_type, locator_value)
        # For data attributes, use CSS selector
        if locator_type == "data_attribute":
            by = (By.CSS_SELECTOR, f"[{locator_value}]")
        else:
            by = (self._get_by(locator_type), locator_value)
        self.wait.until(EC.element_to_be_clickable(by))
        element.click()
    
    def send_keys(self, locator_type, locator_value, text):
        """Send keys to element"""
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator_type, locator_value):
        """Get text from element"""
        element = self.find_element(locator_type, locator_value)
        return element.text
    
    def is_displayed(self, locator_type, locator_value, timeout=5):
        """Check if element is displayed"""
        try:
            element = self.find_element(locator_type, locator_value, timeout)
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def is_enabled(self, locator_type, locator_value):
        """Check if element is enabled"""
        element = self.find_element(locator_type, locator_value)
        return element.is_enabled()
    
    def wait_for_element(self, locator_type, locator_value, timeout=10):
        """Wait for element to be present"""
        return self.find_element(locator_type, locator_value, timeout)
    
    def wait_for_element_visible(self, locator_type, locator_value, timeout=10):
        """Wait for element to be visible"""
        wait = WebDriverWait(self.driver, timeout)
        by = self._get_by(locator_type)
        if locator_type == "data_attribute":
            by = (By.CSS_SELECTOR, f"[{locator_value}]")
        else:
            by = (by, locator_value)
        return wait.until(EC.visibility_of_element_located(by))
    
    def wait_for_element_clickable(self, locator_type, locator_value, timeout=10):
        """Wait for element to be clickable"""
        wait = WebDriverWait(self.driver, timeout)
        by = self._get_by(locator_type)
        if locator_type == "data_attribute":
            by = (By.CSS_SELECTOR, f"[{locator_value}]")
        else:
            by = (by, locator_value)
        return wait.until(EC.element_to_be_clickable(by))
    
    def _get_by(self, locator_type):
        """Get By locator type"""
        mapping = {
            "id": By.ID,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH
        }
        return mapping.get(locator_type, By.ID)
    
    def scroll_to_element(self, locator_type, locator_value):
        """Scroll to element"""
        element = self.find_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    
    def get_attribute(self, locator_type, locator_value, attribute_name):
        """Get element attribute"""
        element = self.find_element(locator_type, locator_value)
        return element.get_attribute(attribute_name)
    
    def execute_script(self, script, *args):
        """Execute JavaScript"""
        return self.driver.execute_script(script, *args)
    
    def take_screenshot(self, filename):
        """Take screenshot"""
        self.driver.save_screenshot(filename)


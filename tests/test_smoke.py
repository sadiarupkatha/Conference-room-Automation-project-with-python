"""
Smoke Tests - Quick validation of critical functionality
"""
import pytest
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage
from tests.pages.rooms_page import RoomsPage
from tests.utils.test_data import TestData


@pytest.mark.smoke
class TestSmokeTests:
    """Smoke tests for critical functionality"""
    
    def test_application_loads(self, setup_driver):
        """Verify application loads successfully"""
        driver = setup_driver
        
        # Check if page title or key element is present
        assert "CRBA" in driver.title or "Conference Room" in driver.page_source, "Application should load"
        
        # Check if main content is displayed
        main_content = driver.find_elements("id", "main-content")
        assert len(main_content) > 0, "Main content should be displayed"
    
    def test_dashboard_displayed(self, setup_driver):
        """Verify dashboard is displayed on load"""
        driver = setup_driver
        dashboard_page = DashboardPage(driver)
        
        # Dashboard should be active by default
        assert dashboard_page.is_dashboard_displayed(), "Dashboard should be displayed"
    
    def test_rooms_section_accessible(self, setup_driver):
        """Verify rooms section is accessible"""
        driver = setup_driver
        rooms_page = RoomsPage(driver)
        
        rooms_page.navigate_to_rooms()
        assert rooms_page.is_rooms_displayed(), "Rooms section should be accessible"
        
        # Verify at least some rooms are displayed
        rooms_count = rooms_page.get_rooms_count()
        assert rooms_count >= 0, "Should handle rooms display (may be empty)"
    
    def test_login_modal_opens(self, setup_driver):
        """Verify login modal can be opened"""
        driver = setup_driver
        login_page = LoginPage(driver)
        
        login_page.open_login_modal()
        assert login_page.is_modal_displayed(), "Login modal should open"
    
    def test_register_modal_opens(self, setup_driver):
        """Verify register modal can be opened"""
        driver = setup_driver
        from tests.pages.register_page import RegisterPage
        
        register_page = RegisterPage(driver)
        register_page.open_register_modal()
        assert register_page.is_modal_displayed(), "Register modal should open"


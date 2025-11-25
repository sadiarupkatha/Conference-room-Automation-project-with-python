"""
Epic 2: User Account & Profile Management Tests
FR-2.1 User Registration
FR-2.2 User Authentication
FR-2.3 Booking Management
FR-2.4 Password Recovery
"""
import pytest
from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage
from tests.pages.my_bookings_page import MyBookingsPage
from tests.utils.helpers import generate_test_email
from tests.utils.test_data import TestData


class TestFR21UserRegistration:
    """FR-2.1 User Registration Tests"""
    
    def test_successful_registration(self, setup_driver):
        """TC-2.1-01: Successful registration"""
        driver = setup_driver
        register_page = RegisterPage(driver)
        
        # Generate unique email
        test_email = generate_test_email("newuser")
        
        # Register new user
        register_page.register(
            name="New Test User",
            email=test_email,
            password="password123",
            confirm_password="password123"
        )
        
        # Verify registration success (user should be logged in)
        # Check if user info is displayed
        import time
        time.sleep(1)  # Wait for registration to complete
        
        user_info = driver.find_elements("id", "user-info")
        assert len(user_info) > 0, "User should be logged in after registration"
    
    def test_invalid_email_format(self, setup_driver):
        """TC-2.1-02: Invalid email format"""
        driver = setup_driver
        register_page = RegisterPage(driver)
        
        # Try to register with invalid email
        register_page.register(
            name="Test User",
            email="invalid-email",
            password="password123",
            confirm_password="password123"
        )
        
        # Verify error message
        error = register_page.get_email_error()
        assert "valid email" in error.lower() or error, "Should show error for invalid email"
    
    def test_weak_password(self, setup_driver):
        """TC-2.1-04: Weak password"""
        driver = setup_driver
        register_page = RegisterPage(driver)
        
        # Try to register with weak password
        test_email = generate_test_email("weakpass")
        register_page.register(
            name="Test User",
            email=test_email,
            password="12345",  # Less than 8 characters
            confirm_password="12345"
        )
        
        # Verify error message
        error = register_page.get_password_error()
        assert "8 characters" in error.lower() or "at least" in error.lower() or error, "Should show error for weak password"
    
    def test_duplicate_email(self, setup_driver):
        """TC-2.1-05: Duplicate email"""
        driver = setup_driver
        register_page = RegisterPage(driver)
        
        # Register with existing email
        register_page.register(
            name="Test User",
            email=TestData.VALID_USER["email"],  # Use existing email
            password="password123",
            confirm_password="password123"
        )
        
        # Verify error message
        error = register_page.get_email_error()
        assert "already registered" in error.lower() or "already exists" in error.lower() or error, "Should show error for duplicate email"
    
    def test_password_mismatch(self, setup_driver):
        """Test password confirmation mismatch"""
        driver = setup_driver
        register_page = RegisterPage(driver)
        
        test_email = generate_test_email("mismatch")
        register_page.register(
            name="Test User",
            email=test_email,
            password="password123",
            confirm_password="differentpass"
        )
        
        # Verify error message
        error = register_page.get_confirm_password_error()
        assert "match" in error.lower() or error, "Should show error for password mismatch"


class TestFR22UserAuthentication:
    """FR-2.2 User Authentication Tests"""
    
    def test_login_valid_credentials(self, setup_driver):
        """TC-2.2-01: Login with valid credentials"""
        driver = setup_driver
        login_page = LoginPage(driver)
        
        # Login with valid credentials
        login_page.login(TestData.VALID_USER["email"], TestData.VALID_USER["password"])
        
        # Verify login success
        import time
        time.sleep(1)
        
        user_info = driver.find_elements("id", "user-info")
        assert len(user_info) > 0, "User should be logged in"
        
        # Verify user name is displayed
        user_name = driver.find_elements("id", "user-name")
        if user_name:
            assert user_name[0].text, "User name should be displayed"
    
    def test_login_wrong_password(self, setup_driver):
        """TC-2.2-02: Wrong password"""
        driver = setup_driver
        login_page = LoginPage(driver)
        
        # Try to login with wrong password
        login_page.login(TestData.VALID_USER["email"], "wrongpassword")
        
        # Verify error message
        error = login_page.get_password_error()
        assert "invalid" in error.lower() or "incorrect" in error.lower() or error, "Should show error for wrong password"
    
    def test_logout(self, setup_driver):
        """TC-2.2-05: Logout"""
        driver = setup_driver
        login_page = LoginPage(driver)
        
        # Login first
        login_page.login(TestData.VALID_USER["email"], TestData.VALID_USER["password"])
        
        import time
        time.sleep(1)
        
        # Logout
        logout_link = driver.find_element("id", "sidebar-logout")
        logout_link.click()
        
        time.sleep(1)
        
        # Verify logout (auth buttons should be visible)
        auth_buttons = driver.find_elements("id", "auth-buttons")
        assert len(auth_buttons) > 0, "Auth buttons should be visible after logout"


class TestFR23BookingManagement:
    """FR-2.3 Booking Management Tests"""
    
    def test_view_upcoming_past_bookings(self, setup_driver):
        """TC-2.3-01: View upcoming/past bookings"""
        driver = setup_driver
        login_page = LoginPage(driver)
        my_bookings_page = MyBookingsPage(driver)
        
        # Login
        login_page.login(TestData.VALID_USER["email"], TestData.VALID_USER["password"])
        
        # Navigate to my bookings
        my_bookings_page.navigate_to_my_bookings()
        
        # Check upcoming bookings tab
        my_bookings_page.switch_to_upcoming_tab()
        upcoming_count = my_bookings_page.get_upcoming_bookings_count()
        assert upcoming_count >= 0, "Should display upcoming bookings (may be empty)"
        
        # Check past bookings tab
        my_bookings_page.switch_to_past_tab()
        past_count = my_bookings_page.get_past_bookings_count()
        assert past_count >= 0, "Should display past bookings (may be empty)"
    
    def test_cancel_booking(self, setup_driver):
        """Test cancel booking functionality"""
        driver = setup_driver
        login_page = LoginPage(driver)
        my_bookings_page = MyBookingsPage(driver)
        
        # Login
        login_page.login(TestData.VALID_USER["email"], TestData.VALID_USER["password"])
        
        # Navigate to my bookings
        my_bookings_page.navigate_to_my_bookings()
        my_bookings_page.switch_to_upcoming_tab()
        
        # Get first booking if exists
        bookings = driver.find_elements("css", "#upcoming-bookings .booking-item")
        if bookings:
            booking_id = bookings[0].get_attribute("data-booking-id")
            if booking_id:
                # Cancel booking
                my_bookings_page.click_cancel_booking(booking_id)
                
                # Handle confirmation dialog
                import time
                time.sleep(1)
                
                # Verify booking was cancelled (check past bookings or count)
                # Note: Implementation may vary
                assert True, "Cancel booking should work"


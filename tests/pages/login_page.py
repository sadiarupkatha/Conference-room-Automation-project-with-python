"""
Login Page Object Model
"""
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object for Login Modal"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.modal_id = "login-modal"
        self.form_id = "login-form"
        self.email_id = "login-email"
        self.password_id = "login-password"
        self.email_error_id = "login-email-error"
        self.password_error_id = "login-password-error"
        self.switch_to_register_id = "switch-to-register"
    
    def open_login_modal(self):
        """Click login button to open modal"""
        self.click("id", "login-btn")
        self.wait_for_element_visible("id", self.modal_id)
    
    def enter_email(self, email):
        """Enter email address"""
        self.send_keys("id", self.email_id, email)
    
    def enter_password(self, password):
        """Enter password"""
        self.send_keys("id", self.password_id, password)
    
    def click_login(self):
        """Submit login form"""
        form = self.find_element("id", self.form_id)
        form.submit()
    
    def login(self, email, password):
        """Complete login flow"""
        self.open_login_modal()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
    
    def get_email_error(self):
        """Get email error message"""
        if self.is_displayed("id", self.email_error_id):
            return self.get_text("id", self.email_error_id)
        return ""
    
    def get_password_error(self):
        """Get password error message"""
        if self.is_displayed("id", self.password_error_id):
            return self.get_text("id", self.password_error_id)
        return ""
    
    def switch_to_register(self):
        """Switch to register modal"""
        self.click("id", self.switch_to_register_id)
    
    def is_modal_displayed(self):
        """Check if login modal is displayed"""
        return self.is_displayed("id", self.modal_id)
    
    def close_modal(self):
        """Close modal using close button"""
        self.click("class", "close-modal")


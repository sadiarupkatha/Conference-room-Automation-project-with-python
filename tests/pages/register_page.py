"""
Register Page Object Model
"""
from .base_page import BasePage


class RegisterPage(BasePage):
    """Page Object for Register Modal"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.modal_id = "register-modal"
        self.form_id = "register-form"
        self.name_id = "register-name"
        self.email_id = "register-email"
        self.password_id = "register-password"
        self.confirm_password_id = "register-confirm-password"
        self.name_error_id = "register-name-error"
        self.email_error_id = "register-email-error"
        self.password_error_id = "register-password-error"
        self.confirm_password_error_id = "register-confirm-password-error"
        self.switch_to_login_id = "switch-to-login"
    
    def open_register_modal(self):
        """Click register button to open modal"""
        self.click("id", "register-btn")
        self.wait_for_element_visible("id", self.modal_id)
    
    def enter_name(self, name):
        """Enter full name"""
        self.send_keys("id", self.name_id, name)
    
    def enter_email(self, email):
        """Enter email address"""
        self.send_keys("id", self.email_id, email)
    
    def enter_password(self, password):
        """Enter password"""
        self.send_keys("id", self.password_id, password)
    
    def enter_confirm_password(self, password):
        """Enter confirm password"""
        self.send_keys("id", self.confirm_password_id, password)
    
    def click_register(self):
        """Submit register form"""
        form = self.find_element("id", self.form_id)
        form.submit()
    
    def register(self, name, email, password, confirm_password=None):
        """Complete registration flow"""
        if confirm_password is None:
            confirm_password = password
        self.open_register_modal()
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_register()
    
    def get_name_error(self):
        """Get name error message"""
        if self.is_displayed("id", self.name_error_id):
            return self.get_text("id", self.name_error_id)
        return ""
    
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
    
    def get_confirm_password_error(self):
        """Get confirm password error message"""
        if self.is_displayed("id", self.confirm_password_error_id):
            return self.get_text("id", self.confirm_password_error_id)
        return ""
    
    def switch_to_login(self):
        """Switch to login modal"""
        self.click("id", self.switch_to_login_id)
    
    def is_modal_displayed(self):
        """Check if register modal is displayed"""
        return self.is_displayed("id", self.modal_id)
    
    def close_modal(self):
        """Close modal using close button"""
        self.click("class", "close-modal")


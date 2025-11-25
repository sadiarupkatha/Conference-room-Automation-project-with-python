"""
My Bookings Page Object Model
"""
from .base_page import BasePage


class MyBookingsPage(BasePage):
    """Page Object for My Bookings Section"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.section_id = "my-bookings"
        self.upcoming_bookings_id = "upcoming-bookings"
        self.past_bookings_id = "past-bookings"
    
    def navigate_to_my_bookings(self):
        """Navigate to my bookings section"""
        self.click("data_attribute", 'data-section="my-bookings"')
        self.wait_for_element_visible("id", self.section_id)
    
    def is_my_bookings_displayed(self):
        """Check if my bookings section is displayed"""
        return self.is_displayed("id", self.section_id)
    
    def switch_to_upcoming_tab(self):
        """Switch to upcoming bookings tab"""
        self.click("data_attribute", 'data-tab="upcoming"')
        self.wait_for_element_visible("id", self.upcoming_bookings_id)
    
    def switch_to_past_tab(self):
        """Switch to past bookings tab"""
        self.click("data_attribute", 'data-tab="past"')
        self.wait_for_element_visible("id", self.past_bookings_id)
    
    def get_upcoming_bookings_count(self):
        """Get count of upcoming bookings"""
        bookings = self.find_elements("css", f"#{self.upcoming_bookings_id} .booking-item")
        return len(bookings)
    
    def get_past_bookings_count(self):
        """Get count of past bookings"""
        bookings = self.find_elements("css", f"#{self.past_bookings_id} .booking-item")
        return len(bookings)
    
    def get_booking_by_id(self, booking_id):
        """Get booking item element by booking ID"""
        return self.find_element("css", f'[data-booking-id="{booking_id}"]')
    
    def click_edit_booking(self, booking_id):
        """Click edit button for a booking"""
        edit_button = self.find_element("css", f'[data-booking-id="{booking_id}"] .edit-booking')
        edit_button.click()
    
    def click_cancel_booking(self, booking_id):
        """Click cancel button for a booking"""
        cancel_button = self.find_element("css", f'[data-booking-id="{booking_id}"] .cancel-booking')
        cancel_button.click()
    
    def click_view_booking(self, booking_id):
        """Click view button for a booking"""
        view_button = self.find_element("css", f'[data-booking-id="{booking_id}"] .view-booking')
        view_button.click()
    
    def is_upcoming_bookings_empty(self):
        """Check if upcoming bookings section is empty"""
        try:
            text = self.get_text("id", self.upcoming_bookings_id)
            return "no upcoming bookings" in text.lower() or "please log in" in text.lower()
        except:
            return False
    
    def is_past_bookings_empty(self):
        """Check if past bookings section is empty"""
        try:
            text = self.get_text("id", self.past_bookings_id)
            return "no past bookings" in text.lower() or "please log in" in text.lower()
        except:
            return False
    
    def get_booking_title(self, booking_id):
        """Get booking title"""
        try:
            booking_item = self.get_booking_by_id(booking_id)
            title_element = booking_item.find_element("css", "h3")
            return title_element.text
        except:
            return ""
    
    def get_booking_date(self, booking_id):
        """Get booking date"""
        try:
            booking_item = self.get_booking_by_id(booking_id)
            meta_text = booking_item.find_element("css", ".booking-meta").text
            # Extract date from meta text
            import re
            # Look for date pattern YYYY-MM-DD
            match = re.search(r'(\d{4}-\d{2}-\d{2})', meta_text)
            if match:
                return match.group(1)
        except:
            return ""


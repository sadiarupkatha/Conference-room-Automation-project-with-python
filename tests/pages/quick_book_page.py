"""
Quick Book Page Object Model
"""
from .base_page import BasePage


class QuickBookPage(BasePage):
    """Page Object for Quick Book Modal"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.modal_id = "quick-book-modal"
        self.form_id = "quick-book-form"
        self.meeting_title_id = "quick-meeting-title"
        self.date_id = "quick-date"
        self.start_time_id = "quick-start-time"
        self.duration_id = "quick-duration"
        self.attendees_id = "quick-attendees"
    
    def open_quick_book_modal(self):
        """Open quick book modal"""
        self.click("id", "quick-book-btn")
        self.wait_for_element_visible("id", self.modal_id)
    
    def enter_meeting_title(self, title):
        """Enter meeting title"""
        self.send_keys("id", self.meeting_title_id, title)
    
    def enter_date(self, date):
        """Enter date"""
        self.send_keys("id", self.date_id, date)
    
    def enter_start_time(self, time):
        """Enter start time"""
        self.send_keys("id", self.start_time_id, time)
    
    def select_duration(self, duration_minutes):
        """Select duration in minutes"""
        from selenium.webdriver.support.ui import Select
        duration_select = self.find_element("id", self.duration_id)
        select = Select(duration_select)
        select.select_by_value(str(duration_minutes))
    
    def enter_attendees(self, count):
        """Enter number of attendees"""
        self.send_keys("id", self.attendees_id, str(count))
    
    def submit_quick_book(self):
        """Submit quick book form"""
        form = self.find_element("id", self.form_id)
        form.submit()
    
    def quick_book(self, title, date, start_time, duration_minutes, attendees):
        """Complete quick book flow"""
        self.open_quick_book_modal()
        self.enter_meeting_title(title)
        self.enter_date(date)
        self.enter_start_time(start_time)
        self.select_duration(duration_minutes)
        self.enter_attendees(attendees)
        self.submit_quick_book()
    
    def is_modal_displayed(self):
        """Check if quick book modal is displayed"""
        return self.is_displayed("id", self.modal_id)
    
    def close_modal(self):
        """Close modal using close button"""
        self.click("class", "close-modal")


"""
Room Details Page Object Model
"""
from .base_page import BasePage
from datetime import datetime, timedelta


class RoomDetailsPage(BasePage):
    """Page Object for Room Details Section"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.section_id = "room-details"
        self.room_name_id = "selected-room-name"
        self.room_location_id = "selected-room-location"
        self.room_capacity_id = "selected-room-capacity"
        self.room_features_id = "selected-room-features"
        self.room_availability_text_id = "room-availability-text"
        self.booking_form_id = "booking-form"
        self.meeting_title_id = "meeting-title"
        self.booking_date_id = "booking-date"
        self.start_time_id = "start-time"
        self.end_time_id = "end-time"
        self.attendees_id = "attendees"
        self.meeting_notes_id = "meeting-notes"
        self.cancel_booking_id = "cancel-booking"
    
    def is_room_details_displayed(self):
        """Check if room details section is displayed"""
        return self.is_displayed("id", self.section_id)
    
    def get_room_name(self):
        """Get room name"""
        return self.get_text("id", self.room_name_id)
    
    def get_room_location(self):
        """Get room location"""
        return self.get_text("id", self.room_location_id)
    
    def get_room_capacity(self):
        """Get room capacity"""
        capacity_text = self.get_text("id", self.room_capacity_id)
        try:
            return int(capacity_text)
        except:
            return 0
    
    def get_room_features(self):
        """Get list of room features"""
        features_container = self.find_element("id", self.room_features_id)
        feature_tags = features_container.find_elements("css", ".feature-tag")
        return [tag.text for tag in feature_tags]
    
    def get_availability_status(self):
        """Get availability status text"""
        return self.get_text("id", self.room_availability_text_id)
    
    def is_room_available(self):
        """Check if room is available"""
        availability_container = self.find_element("css", ".availability")
        return "available" in availability_container.get_attribute("class").lower()
    
    def enter_meeting_title(self, title):
        """Enter meeting title"""
        self.send_keys("id", self.meeting_title_id, title)
    
    def enter_booking_date(self, date):
        """Enter booking date (format: YYYY-MM-DD)"""
        self.send_keys("id", self.booking_date_id, date)
    
    def enter_start_time(self, time):
        """Enter start time (format: HH:MM)"""
        self.send_keys("id", self.start_time_id, time)
    
    def enter_end_time(self, time):
        """Enter end time (format: HH:MM)"""
        self.send_keys("id", self.end_time_id, time)
    
    def enter_attendees(self, count):
        """Enter number of attendees"""
        self.send_keys("id", self.attendees_id, str(count))
    
    def enter_meeting_notes(self, notes):
        """Enter meeting notes"""
        self.send_keys("id", self.meeting_notes_id, notes)
    
    def submit_booking(self):
        """Submit booking form"""
        form = self.find_element("id", self.booking_form_id)
        form.submit()
    
    def book_room(self, title, date, start_time, end_time, attendees, notes=""):
        """Complete booking flow"""
        self.enter_meeting_title(title)
        self.enter_booking_date(date)
        self.enter_start_time(start_time)
        self.enter_end_time(end_time)
        self.enter_attendees(attendees)
        if notes:
            self.enter_meeting_notes(notes)
        self.submit_booking()
    
    def get_meeting_title_error(self):
        """Get meeting title error message"""
        error_id = "meeting-title-error"
        if self.is_displayed("id", error_id):
            return self.get_text("id", error_id)
        return ""
    
    def get_booking_date_error(self):
        """Get booking date error message"""
        error_id = "booking-date-error"
        if self.is_displayed("id", error_id):
            return self.get_text("id", error_id)
        return ""
    
    def get_start_time_error(self):
        """Get start time error message"""
        error_id = "start-time-error"
        if self.is_displayed("id", error_id):
            return self.get_text("id", error_id)
        return ""
    
    def get_end_time_error(self):
        """Get end time error message"""
        error_id = "end-time-error"
        if self.is_displayed("id", error_id):
            return self.get_text("id", error_id)
        return ""
    
    def get_attendees_error(self):
        """Get attendees error message"""
        error_id = "attendees-error"
        if self.is_displayed("id", error_id):
            return self.get_text("id", error_id)
        return ""
    
    def click_cancel_booking(self):
        """Click cancel booking button"""
        self.click("id", self.cancel_booking_id)
    
    def check_availability(self, date, start_time, end_time):
        """Check room availability for given date and time"""
        self.enter_booking_date(date)
        self.enter_start_time(start_time)
        self.enter_end_time(end_time)
        # Wait for availability check to update
        import time
        time.sleep(0.5)
        return self.is_room_available()
    
    def get_future_date(self, days_ahead=1):
        """Get future date string"""
        future_date = datetime.now() + timedelta(days=days_ahead)
        return future_date.strftime("%Y-%m-%d")
    
    def get_past_date(self, days_ago=1):
        """Get past date string"""
        past_date = datetime.now() - timedelta(days=days_ago)
        return past_date.strftime("%Y-%m-%d")


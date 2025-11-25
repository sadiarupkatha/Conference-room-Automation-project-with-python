"""
Rooms Page Object Model
"""
from .base_page import BasePage
import time


class RoomsPage(BasePage):
    """Page Object for Rooms Section"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.section_id = "rooms"
        self.capacity_filter_id = "capacity-filter"
        self.feature_filter_id = "feature-filter"
        self.date_filter_id = "date-filter"
        self.time_filter_id = "time-filter"
        self.apply_filters_id = "apply-filters"
        self.clear_filters_id = "clear-filters"
        self.all_rooms_id = "all-rooms"
    
    def navigate_to_rooms(self):
        """Navigate to rooms section"""
        # Find navigation link with data-section="rooms"
        nav_link = self.find_element("css", '[data-section="rooms"]')
        nav_link.click()
        self.wait_for_element_visible("id", self.section_id)
    
    def is_rooms_displayed(self):
        """Check if rooms section is displayed"""
        return self.is_displayed("id", self.section_id)
    
    def get_rooms_count(self):
        """Get count of displayed rooms"""
        rooms = self.find_elements("css", f"#{self.all_rooms_id} .room-card")
        return len(rooms)
    
    def filter_by_capacity(self, capacity_value):
        """Filter rooms by capacity"""
        from selenium.webdriver.support.ui import Select
        capacity_filter = self.find_element("id", self.capacity_filter_id)
        select = Select(capacity_filter)
        select.select_by_value(str(capacity_value))
    
    def filter_by_feature(self, feature_value):
        """Filter rooms by feature"""
        from selenium.webdriver.support.ui import Select
        feature_filter = self.find_element("id", self.feature_filter_id)
        select = Select(feature_filter)
        select.select_by_value(feature_value)
    
    def filter_by_date(self, date):
        """Filter rooms by date"""
        self.send_keys("id", self.date_filter_id, date)
    
    def filter_by_time(self, time):
        """Filter rooms by time"""
        self.send_keys("id", self.time_filter_id, time)
    
    def apply_filters(self):
        """Click apply filters button"""
        self.click("id", self.apply_filters_id)
        time.sleep(1)  # Wait for filter to apply
    
    def clear_filters(self):
        """Click clear filters button"""
        self.click("id", self.clear_filters_id)
        time.sleep(1)  # Wait for filters to clear
    
    def get_room_by_id(self, room_id):
        """Get room card element by room ID"""
        return self.find_element("data_attribute", f'data-room-id="{room_id}"')
    
    def click_room(self, room_id):
        """Click on a room card"""
        room_card = self.get_room_by_id(room_id)
        room_card.click()
        time.sleep(0.5)
    
    def click_book_room(self, room_id):
        """Click book button for a specific room"""
        book_button = self.find_element("css", f'[data-room-id="{room_id}"] .book-room')
        self.wait_for_element_clickable("css", f'[data-room-id="{room_id}"] .book-room')
        book_button.click()
    
    def is_room_available(self, room_id):
        """Check if room is available"""
        try:
            availability = self.find_element("css", f'[data-room-id="{room_id}"] .availability')
            return "available" in availability.get_attribute("class").lower()
        except:
            return False
    
    def get_room_name(self, room_id):
        """Get room name"""
        try:
            return self.get_text("css", f'[data-room-id="{room_id}"] .room-title')
        except:
            return ""
    
    def get_room_capacity(self, room_id):
        """Get room capacity"""
        try:
            meta_text = self.get_text("css", f'[data-room-id="{room_id}"] .room-meta')
            # Extract capacity from text like "10 people"
            import re
            match = re.search(r'(\d+)\s+people', meta_text)
            if match:
                return int(match.group(1))
        except:
            return 0
    
    def get_room_location(self, room_id):
        """Get room location"""
        try:
            meta_text = self.get_text("css", f'[data-room-id="{room_id}"] .room-meta')
            # Extract location (first part before comma or before "people")
            parts = meta_text.split(',')
            if len(parts) > 0:
                return parts[0].strip()
        except:
            return ""
    
    def is_empty_state_displayed(self):
        """Check if empty state message is displayed"""
        try:
            text = self.get_text("id", self.all_rooms_id)
            return "no rooms" in text.lower() or "no rooms match" in text.lower()
        except:
            return False


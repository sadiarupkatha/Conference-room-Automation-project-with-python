"""
Find Room Page Object Model
"""
from .base_page import BasePage


class FindRoomPage(BasePage):
    """Page Object for Find Available Room Section"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.section_id = "find-room"
        self.search_date_id = "search-date"
        self.search_start_time_id = "search-start-time"
        self.search_end_time_id = "search-end-time"
        self.search_capacity_id = "search-capacity"
        self.search_features_id = "search-features"
        self.search_rooms_id = "search-rooms"
        self.search_results_id = "search-results"
    
    def navigate_to_find_room(self):
        """Navigate to find room section"""
        self.click("data_attribute", 'data-section="find-room"')
        self.wait_for_element_visible("id", self.section_id)
    
    def is_find_room_displayed(self):
        """Check if find room section is displayed"""
        return self.is_displayed("id", self.section_id)
    
    def enter_search_date(self, date):
        """Enter search date"""
        self.send_keys("id", self.search_date_id, date)
    
    def enter_search_start_time(self, time):
        """Enter search start time"""
        self.send_keys("id", self.search_start_time_id, time)
    
    def enter_search_end_time(self, time):
        """Enter search end time"""
        self.send_keys("id", self.search_end_time_id, time)
    
    def enter_search_capacity(self, capacity):
        """Enter search capacity"""
        self.send_keys("id", self.search_capacity_id, str(capacity))
    
    def select_search_features(self, features):
        """Select search features (list of feature values)"""
        from selenium.webdriver.support.ui import Select
        feature_select = self.find_element("id", self.search_features_id)
        select = Select(feature_select)
        # Clear previous selections
        select.deselect_all()
        # Select new features
        for feature in features:
            try:
                select.select_by_value(feature)
            except:
                pass
    
    def click_search_rooms(self):
        """Click search rooms button"""
        self.click("id", self.search_rooms_id)
        import time
        time.sleep(1)  # Wait for search results
    
    def search_rooms(self, date, start_time, end_time, capacity=None, features=None):
        """Complete room search flow"""
        self.enter_search_date(date)
        self.enter_search_start_time(start_time)
        self.enter_search_end_time(end_time)
        if capacity:
            self.enter_search_capacity(capacity)
        if features:
            self.select_search_features(features)
        self.click_search_rooms()
    
    def get_search_results_count(self):
        """Get count of search results"""
        results = self.find_elements("css", f"#{self.search_results_id} .room-card")
        return len(results)
    
    def is_no_results_displayed(self):
        """Check if no results message is displayed"""
        try:
            text = self.get_text("id", self.search_results_id)
            return "no rooms available" in text.lower() or "no rooms match" in text.lower()
        except:
            return False


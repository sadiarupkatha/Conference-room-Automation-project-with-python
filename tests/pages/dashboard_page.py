"""
Dashboard Page Object Model
"""
from .base_page import BasePage


class DashboardPage(BasePage):
    """Page Object for Dashboard Section"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.section_id = "dashboard"
        self.stats_grid_id = "stats-grid"
        self.quick_book_action_id = "quick-book-action"
        self.profile_action_id = "profile-action"
        self.recent_bookings_id = "recent-bookings"
        self.featured_rooms_id = "featured-rooms"
    
    def navigate_to_dashboard(self):
        """Navigate to dashboard section"""
        self.click("data_attribute", 'data-section="dashboard"')
        self.wait_for_element_visible("id", self.section_id)
    
    def is_dashboard_displayed(self):
        """Check if dashboard is displayed"""
        return self.is_displayed("id", self.section_id)
    
    def get_stats_count(self):
        """Get count of stat cards"""
        stats = self.find_elements("css", "#stats-grid .stat-card")
        return len(stats)
    
    def click_quick_book(self):
        """Click quick book action button"""
        self.click("id", self.quick_book_action_id)
    
    def click_profile_action(self):
        """Click profile action button"""
        self.click("id", self.profile_action_id)
    
    def get_recent_bookings_count(self):
        """Get count of recent bookings"""
        bookings = self.find_elements("css", f"#{self.recent_bookings_id} .booking-item")
        return len(bookings)
    
    def get_featured_rooms_count(self):
        """Get count of featured rooms"""
        rooms = self.find_elements("css", f"#{self.featured_rooms_id} .room-card")
        return len(rooms)
    
    def is_recent_bookings_empty(self):
        """Check if recent bookings section is empty"""
        text = self.get_text("id", self.recent_bookings_id)
        return "no recent bookings" in text.lower() or "please log in" in text.lower()


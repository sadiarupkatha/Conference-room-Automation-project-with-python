"""
Test data constants
"""
from datetime import datetime, timedelta


class TestData:
    """Test data constants"""
    
    # User credentials
    VALID_USER = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123"
    }
    
    INVALID_EMAILS = [
        "invalid-email",
        "test@",
        "@example.com",
        "test@.com",
        "test@example",
        "test@example.",
    ]
    
    WEAK_PASSWORDS = [
        "12345",  # Less than 8 chars
        "abc",    # Too short
        "pass",   # Too short
    ]
    
    STRONG_PASSWORDS = [
        "password123",
        "SecurePass123!",
        "Test@1234",
    ]
    
    # Room data
    ROOM_CAPACITIES = [2, 5, 10, 20, 25]
    ROOM_FEATURES = [
        "projector",
        "whiteboard",
        "video-conferencing",
        "monitor",
        "teleconference",
        "sound-system"
    ]
    
    # Date/Time helpers
    @staticmethod
    def get_tomorrow_date():
        """Get tomorrow's date"""
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    @staticmethod
    def get_next_week_date():
        """Get next week's date"""
        return (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    @staticmethod
    def get_yesterday_date():
        """Get yesterday's date"""
        return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    @staticmethod
    def get_future_time(hours=1):
        """Get future time"""
        return (datetime.now() + timedelta(hours=hours)).strftime("%H:%M")
    
    @staticmethod
    def get_business_hours_time():
        """Get a time within business hours (10:00)"""
        return "10:00"
    
    @staticmethod
    def get_outside_business_hours_time():
        """Get a time outside business hours (7:00)"""
        return "07:00"
    
    # Meeting data
    MEETING_TITLES = [
        "Team Stand-up",
        "Client Presentation",
        "Project Planning",
        "Sprint Review",
        "Code Review"
    ]
    
    # Duration options (in minutes)
    DURATION_OPTIONS = [30, 60, 90, 120, 180, 240]
    
    # Invalid durations
    INVALID_DURATIONS = [
        (10, "Less than 15 minutes"),
        (300, "More than 4 hours"),
    ]


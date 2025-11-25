"""
Helper utility functions
"""
from datetime import datetime, timedelta
import re


def get_future_date(days_ahead=1):
    """Get future date string in YYYY-MM-DD format"""
    future_date = datetime.now() + timedelta(days=days_ahead)
    return future_date.strftime("%Y-%m-%d")


def get_past_date(days_ago=1):
    """Get past date string in YYYY-MM-DD format"""
    past_date = datetime.now() - timedelta(days=days_ago)
    return past_date.strftime("%Y-%m-%d")


def get_future_time(hours_ahead=1):
    """Get future time string in HH:MM format"""
    future_time = datetime.now() + timedelta(hours=hours_ahead)
    return future_time.strftime("%H:%M")


def calculate_end_time(start_time, duration_minutes):
    """Calculate end time from start time and duration"""
    time_obj = datetime.strptime(start_time, "%H:%M")
    end_time_obj = time_obj + timedelta(minutes=duration_minutes)
    return end_time_obj.strftime("%H:%M")


def is_valid_email(email):
    """Validate email format"""
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(pattern, email) is not None


def is_corporate_email(email):
    """Check if email is from corporate domain (not gmail, yahoo, etc.)"""
    corporate_domains = ['example.com', 'company.com', 'corp.com']
    personal_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    
    domain = email.split('@')[1].lower() if '@' in email else ''
    
    if domain in personal_domains:
        return False
    return True


def is_weak_password(password):
    """Check if password is weak (less than 8 characters)"""
    return len(password) < 8


def is_business_hours(time_str):
    """Check if time is within business hours (8 AM - 6 PM)"""
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    business_start = datetime.strptime("08:00", "%H:%M").time()
    business_end = datetime.strptime("18:00", "%H:%M").time()
    return business_start <= time_obj <= business_end


def is_valid_duration(start_time, end_time):
    """Check if duration is valid (15 minutes to 4 hours)"""
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    
    if end <= start:
        return False, "End time must be after start time"
    
    duration = (end - start).total_seconds() / 60  # Duration in minutes
    
    if duration < 15:
        return False, "Duration must be at least 15 minutes"
    
    if duration > 240:  # 4 hours
        return False, "Duration cannot exceed 4 hours"
    
    return True, "Valid duration"


def generate_test_email(prefix="test"):
    """Generate unique test email"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}_{timestamp}@example.com"


def wait_for_ajax(driver, timeout=10):
    """Wait for AJAX calls to complete"""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return jQuery.active == 0")
        )
    except:
        pass  # jQuery might not be available


def extract_number_from_text(text):
    """Extract first number from text"""
    match = re.search(r'\d+', text)
    return int(match.group()) if match else 0


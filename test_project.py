import pytest
from project import validate_email, validate_name, calculate_win_rate


def test_validate_email():
    # Valid emails
    assert validate_email("user@example.com") == True
    
    # Invalid emails
    assert validate_email("invalid") == False
    assert validate_email("@example.com") == False


def test_validate_name():
    # Valid names
    assert validate_name("Tasnimul") == True
    assert validate_name("David Malan") == True
    
    # Invalid names
    assert validate_name("") == False
    assert validate_name("   ") == False


def test_calculate_win_rate():
    # Normal cases
    assert calculate_win_rate(5, 10) == 50.0
    assert calculate_win_rate(0, 10) == 0.0
    
    # Edge cases
    assert calculate_win_rate(0, 0) == 0.0
    assert calculate_win_rate(5, 0) == 0.0
    
    # Negative cases 
    assert calculate_win_rate(0, -5) == 0.0


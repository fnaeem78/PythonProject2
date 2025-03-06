import pytest
from main import custom_decorator

# Sample function to apply the decorator to
def sample_function():
    return {"message": "Test"}

def test_custom_decorator_true():
    """Test that the decorator modifies the response when condition is True."""
    decorated_function = custom_decorator(condition=True)(sample_function)
    response = decorated_function()
    assert "decorated" in response
    assert response["decorated"] is True

def test_custom_decorator_false():
    """Test that the decorator does not modify the response when condition is False."""
    decorated_function = custom_decorator(condition=False)(sample_function)
    response = decorated_function()
    assert "decorated" not in response

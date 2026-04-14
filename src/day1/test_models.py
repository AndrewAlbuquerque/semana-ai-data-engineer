import pytest
from pydantic import ValidationError
from src.day1.models import Customer
from uuid import uuid4

def test_customer_invalid_email():
    with pytest.raises(ValidationError) as excinfo:
        Customer(
            customer_id=uuid4(),
            name="Test User",
            email="invalid-email",
            segment="premium"
        )
    assert "value is not a valid email address" in str(excinfo.value)

def test_customer_invalid_segment():
    with pytest.raises(ValidationError) as excinfo:
        Customer(
            customer_id=uuid4(),
            name="Test User",
            email="test@example.com",
            segment="invalid-segment"
        )
    assert "Input should be 'premium', 'standard' or 'basic'" in str(excinfo.value)

def test_customer_valid():
    customer = Customer(
        customer_id=uuid4(),
        name="Test User",
        email="test@example.com",
        segment="premium",
        state="SP"
    )
    assert customer.name == "Test User"
    assert customer.segment == "premium"

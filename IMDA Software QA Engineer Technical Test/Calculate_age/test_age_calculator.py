import pytest
from age_calculator import calculate_age

def test_valid_input():
    name = "John"
    dob = "12"
    month = "5"
    age = "30"
    result = calculate_age(name, dob, month, age)
    assert result == "John's age is 29 years or 348 months or 10620 days"

def test_invalid_name():
    name = "123"
    dob = "12"
    month = "5"
    age = "30"
    with pytest.raises(ValueError):
        calculate_age(name, dob, month, age)

def test_invalid_day():
    name = "John"
    dob = "45"
    month = "5"
    age = "30"
    with pytest.raises(ValueError):
        calculate_age(name, dob, month, age)

def test_invalid_month():
    name = "John"
    dob = "12"
    month = "15"
    age = "30"
    with pytest.raises(ValueError):
        calculate_age(name, dob, month, age)

def test_invalid_age():
    name = "John"
    dob = "12"
    month = "5"
    age = "thirty"
    with pytest.raises(ValueError):
        calculate_age(name, dob, month, age)

def test_leap_year():
    name = "John"
    dob = "29"
    month = "2"
    age = "30"
    result = calculate_age(name, dob, month, age)
    assert result == "John's age is 28 years or 336 months or 10224 days"

if __name__ == "__main__":
    pytest.main()
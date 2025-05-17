import pytest

@pytest.fixture(scope="function")
def login_credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }
@pytest.fixture(scope="function")
def product_names():
    return [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]
@pytest.fixture(scope="function")
def checkout_info():
    return {
        "first_name": "Fabian",
        "last_name": "Fabian",
        "postal_code": "007"
    }
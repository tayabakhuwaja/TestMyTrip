import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from pages.register_page import RegisterPage  # Import the RegisterPage class

@pytest.fixture
def driver():
    service = Service("chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Helper to generate unique emails
def generate_email():
    return f"test{random.randint(1000,9999)}@gmail.com"

# Test Case 1: Successful Registration
def test_register_success(driver):
    register_page = RegisterPage(driver)
    register_page.open("http://localhost:8000/register.php")

    # Fill in registration form
    register_page.fill_form(
        fullname="Test User",
        email="testuser@example.com",
        password="password123",
        contact="1234567890",
        address="Test Address"
    )
    register_page.submit_form()

    time.sleep(2)
    assert "register.php" in driver.current_url, "Registration may have failed"
    print("✅ Registration successful")

# Test Case 2: Missing Fields
def test_register_missing_fields(driver):
    register_page = RegisterPage(driver)
    register_page.open("http://localhost:8000/register.php")

    register_page.fill_form(
        fullname="",
        email="",
        password="",
        contact="",
        address=""
    )
    register_page.submit_form()

    time.sleep(2)
    print("Registration failed as expected for missing fields")

# Test Case 3: Invalid Email
def test_register_invalid_email(driver):
    register_page = RegisterPage(driver)
    register_page.open("http://localhost/tourz/register.php")

    register_page.fill_form(
        fullname="Zeeshan Ali",
        email="invalidemail",
        password="pass123",
        contact="03123456789",
        address="Lahore"
    )
    register_page.submit_form()

    time.sleep(2)
    print("Registration failed as expected for invalid email format")

# Test Case 4: Invalid Phone Number
def test_register_invalid_phone(driver):
    register_page = RegisterPage(driver)
    register_page.open("http://localhost/tourz/register.php")

    register_page.fill_form(
        fullname="Hassan Raza",
        email=generate_email(),
        password="pass123",
        contact="abc123",  # Invalid
        address="Karachi"
    )
    register_page.submit_form()

    time.sleep(2)
    print("Registration failed as expected for invalid phone number")

# Test Case 5: Duplicate Email
def test_register_duplicate_email(driver):
    register_page = RegisterPage(driver)
    
    duplicate_email = "duplicate@gmail.com"

    # First registration with the duplicate email
    register_page.open("http://localhost/tourz/register.php")
    register_page.fill_form(
        fullname="Test User 1",
        email=duplicate_email,
        password="testpass123",
        contact="03112223333",
        address="Peshawar"
    )
    register_page.submit_form()
    time.sleep(3)

    # Try registering again with the same email
    register_page.open("http://localhost/tourz/register.php")
    register_page.fill_form(
        fullname="Test User 2",
        email=duplicate_email,
        password="testpass456",
        contact="03223334444",
        address="Peshawar"
    )
    register_page.submit_form()

    time.sleep(2)
    print("Duplicate email registration failed as expected")


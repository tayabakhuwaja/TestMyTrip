import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
import time
from pages.empty_registerform import EmptyRegisterPage

def test_register_without_email():
    driver = webdriver.Chrome()
    register = EmptyRegisterPage(driver)

    register.open("http://localhost:8000/register.php")

    # Fill the form without email
    register.fill_form(
        fullname="Test User",
        email="",  # <-- Email left empty
        password="password123",
        contact="1234567890",
        address="123 Street Name"
    )

    register.submit_form()
    time.sleep(2)

    if "register.php" in driver.current_url:
        print("Registration failed as expected due to missing email.")
    else:
        print("Unexpected behavior: redirected despite missing email.")

    driver.quit()

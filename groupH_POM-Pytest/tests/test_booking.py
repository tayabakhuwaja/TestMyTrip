import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.booking_page import BookingPage

@pytest.fixture
def driver():
    service = Service("chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_booking_form(driver):
    booking = BookingPage(driver)
    booking.load()

    booking.fill_booking_form(
        name="zarah hassan",
        email="zarah@gmail.com",
        phone="03001234567",
        address="saddar, Karachi",
        location="Hunza Valley",
        guests="2",
        adate="05/01/2025",
        ldate="05/26/2025"
    )

    booking.submit()
    time.sleep(3)

    assert booking.is_redirected_to_payment(), "Booking failed or did not redirect to payment page."

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.empty_bookingform import EmptyBookingPage

def test_booking_without_location():
    driver = webdriver.Chrome()
    booking_page = EmptyBookingPage(driver)

    booking_page.load()
    booking_page.fill_booking_form(
        name="John Doe",
        email="johndoe@example.com",
        phone="1234567890",
        address="123 Test St",
        guests="2",
        adate="2025-05-01",
        ldate="2025-05-10"
    )
    booking_page.submit()

    if booking_page.is_redirected_to_payment():
        print("Booking successful and redirected to payment page.")
    else:
        print("Booking failed or redirection issue.")

    driver.quit()

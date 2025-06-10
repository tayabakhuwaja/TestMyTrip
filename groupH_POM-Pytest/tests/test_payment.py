import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
import time
from pages.payment_page import PaymentPage

def test_valid_payment():
    driver = webdriver.Chrome()
    payment = PaymentPage(driver)
    try:
        payment.load()
        payment.enter_card_details("4242424242424242", "12/25", "123")
        payment.submit_payment()
        time.sleep(3)
        assert payment.is_payment_successful(), "❌ Payment failed or redirection issue."
        print("✅ Valid payment succeeded.")
    finally:
        driver.quit()

def test_invalid_cvv():
    driver = webdriver.Chrome()
    payment = PaymentPage(driver)
    try:
        payment.load()
        payment.enter_card_details("4242424242424242", "12/25", "12")
        payment.submit_payment()
        time.sleep(2)
        assert not payment.is_field_valid("cvv"), "❌ Invalid CVV should be rejected."
        print("✅ Invalid CVV test passed.")
    finally:
        driver.quit()

def test_missing_card_number():
    driver = webdriver.Chrome()
    payment = PaymentPage(driver)
    try:
        payment.load()
        payment.enter_card_details("", "12/25", "123")
        payment.submit_payment()
        time.sleep(2)
        assert not payment.is_field_valid("cardNumber"), "❌ Missing card number should be invalid."
        print("✅ Missing card number test passed.")
    finally:
        driver.quit()

def test_expired_card():
    driver = webdriver.Chrome()
    payment = PaymentPage(driver)
    try:
        payment.load()
        payment.enter_card_details("4242424242424242", "01/20", "123")
        payment.submit_payment()
        time.sleep(2)
        assert not payment.validate_form_script(), "❌ Expired date should fail validation."
        print("✅ Expired card test passed.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_payment()
    test_invalid_cvv()
    test_missing_card_number()
    test_expired_card()

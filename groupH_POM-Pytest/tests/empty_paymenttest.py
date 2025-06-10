import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
import time
from pages.empty_paymentform import EmptyPaymentPage

def test_submit_empty_payment_form():
    driver = webdriver.Chrome()
    page = EmptyPaymentPage(driver)

    page.load()
    page.submit_form_empty()

    time.sleep(3)
    if "ordersuccess.php" in driver.current_url:
        print("❌ Form submitted even with empty fields. Validation missing.")
    else:
        print("✅ Validation works. Form not submitted with empty fields.")
    
    time.sleep(2)
    driver.quit()

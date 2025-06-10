#!/usr/bin/env python
# coding: utf-8

# In[61]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def test_valid_payment():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/pay.php?totalAmount=1000")
    
    driver.find_element(By.ID, "cardNumber").send_keys("4242424242424242")  # Valid Card Number
    driver.find_element(By.ID, "expirationDate").send_keys("12/25")  # Valid Expiry Date
    driver.find_element(By.ID, "cvv").send_keys("123")  # Valid CVV
    
    driver.find_element(By.NAME, "Paybttn").click()
    
    time.sleep(3)
    
    assert "ordersuccess.php" in driver.current_url, "❌ Payment simulation failed or redirection did not occur"
    
    print("✅ Valid payment simulated successfully. Redirected to ordersuccess page.")
    driver.quit()
    
def test_invalid_cvv():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/pay.php?totalAmount=1000")

    driver.find_element(By.ID, "cardNumber").send_keys("4242424242424242")
    driver.find_element(By.ID, "expirationDate").send_keys("12/25")
    driver.find_element(By.ID, "cvv").send_keys("12")  # Invalid CVV

# Attempt form submission
    driver.find_element(By.NAME, "Paybttn").click()
    time.sleep(3)
# Use JS to check if CVV is valid
    cvv_valid = driver.execute_script("return document.getElementById('cvv').checkValidity();")

    assert not cvv_valid, "❌ CVV input should be invalid"
    print("✅ Invalid CVV prevented form submission as expected.")
    
    driver.quit()
  

def test_missing_card_details():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/pay.php?totalAmount=1000")

    # Leave cardNumber blank
    driver.find_element(By.ID, "expirationDate").send_keys("12/25")
    driver.find_element(By.ID, "cvv").send_keys("123")

    # Try to submit form
    driver.find_element(By.NAME, "Paybttn").click()
    time.sleep(2)

    # Check if the cardNumber input is valid using JS
    is_valid = driver.execute_script("return document.getElementById('cardNumber').checkValidity();")
    assert not is_valid, "❌ Card number field should be marked as invalid"

    print("✅ Browser correctly prevented form submission due to missing card number.")
    driver.quit()

    
def test_expired_card():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/pay.php?totalAmount=1000")
    
    driver.find_element(By.ID, "cardNumber").send_keys("4242424242424242")  # Valid Card Number
    driver.find_element(By.ID, "expirationDate").send_keys("01/20")  # Expired Expiry Date
    driver.find_element(By.ID, "cvv").send_keys("123")  # Valid CVV
    
    driver.find_element(By.NAME, "Paybttn").click()
    
    time.sleep(3)
    
    is_valid = driver.execute_script("return validateForm();")
    assert not is_valid, "❌ Expiration date should be marked invalid (expired)"
    print("✅ Browser correctly flagged expired card.")


    driver.quit()
    
test_valid_payment()
test_invalid_cvv()
test_missing_card_details()
test_expired_card()


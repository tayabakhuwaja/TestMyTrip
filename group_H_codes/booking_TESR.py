#!/usr/bin/env python
# coding: utf-8

# In[38]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ✅ Test Case 1: Successful Booking
def test_booking_success():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/book.php")

    driver.find_element(By.NAME, "name").send_keys("Zarah Hassan")
    driver.find_element(By.NAME, "email").send_keys("zarah@gmail.com")
    driver.find_element(By.NAME, "phone").send_keys("03001234567")
    driver.find_element(By.NAME, "address").send_keys("Saddar, Karachi")
    driver.find_element(By.NAME, "location").send_keys("Hunza Valley")
    driver.find_element(By.NAME, "guests").send_keys("2")
    driver.find_element(By.NAME, "adate").send_keys("05/01/2025")
    driver.find_element(By.NAME, "ldate").send_keys("05/26/2025")
    driver.find_element(By.NAME, "send").click()

    time.sleep(3)
    assert "pay.php" in driver.current_url, "❌ Booking failed or not redirected"
    print("✅ Booking successful and redirected to payment page")
    driver.quit()

# ❌ Test Case 2: Missing Required Fields
def test_booking_missing_fields():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/book.php")

    driver.find_element(By.NAME, "name").send_keys("")  # Name missing
    driver.find_element(By.NAME, "email").send_keys("")
    driver.find_element(By.NAME, "phone").send_keys("03001234567")
    driver.find_element(By.NAME, "address").send_keys("Karachi")
    driver.find_element(By.NAME, "location").send_keys("Skardu")
    driver.find_element(By.NAME, "guests").send_keys("2")
    driver.find_element(By.NAME, "adate").send_keys("05/01/2025")
    driver.find_element(By.NAME, "ldate").send_keys("05/10/2025")
    driver.find_element(By.NAME, "send").click()

    time.sleep(3)
    assert "pay.php" not in driver.current_url, "❌ Booking should fail due to missing required fields"
    print("✅ Booking failed as expected for missing fields")
    driver.quit()

# ❌ Test Case 3: Invalid Guest Number
def test_booking_invalid_guest_number():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/book.php")

    driver.find_element(By.NAME, "name").send_keys("Ali Khan")
    driver.find_element(By.NAME, "email").send_keys("ali@example.com")
    driver.find_element(By.NAME, "phone").send_keys("03123456789")
    driver.find_element(By.NAME, "address").send_keys("Lahore")
    driver.find_element(By.NAME, "location").send_keys("Fairy Meadows")
    driver.find_element(By.NAME, "guests").send_keys("-1")  # Invalid
    driver.find_element(By.NAME, "adate").send_keys("05/01/2025")
    driver.find_element(By.NAME, "ldate").send_keys("05/05/2025")
    driver.find_element(By.NAME, "send").click()

    time.sleep(3)
    assert "pay.php" not in driver.current_url, "❌ Booking should fail due to invalid guest number"
    print("✅ Booking failed as expected for invalid guest number")
    driver.quit()
    
    

def test_booking_past_date():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/book.php")

    try:
        # Fill the form with past date for arrival
        driver.find_element(By.NAME, "name").send_keys("Zarah Hassan")
        driver.find_element(By.NAME, "email").send_keys("zarah@gmail.com")
        driver.find_element(By.NAME, "phone").send_keys("03001234567")
        driver.find_element(By.NAME, "address").send_keys("Karachi")
        driver.find_element(By.NAME, "location").send_keys("Karachi")
        driver.find_element(By.NAME, "guests").send_keys("2")

        # Get the current date and use a past date for testing
        driver.find_element(By.NAME, "adate").send_keys("01/01/2020")  # past date
        driver.find_element(By.NAME, "ldate").send_keys("01/07/2020")

        # Submit the form
        driver.find_element(By.NAME, "send").click()

        # Handle unexpected alert (if any) that may appear
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert Text: {alert_text}")  # Print the alert message
            assert "Arrival date must be greater than the current date" in alert_text, "❌ Unexpected alert text."
            alert.accept()  # Accept the alert
        except UnexpectedAlertPresentException:
            print("❌ Unexpected alert present")

        time.sleep(2)  # Allow some time for the alert to be processed

        print("✅ Booking form correctly rejected due to past date.")
        
    except NoSuchElementException:
        print("❌ Error message for past date not found.")
    
    finally:
        driver.quit()




# ✅ Run all tests
test_booking_success()
test_booking_missing_fields()
test_booking_invalid_guest_number()
test_booking_past_date()


# In[ ]:





# In[ ]:





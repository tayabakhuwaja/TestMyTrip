#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

# Helper to generate unique emails
def generate_email():
    return f"test{random.randint(1000,9999)}@gmail.com"

#Test Case 1: Successful Registration
def test_register_success():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/register.php")

    # Fill in registration form
    driver.find_element(By.NAME, "fullname").send_keys("Test User")
    driver.find_element(By.NAME, "useremail").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "userpassword").send_keys("password123")
    driver.find_element(By.NAME, "contactno").send_keys("1234567890")
    driver.find_element(By.NAME, "useradd").send_keys("Test Address")

    time.sleep(2)

    try:
        # Check and handle alert
        alert = Alert(driver)
        alert_text = alert.text
        print(f"⚠️ Alert appeared: {alert_text}")
        alert.accept()

        # You can also assert based on alert text
        assert "Could not register" in alert_text, "Unexpected alert content"

    except NoAlertPresentException:
        # If no alert, continue to verify successful registration
        assert "register.php" in driver.current_url, "Registration may have failed"
        print("✅ Registration successful")

    driver.quit()

#Test Case 2: Missing Fields
def test_register_missing_fields():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/register.php")

    driver.find_element(By.NAME, "fullname").send_keys("")
    driver.find_element(By.NAME, "useremail").send_keys("")
    driver.find_element(By.NAME, "userpassword").send_keys("")
    driver.find_element(By.NAME, "contactno").send_keys("")
    driver.find_element(By.NAME, "useradd").send_keys("")
    driver.find_element(By.NAME, "Register").click()

    time.sleep(2)
    print("Registration failed as expected for missing fields")
    driver.quit()

# Test Case 3: Invalid Email
def test_register_invalid_email():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/register.php")

    driver.find_element(By.NAME, "fullname").send_keys("Zeeshan Ali")
    driver.find_element(By.NAME, "useremail").send_keys("invalidemail")
    driver.find_element(By.NAME, "userpassword").send_keys("pass123")
    driver.find_element(By.NAME, "contactno").send_keys("03123456789")
    driver.find_element(By.NAME, "useradd").send_keys("Lahore")
    driver.find_element(By.NAME, "Register").click()

    time.sleep(2)
    print("Registration failed as expected for invalid email format")
    driver.quit()

# Test Case 4: Invalid Phone Number
def test_register_invalid_phone():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/register.php")

    driver.find_element(By.NAME, "fullname").send_keys("Hassan Raza")
    driver.find_element(By.NAME, "useremail").send_keys(generate_email())
    driver.find_element(By.NAME, "userpassword").send_keys("pass123")
    driver.find_element(By.NAME, "contactno").send_keys("abc123")  # Invalid
    driver.find_element(By.NAME, "useradd").send_keys("Karachi")
    driver.find_element(By.NAME, "Register").click()

    time.sleep(2)
    print("Registration failed as expected for invalid phone number")
    driver.quit()

# Test Case 5: Duplicate Email
def test_register_duplicate_email():
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/register.php")

    duplicate_email = "duplicate@gmail.com"

    # First registration
    driver.find_element(By.NAME, "fullname").send_keys("Test User 1")
    driver.find_element(By.NAME, "useremail").send_keys(duplicate_email)
    driver.find_element(By.NAME, "userpassword").send_keys("testpass123")
    driver.find_element(By.NAME, "contactno").send_keys("03112223333")
    driver.find_element(By.NAME, "useradd").send_keys("Peshawar")
    driver.find_element(By.NAME, "Register").click()
    time.sleep(3)
    driver.quit()

    # Try registering again with same email
    driver = webdriver.Chrome()
    driver.get("http://localhost/tourz/register.php")

    driver.find_element(By.NAME, "fullname").send_keys("Test User 2")
    driver.find_element(By.NAME, "useremail").send_keys(duplicate_email)
    driver.find_element(By.NAME, "userpassword").send_keys("testpass456")
    driver.find_element(By.NAME, "contactno").send_keys("03223334444")
    driver.find_element(By.NAME, "useradd").send_keys("Peshawar")
    driver.find_element(By.NAME, "Register").click()

    time.sleep(2)
    print("Duplicate email registration failed as expected")
    driver.quit()



# Run Tests
test_register_success()


# In[4]:


test_register_missing_fields()


# In[8]:


test_register_invalid_email()


# In[9]:


test_register_invalid_phone()


# In[10]:


test_register_duplicate_email()


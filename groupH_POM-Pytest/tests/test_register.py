import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.fullname_input = (By.NAME, "fullname")
        self.email_input = (By.NAME, "useremail")
        self.password_input = (By.NAME, "userpassword")
        self.contact_input = (By.NAME, "contactno")
        self.address_input = (By.NAME, "useradd")
        self.register_button = (By.NAME, "Register")

    def open(self, url):
        self.driver.get(url)

    def fill_form(self, fullname, email, password, contact, address):
        self.driver.find_element(*self.fullname_input).send_keys(fullname)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.contact_input).send_keys(contact)
        self.driver.find_element(*self.address_input).send_keys(address)

    def submit_form(self):
        self.driver.find_element(*self.register_button).click()

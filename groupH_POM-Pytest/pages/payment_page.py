from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:8000/pay.php?totalAmount=1000"
        self.card_number_input = (By.ID, "cardNumber")
        self.expiration_date_input = (By.ID, "expirationDate")
        self.cvv_input = (By.ID, "cvv")
        self.pay_button = (By.NAME, "Paybttn")
    
    def load(self):
        self.driver.get(self.url)

    def enter_card_details(self, card_number="", expiration_date="", cvv=""):
        if card_number:
            self.driver.find_element(*self.card_number_input).send_keys(card_number)
        if expiration_date:
            self.driver.find_element(*self.expiration_date_input).send_keys(expiration_date)
        if cvv:
            self.driver.find_element(*self.cvv_input).send_keys(cvv)

    def submit_payment(self):
        self.driver.find_element(*self.pay_button).click()

    def is_payment_successful(self):
        return "ordersuccess.php" in self.driver.current_url

    def is_field_valid(self, field_id):
        return self.driver.execute_script(f"return document.getElementById('{field_id}').checkValidity();")

    def validate_form_script(self):
        return self.driver.execute_script("return validateForm();")

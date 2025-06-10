from selenium.webdriver.common.by import By

class EmptyPaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:8000/pay.php?totalAmount=1000"
        self.card_number_input = (By.ID, "cardNumber")
        self.expiration_input = (By.ID, "expirationDate")
        self.cvv_input = (By.ID, "cvv")
        self.pay_button = (By.NAME, "Paybttn")

    def load(self):
        self.driver.get(self.url)

    def submit_form_empty(self):
        # Click Pay without filling anything
        self.driver.find_element(*self.pay_button).click()

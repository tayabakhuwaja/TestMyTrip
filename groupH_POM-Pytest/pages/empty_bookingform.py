from selenium.webdriver.common.by import By

class EmptyBookingPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://localhost:8000/book.php")

    def fill_booking_form(self, name, email, phone, address, guests, adate, ldate):
        self.driver.find_element(By.NAME, "name").send_keys(name)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        # Location is omitted to submit the form without it
        self.driver.find_element(By.NAME, "guests").send_keys(guests)
        self.driver.find_element(By.NAME, "adate").send_keys(adate)
        self.driver.find_element(By.NAME, "ldate").send_keys(ldate)

    def submit(self):
        self.driver.find_element(By.NAME, "send").click()

    def is_redirected_to_payment(self):
        return "pay.php" in self.driver.current_url

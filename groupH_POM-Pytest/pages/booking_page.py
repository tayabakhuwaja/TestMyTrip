from selenium.webdriver.common.by import By

class BookingPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        # Open the booking page
        self.driver.get("http://localhost:8000/book.php")

    def fill_booking_form(self, name, email, phone, address, location, guests, adate, ldate):
        # Fill the booking form fields
        self.driver.find_element(By.NAME, "name").clear()
        self.driver.find_element(By.NAME, "name").send_keys(name)

        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)

        self.driver.find_element(By.NAME, "phone").clear()
        self.driver.find_element(By.NAME, "phone").send_keys(phone)

        self.driver.find_element(By.NAME, "address").clear()
        self.driver.find_element(By.NAME, "address").send_keys(address)

        self.driver.find_element(By.NAME, "location").clear()
        self.driver.find_element(By.NAME, "location").send_keys(location)

        self.driver.find_element(By.NAME, "guests").clear()
        self.driver.find_element(By.NAME, "guests").send_keys(guests)

        self.driver.find_element(By.NAME, "adate").clear()
        self.driver.find_element(By.NAME, "adate").send_keys(adate)

        self.driver.find_element(By.NAME, "ldate").clear()
        self.driver.find_element(By.NAME, "ldate").send_keys(ldate)

    def submit(self):
        # Submit the form
        self.driver.find_element(By.NAME, "send").click()

    def is_redirected_to_payment(self):
        # Check if redirected to payment page
        return "pay.php" in self.driver.current_url

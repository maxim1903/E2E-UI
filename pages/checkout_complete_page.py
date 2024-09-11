from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.confirmation_message_locator = (By.CSS_SELECTOR, ".complete-header")

    def verify_order_complete(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.confirmation_message_locator)
            )
            confirmation_message_element = self.driver.find_element(*self.confirmation_message_locator)
            print("Page text:", confirmation_message_element.text)  

            return "Thank you for your order!" in confirmation_message_element.text
        except Exception as e:
            print("Exception occurred:", str(e))  
            return False

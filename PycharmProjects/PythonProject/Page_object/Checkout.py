from selenium.webdriver.common.by import By


class Check_out:
    def __init__(self,driver):
        self.driver = driver
        self.checkout = (By.CSS_SELECTOR,".checkout-button")

    def check_btn(self):
        self.driver.find_element(*self.checkout).click()
from selenium.webdriver.common.by import By


class Login_page:

    def __init__(self,driver):
        self.driver = driver
        self.textbox_username = (By.CSS_SELECTOR,".email")
        self.textbox_pwd = (By.CSS_SELECTOR,".password")
        self.checkbox_agree = (By.XPATH,"//input[@type='checkbox']")
        self.button_login = (By.CSS_SELECTOR,".login-button")

    def user_name(self,username):
        self.driver.find_element(*self.textbox_username).clear()
        self.driver.find_element(*self.textbox_username).send_keys(username)

    def password(self,password):
        self.driver.find_element(*self.textbox_pwd).clear()
        self.driver.find_element(*self.textbox_pwd).send_keys(password)

    def agree(self):
        self.driver.find_element(*self.checkbox_agree).click()

    def click_login(self):
        self.driver.find_element(*self.button_login).click()
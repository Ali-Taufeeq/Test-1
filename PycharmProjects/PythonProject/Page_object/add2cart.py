from selenium.webdriver.common.by import By

from Config.conftest import browserInstance

class Add2cart:
    def __init__(self,driver):
        self.driver = driver
        self.cart1 = (By.XPATH,"//*[@id='main']/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/button[1]")
        self.cart2 = (By.XPATH,"//*[@id='main']/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[4]/div/div[2]/div[3]/div[2]/button[1]")
        self.cart3 = (By.XPATH,"//*[@id='main']/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[5]/div/div[2]/div[3]/div[2]/button[1]")

def button_1(self):
    self.driver.find_element(*self.cart1).click()

def button_2(self):
    self.driver.find_element(*self.cart2).click()

def button_3(self):
    self.driver.find_element(*self.cart3).click()



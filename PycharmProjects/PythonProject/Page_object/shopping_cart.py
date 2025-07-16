from selenium import webdriver
from selenium.webdriver.common.by import By

from E2E_framework import driver


class Shopping_cart:
    def __init__(self,driver):
        self.driver = driver
        self.Scart = (By.LINK_TEXT,"Shopping cart")

    def cart(self):
        self.driver.find_element(*self.Scart).click()

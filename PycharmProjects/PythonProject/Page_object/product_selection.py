from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from E2E_framework import driver

class Electronic:
    def __init__(self,driver):
        self.driver = driver
        self.photo = (By.XPATH,"//*[@id='main']/div/div/div/div/div[3]/div/div[1]/div/div/a/img")

    def click_electronics_photo(self):
        self.driver.find_element(*self.photo).click()


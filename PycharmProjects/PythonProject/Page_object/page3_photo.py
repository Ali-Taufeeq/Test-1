from selenium.webdriver.common.by import By


class Page3:
    def __init__(self,driver):
        self.driver = driver
        self.page_3 = (By.CSS_SELECTOR,"#main > div > div.center-2 > div > div.page-body > div.category-grid.sub-category-grid > div > div:nth-child(2) > div > div > a")

    def page3(self):
        self.driver.find_element(*self.page_3).click()

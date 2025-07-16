from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.find_element(By.LINK_TEXT, "Shop").click()

    wait = WebDriverWait(driver, 15)
    products = driver.find_elements(By.ID, "row")
    for product in products:
        Product_name = product.find_element(By.XPATH, "//h4[@class='card-title']").text
        if Product_name == "Blackberry":
            driver.find_element(By.XPATH,
                                "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[4]/div/div[2]/button").click()

    driver.find_element(By.XPATH, "//*[@id='navbarResponsive']/ul/li/a").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in successText
    driver.close()

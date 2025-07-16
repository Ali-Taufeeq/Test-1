import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

#page 1:
driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("rahulshettyacademy") # I.D
driver.find_element(By.NAME,"password").send_keys("learning")
driver.find_element(By.NAME,"terms").click()
driver.find_element(By.CSS_SELECTOR,".btn-md").click()

#page 2:
driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[2]/div/div[2]/button").click()
driver.find_element(By.CSS_SELECTOR,"body > app-root > app-shop > div > div > div.col-lg-9 > app-card-list > app-card:nth-child(1) > div > div.card-footer > button").click()
driver.find_element(By.CSS_SELECTOR,"body > app-root > app-shop > div > div > div.col-lg-9 > app-card-list > app-card:nth-child(4) > div > div.card-footer > button").click()

wait= WebDriverWait(driver,5)
try:
    failure = wait.until(EC.until(visibility_of_element_located(By.XPATH,'//*[@id="username"]')))
    print(failure.text)
except:
    pass
driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click() #checkout

try:
    alert= driver.switch_to.alert
    alert_text = alert.text
    print(alert.text)
    alert.accept()
except:
    pass

#page 3: Checkout button
driver.find_element(By.CSS_SELECTOR,".btn-success").click()

# Page 4:

# send "Ind"
driver.find_element(By.XPATH,"//*[@id='country']").click()
driver.find_element(By.XPATH,"//*[@id='country']").send_keys("Ind")
# Wait for "Select Country" input
wait = WebDriverWait(driver,15)
country_input = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India"))) # India ka naam aagaya
driver.find_element(By.PARTIAL_LINK_TEXT,"India").click() # India select kr diya

# Complete order
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success.btn-lg").click()
wait = WebDriverWait(driver,10)
Purchase = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-dismissible")))
print(Purchase.text)
driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")

# Initialize the Edge WebDriver with the service object
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.LINK_TEXT,"Shop").click()

mobilelist  = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(mobilelist)
for mobile in mobilelist:
    mobile_text = mobile.find_element(By.TAG_NAME,"h4").text
    print(mobile_text)
    if mobile_text == "Blackberry":
        mobile.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//td/button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("India")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
# print(driver.find_element(By.XPATH,"//a[@xpath='1']"))

driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successmessage = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(successmessage)



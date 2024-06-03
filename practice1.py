import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")

# Initialize the Edge WebDriver with the service object
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME,"blinkingText").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])

text = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
list = text.split()
# print(list)
word = []
for i in list:
    if ".com" in i:
        word.append(i)
print(word)

driver.close()
driver.switch_to.window(windowsopened[0])
driver.find_element(By.NAME,"username").send_keys(word)
driver.find_element(By.NAME,"password").send_keys("Rahulshetty")
# driver.find_element(By.XPATH,"//span[@xpath='1']").click()
driver.find_element(By.NAME,"terms").click()
driver.find_element(By.NAME,"signin").click()
time.sleep(3)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))
alert =driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(alert)
assert alert  == "Incorrect username/password."

time.sleep(5)



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver import ActionChains,Keys
# Specify the path to the Edge driver
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")

# Initialize the Edge WebDriver with the service object
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()

driver.get('https://testpages.eviltester.com/styled/index.html')
driver.find_element(By.LINK_TEXT,"Calculator").click()

windowopened = driver.window_handles

driver.switch_to.window(windowopened[0])
print(driver.find_element(By.TAG_NAME,"h1").text)
driver.back()
print(driver.find_element(By.TAG_NAME,"h1").text)


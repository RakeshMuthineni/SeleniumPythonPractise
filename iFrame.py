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

driver.get("https://www.google.com/recaptcha/api2/demo")
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']"))
driver.find_element(By.CLASS_NAME,"recaptcha-checkbox-border").click()

time.sleep(4)
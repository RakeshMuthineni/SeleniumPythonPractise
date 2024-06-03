import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win64\msedgedriver.exe")


driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("Maheshbabu@11")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("Maheshbabu@11")
driver.find_element(By.XPATH,"//button[@type='submit']").click()






time.sleep(10)
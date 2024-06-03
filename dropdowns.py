import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.service import Service


service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
country = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(country))

for i in country:
    if i.text == "India":
        i.click()
        break
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"





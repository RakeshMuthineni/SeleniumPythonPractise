import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")

# Initialize the Edge WebDriver with the service object
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
browsersortedlist = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on header

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
# collect all veg list after browsersortedlist

vegelements = driver.find_elements(By.XPATH,"//tr/td[1]")
for vegtext in vegelements:
    browsersortedlist.append(vegtext.text)

orginalbrowsersortedlist = browsersortedlist.copy()
print(orginalbrowsersortedlist)

# sort the list by python using sort method
browsersortedlist.sort()
print("its python sorted list",browsersortedlist)
assert browsersortedlist == orginalbrowsersortedlist


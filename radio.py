import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkbox))
for i in checkbox:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break



# Radio button
radio = driver.find_elements(By.XPATH,"//input[@type='radio']")

print(len(radio))

for i in radio:
    if i.get_attribute("value") == "radio2":
        i.click()
        assert i.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()


time.sleep(5)
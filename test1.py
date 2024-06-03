import time

# import BY as BY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win64\msedgedriver.exe")

driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("rakesmuthineni9@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("qwerasdfzxcv")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rakesh Varma")

# select dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

message = driver.find_element(By.CLASS_NAME,"alert-success").text



print(message)
assert "success" in message
# driver.find_element(By.CLASS_NAME,"")


time.sleep(10)
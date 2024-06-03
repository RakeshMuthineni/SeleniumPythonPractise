import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")

# Initialize the Edge WebDriver with the service object
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")

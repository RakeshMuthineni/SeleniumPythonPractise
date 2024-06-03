import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

Service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=Service_obj)
driver.get("https://www.instagram.com/")

# driver = webdriver.Firefox()
# driver.get("https://www.ultimatix.net/uxportal/uxportalhome.html/Megamenu")

time.sleep(5)

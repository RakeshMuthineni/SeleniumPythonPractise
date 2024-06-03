import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)


driver.get("http://the-internet.herokuapp.com/drag_and_drop")



time.sleep(3)
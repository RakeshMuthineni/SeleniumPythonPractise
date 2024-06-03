
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

# Correct the method name to implicitly_wait
driver.implicitly_wait(10)

# Open the specified URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
wait = WebDriverWait(driver,10)

# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()



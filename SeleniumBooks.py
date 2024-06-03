import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--start-maximized")


service_obj = Service(r"C:\Users\Rakesh\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)


driver.get("https://practice.automationtesting.in/")
driver.find_element(By.LINK_TEXT,"Shop").click()
driver.execute_script("window.scrollBy(0,300);")
dropdown_elements = driver.find_element(By.XPATH,"//select[@class='orderby']")
select = Select(dropdown_elements)
select.select_by_visible_text("Sort by price: low to high")
driver.execute_script("window.scrollBy(0,500);")
BookElements = driver.find_elements(By.XPATH,"//li/a")
print(BookElements)

for books in BookElements:
    wait = WebDriverWait(driver,10)
    element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//h3[text()='JS Data Structures and Algorithm']")))
    element.click()
print("somthing")

# print(driver.find_element(By.TAG_NAME,"h1").text)








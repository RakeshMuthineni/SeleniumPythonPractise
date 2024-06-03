import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expected_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]


service_obj = Service(r"C:\Users\Rakesh\Dropbox\My PC (LAPTOP-S31RKO9R)\Documents\edgedriver_win65\msedgedriver.exe")

driver = webdriver.Edge(service=service_obj)
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")


time.sleep(3)
length = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(length)
count = len(length)

assert count> 0
resultList = []

for i in length:
    k =i.find_element(By.XPATH,'h4').text
    resultList.append(k)
    i.find_element(By.XPATH,'div/button').click()
assert expected_list == resultList


driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for i in prices:
    sum = sum+ int(i.text)
print(sum)


totalAmount = int(driver.find_element(By.CLASS_NAME,"totAmt").text)

assert sum == totalAmount
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

totcost = driver.find_element(By.CLASS_NAME,"totAmt").text
print(totcost)
totcostAfterDiscount = driver.find_element(By.CLASS_NAME,"discountAmt").text
print(totcostAfterDiscount)

assert totcost>totcostAfterDiscount

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(3)


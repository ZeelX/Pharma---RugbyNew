from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome("")
driver.get("http://localhost:8000/")

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h4")
element = element.text

list_road = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[2]/a")
list_road.click()
time.sleep(2)
last_page = driver.find_element(By.XPATH, "/html/body/div/div/a[2]")
last_page.click()
time.sleep(2)

td = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[5]")
td_element = td.text

f = open("logs.txt", "a")
f.write(element+"\n"+td_element + "\n")
f.close()
driver.close()
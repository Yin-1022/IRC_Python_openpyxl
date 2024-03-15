from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
data = driver.get('https://zh.wikipedia.org/wiki/兰顿蚂蚁')
print(driver.title)

name = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')
print(name.text)
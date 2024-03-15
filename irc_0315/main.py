from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', value=True)

driver = webdriver.Chrome(options=chrome_options)

data = driver.get('https://popcat.click')

Click = driver.find_element(By.XPATH, '//*[@id="app"]/div')

for i in range(100):
    Click.click();
    time.sleep(1);


# Texas = driver.find_element(By.XPATH, '//*[@id="column-feature"]/p/a[1]')
# Texas.click()
# print(driver.title)
# name = driver.find_element(By.XPATH, '//*[@id="firstHeading"]/span[1]')
# print(name.text)

# next = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]/a[3]')
# next.click()

# keyword = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input')
# keyword.click()
# keyword.send_keys('USA')
# Search = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button')
# Search.click()

# data = driver.get('https://zh.wikipedia.org/wiki/Wikipedia:首页')

# element = driver.find_element_by_class_name("//*[@id="searchform"]/div/div/div[1]/input")
# element.send_keys("Selenium Python")

# print(driver.title)

# name = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')
# print(name.text)
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', value=True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://github.com/Lichyo?tab=repositories')
the_cube = driver.find_element(By.CLASS_NAME, 'wb-break-all')
the_cube.click()
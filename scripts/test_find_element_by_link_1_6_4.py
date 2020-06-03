from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

a = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"

try:

    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.LINK_TEXT, a).click()
    time.sleep(5)
    input1 = driver.find_element(By.TAG_NAME, '.form-group:nth-child(1) input')
    input1.send_keys("Ihor")
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Voitkiv")
    input3 = driver.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Lviv")
    input4 = driver.find_element(By.ID, 'country')
    input4.send_keys("UA")
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    driver.quit()

#
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/alert_accept.html")
    driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
    driver.switch_to.alert.accept()
    x_element = driver.find_element(By.ID,'input_value')
    x = x_element.text
    y = calc(x)
    driver.find_element(By.ID,'answer').send_keys(y)
    driver.find_element(By.CSS_SELECTOR,'.btn.btn-primary').click()
    time.sleep(5)

finally:
    driver.quit()

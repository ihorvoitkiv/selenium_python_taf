from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    x_element  = driver.find_element(By.CSS_SELECTOR,'span#input_value')
    x = x_element.text
    y = calc(x)
    input_field = driver.find_element(By.ID,'answer').send_keys(y)
    radio_btn = driver.find_element(By.ID,'robotCheckbox').click()
    check_box = driver.find_element(By.ID,'robotsRule').click()
    submit = driver.find_element(By.CSS_SELECTOR,'form[method="get"] > .btn.btn-default').click()

finally:
    driver.quit()

#




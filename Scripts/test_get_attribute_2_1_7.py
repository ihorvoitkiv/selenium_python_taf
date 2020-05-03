from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import  time


link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    img  = driver.find_element(By.CSS_SELECTOR,'img#treasure')
    x = img.get_attribute("valuex")
    y = calc(x)
    input_field = driver.find_element(By.ID, 'answer').send_keys(y)
    radio_btn = driver.find_element(By.ID, 'robotCheckbox').click()
    check_box = driver.find_element(By.ID, 'robotsRule').click()
    submit = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    time.sleep(5)

finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/execute_script.html")
    x_element = driver.find_element(By.ID,'input_value')
    x = x_element.text
    y = calc(x)
    driver.find_element(By.CSS_SELECTOR,'input#answer').send_keys(y)
    checkbox = driver.find_element(By.ID,'robotCheckbox')
    driver.execute_script("return arguments[0].scrollIntoView({block : 'center'});", checkbox)
    checkbox.click()
    radio_btn = driver.find_element(By.ID,'robotsRule')
    driver.execute_script("window.scrollBy(0,100);")
    #driver.execute_script("return arguments[0].scrollIntoView({block : 'center'});", radio_btn)
    #gust display alert:
    #driver.execute_script("alert('Robots at work');")
    radio_btn.click()
    driver.find_element(By.CSS_SELECTOR,'.btn.btn-primary').click()
    time.sleep(5)

finally:
    driver.quit()

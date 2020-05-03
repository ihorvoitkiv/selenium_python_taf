from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(driver,15).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100')
    )
    button = driver.find_element(By.ID,'book').click()
    number = driver.find_element_by_css_selector("#input_value")
    x = number.text
    y = calc(x)
    input = driver.find_element_by_css_selector("input#answer")
    input.send_keys(y)
    submit = driver.find_element_by_css_selector("button#solve")
    submit.click()
    time.sleep(5)

finally:
    driver.quit()

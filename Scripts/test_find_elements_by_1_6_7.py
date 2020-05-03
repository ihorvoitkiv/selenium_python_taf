from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.CSS_SELECTOR,'input[type="text"]')
    for element in elements:
        element.send_keys("data")
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

finally:
    time.sleep(5)
    driver.quit()

#


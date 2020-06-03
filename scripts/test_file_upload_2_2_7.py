from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/file_input.html")
    driver.find_element(By.NAME,'firstname').send_keys('Ihor')
    driver.find_element(By.NAME, 'lastname').send_keys('Voitkiv')
    driver.find_element(By.NAME, 'email').send_keys('iv@gmail.com')
    #path to the file in current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # path to the file in the current file
    # current_dir = (os.path.abspath(__file__))
    file_path = os.path.join(current_dir,'file.txt')
    driver.find_element(By.ID,'file').send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR,'.btn.btn-primary').click()
    time.sleep(5)

finally:
    driver.quit()
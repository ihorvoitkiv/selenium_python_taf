from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")
    a = driver.find_element(By.ID,'num1')
    n1 = a.text
    b = driver.find_element(By.ID,'num2')
    n2 = b.text
    summ = int(n1) + int(n2)
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))
    driver.find_element(By.CSS_SELECTOR,'form > .btn.btn-default')
    time.sleep(5)

finally:
    driver.quit()

#
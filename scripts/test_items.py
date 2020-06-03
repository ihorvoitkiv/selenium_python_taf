from selenium.webdriver.common.by import By
import time

def test_add2basket_button(browser):

    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207")
    time.sleep(5)
    btn_element = browser.find_element(By.CSS_SELECTOR,'button.btn-add-to-basket')
    assert btn_element.is_displayed(), "add to basket button is not displayed"

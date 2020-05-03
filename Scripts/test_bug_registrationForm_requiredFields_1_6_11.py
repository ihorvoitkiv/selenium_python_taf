from selenium import webdriver
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element_by_css_selector(".first_block .first")
    fn.send_keys("Ihor")
    sn = browser.find_element_by_css_selector(".first_block .second")
    sn.send_keys("Voitkiv")
    email = browser.find_element_by_css_selector(".form-control.third")
    email.send_keys("iv@gmail.com")
    btn = browser.find_element_by_css_selector(".btn-default")
    btn.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

    #close browser
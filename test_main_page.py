from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_url(driver):
    test_guest_can_go_to_login_page(driver)
    page = LoginPage(driver, link)
    page.should_be_login_url()

def test_guest_should_see_login_form(driver):
    test_guest_can_go_to_login_page(driver)
    page = LoginPage(driver, link)
    page.should_be_login_form()

def test_guest_should_see_register_form(driver):
    test_guest_can_go_to_login_page(driver)
    page = LoginPage(driver,link)
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver,link)
    page.open()
    page.should_enter_basket()
    page2 = BasketPage(driver, driver.current_url)
    page2.if_basket_is_empty()
    page2.if_message_in_empty_basket()



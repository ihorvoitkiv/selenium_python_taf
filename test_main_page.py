from .pages.main_page import MainPage
from .pages.login_page import LoginPage

url = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,url)
    page.open()
    #login_page = page.go_to_login_page()
    #login_page.should_be_login_url()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_url(browser):
    test_guest_can_go_to_login_page(browser)
    page = LoginPage(browser, url)
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    test_guest_can_go_to_login_page(browser)
    page = LoginPage(browser, url)
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    test_guest_can_go_to_login_page(browser)
    page = LoginPage(browser,url)
    page.should_be_register_form()
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,url)
    page.open()
    page.go_to_login_page()
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random
import time

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="offer is missed")
@pytest.mark.parametrize('n',["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6","offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(driver,n):
    link = f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo={n}'
    product_page = ProductPage(driver,link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.book_name_equal()
    product_page.book_price_equal()

@pytest.mark.xfail(reason="wrong message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.is_dissappeared()

def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(driver,link)
    product_page.open()
    product_page.add_to_basket()
    product_page2 = BasketPage(driver, driver.current_url)
    product_page2.if_basket_is_empty()
    product_page2.if_message_in_empty_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(driver, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)

    def test_user_cant_see_success_message(self,driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(driver, link)
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, driver):
        link = f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207'
        self.product_page = ProductPage(driver, link)
        self.product_page.open()
        self.product_page.add_to_basket()
        #self.product_page.solve_quiz_and_get_code()
        self.product_page.book_name_equal()
        self.product_page.book_price_equal()
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random
import time

base_url = "http://selenium1py.pythonanywhere.com/"
product_link = f"{base_url}catalogue/coders-at-work_207/"
login_link = f"{base_url}en-gb/accounts/login/"

def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, product_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, product_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="offer is missed")
@pytest.mark.parametrize('n',["offer0", "offer1", "offer2", "offer3", "offer4", "offer5","offer6","offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(driver,n):
    link = f'{product_link}?promo={n}'
    product_page = ProductPage(driver,link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.book_name_equal()
    product_page.book_price_equal()

@pytest.mark.xfail(reason="wrong message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    product_page = ProductPage(driver, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    product_page = ProductPage(driver, product_link)
    product_page.open()
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(driver):
    product_page = ProductPage(driver, product_link)
    product_page.open()
    product_page.is_dissappeared()

def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    product_page = ProductPage(driver,product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page2 = BasketPage(driver, driver.current_url)
    product_page2.if_basket_is_empty()
    product_page2.if_message_in_empty_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver, login_link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)

    def test_user_cant_see_success_message(self,driver):
        self.product_page = ProductPage(driver, product_link)
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, driver):
        self.product_page = ProductPage(driver, product_link)
        self.product_page.open()
        self.product_page.add_to_basket()
        #self.product_page.solve_quiz_and_get_code()
        self.product_page.book_name_equal()
        self.product_page.book_price_equal()
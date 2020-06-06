from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "button element is not present"
        basket_btn = self.driver.find_element(*ProductPageLocators.ADD_BUTTON)
        basket_btn.click()

    def book_price_equal(self):
        book_price = self.driver.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_basket = self.driver.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert book_price == book_price_basket, "Book price at the basket page is not equal at the product page"

    def book_name_equal(self):
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_basket = self.driver.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_name_basket, "Book name at the basket page is not equal at the product page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
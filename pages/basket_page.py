from pages.locators import BasketPageLocators
from pages.base_page import BasePage

class BasketPage(BasePage):
    def if_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), 'Basket is NOT empty'

    def if_message_in_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Basket is not empty'

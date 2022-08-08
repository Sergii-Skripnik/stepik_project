from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def shouldnt_be_price_in_the_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LINK_DISPLAYS_PRICE), "The basket is not empty"
    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_BASKET_IS_EMPTY), "The message is not display"





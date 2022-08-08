from .locators import ProductPageLocators
from .base_page import BasePage




class ProductPage(BasePage):
    def go_to_product_page(self):
        Add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        Add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_message_of_adding_book_to_the_basket(self):
        book_in_the_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_OF_ADDING_THE_BOOK)
        book_name = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK)
        assert book_in_the_basket.text == book_name.text, "The book is not in the basket"

    def should_be_price_of_book_add_to_the_basket(self):
        price_of_the_book_in_the_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_OF_TOTAL_PRICE_IN_BASKET)
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_BOOK)
        assert price_of_the_book_in_the_basket.text == price_book.text, "The price is not correct"

    def shouldnt_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_OF_ADDING_THE_BOOK), "The book is in the basket"

    def shouldnt_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_OF_ADDING_THE_BOOK), "The book is in the basket"

    def should_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_OF_ADDING_THE_BOOK), "The book is not disappeared from thebasket"











import pytest as pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks = pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket (browser, offer):
    link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_product_page()
    page.should_be_message_of_adding_book_to_the_basket()
    page.should_be_price_of_book_add_to_the_basket()

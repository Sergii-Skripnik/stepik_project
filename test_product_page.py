import pytest as pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.shouldnt_see_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('offer',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    page.go_to_product_page()
    page.should_be_message_of_adding_book_to_the_basket()
    page.should_be_price_of_book_add_to_the_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #Открываем страницу товара
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasePage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.go_to_product_page()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.shouldnt_see_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    #Открываем страницу товара
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.go_to_product_page()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    # открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    #проверяем наличие на странице линка на логин и регистрацию
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # проверяем наличие на странице линка на логин/регистрацию
    page.should_be_login_link()
    #переходим на страницу логина/регистрации
    page.go_to_login_page()
    #проверяем наличие: слова login в url/формы логина на странице/формы регистрации на странице
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    #Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    #Ожидаем, что в корзине нет товаров
    page.shouldnt_be_price_in_the_basket()
    #Ожидаем, что есть текст о том что корзина пуста
    page.should_be_message_that_basket_is_empty()

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #открыть страницу регистрации;
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        # проверяем наличие на странице линка на логин/регистрацию
        page.should_be_login_link()
        # переходим на страницу логина/регистрации
        page.go_to_login_page()
        #зарегистрировать нового пользователя;
        page.register_new_user()
        #проверить, что пользователь залогинен.
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.shouldnt_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        # открываем страницу
        page.open()
        # добавляем товар в корзину и переходим на страницу товара
        page.go_to_product_page()
        # проверка наличия сообщения о добавлении товара в корзину
        page.should_be_message_of_adding_book_to_the_basket()
        # проверка добавления цены товра в корзину
        page.should_be_price_of_book_add_to_the_basket()



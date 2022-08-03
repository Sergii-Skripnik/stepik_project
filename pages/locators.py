from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_OF_ADDING_THE_BOOK = (By.XPATH, '(//div[@class="alertinner "]/strong)[1]')
    NAME_OF_THE_BOOK = (By.TAG_NAME, 'h1')
    MESSAGE_OF_TOTAL_PRICE_IN_BASKET = (By.XPATH, '//div[@class = "alertinner "]/p/strong')
    PRICE_OF_THE_BOOK = (By.CSS_SELECTOR, 'p.price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")




from selenium.webdriver.common.by import By


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
    BASKET_LINK = (By.XPATH, "//a[@class = 'btn btn-default']")
    BASKET_LINK_DISPLAYS_PRICE = (By.XPATH, "(//p[@class = 'price_color align-right'])[2]")
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, "// div[ @ id = 'content_inner']/p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    EMAIL_ADDRESS_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")






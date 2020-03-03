from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS_II = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages div:first-child")
    TITLE = (By.CSS_SELECTOR, ".product_main :first-child")
    ALERT_TITLE = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner :nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_CONTENT = (By.CSS_SELECTOR, "div.row h2.h3")
    HEADER = (By.CSS_SELECTOR, ".page-header")

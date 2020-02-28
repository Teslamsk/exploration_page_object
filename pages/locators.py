from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")


class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages div:first-child")
    TITLE = (By.CSS_SELECTOR, ".product_main :first-child")
    ALERT_TITLE = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner :nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")

from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class ProductPage(BasePage):
    # Описать в нем метод для добавления в корзину.
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def should_be_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Error: Success messages not found."

    def title_are_the_same(self):
        title_text = self.browser.find_element(*ProductPageLocators.TITLE).text
        alert_title_text = self.browser.find_element(*ProductPageLocators.ALERT_TITLE).text
        assert title_text == alert_title_text, f"Error: Title text ({title_text}) are not the same like in " \
                                               f"success message ({alert_title_text})."

    def price_are_the_same(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        price = float(price.replace('£', ''))
        alert_price = float(alert_price.replace('£', ''))
        assert price == alert_price, f"Error: Price ({price}) are not the same like in " \
                                     f"alert price ({alert_price})."




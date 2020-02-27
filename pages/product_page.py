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
        # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        # ассерт что имя книги во всплывающем окне == в заголовке товара
        title_text = self.browser.find_element(*ProductPageLocators.TITLE).text
        alert_title_text = self.browser.find_element(*ProductPageLocators.ALERT_TITLE).text
        # price = int(self.browser.find_element(*ProductPageLocators.PRICE).text)
        # alert_price = int(self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text)
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Error: Success messages not found."
        assert title_text == alert_title_text, f"Error: Title text ({title_text}) are not the same like in " \
                                               f"success message ({alert_title_text})."
        # assert price == alert_price, f"Error: Price ({price}) are not the same like in " \
        #                              f"alert price ({alert_price})."




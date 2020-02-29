from .base_page import BasePage
from .locators import BasketPageLocators

# Создайте файл basket_page.py и в нем класс BasketPage. Реализуйте там необходимые проверки, в том числе
# отрицательную, которую мы обсуждали в предыдущих шагах.


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT)

    def should_be_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT)

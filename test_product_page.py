import math
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

from selenium.common.exceptions import NoAlertPresentException # в начале файла


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()




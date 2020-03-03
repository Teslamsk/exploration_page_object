import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):




    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(int(time.time()))
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_II)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"



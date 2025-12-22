import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.text import Text


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'Title')
        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str):
        self.title.check_visible()
        self.title.check_have_text('UI Course')

        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.text import Text


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'Title')
        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def check_visible(self, email: str, password: str):
        self.title.check_visible()
        self.title.check_have_text('UI Course')

        self.email_input.check_visible()
        self.email_input.check_have_text(email)

        self.password_input.check_visible()
        self.password_input.check_have_text(password)

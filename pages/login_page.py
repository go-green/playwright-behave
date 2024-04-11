"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""
import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.ui_controls.px_button import PxButton
from pages.ui_controls.px_input import PxInput


class LoginPage(BasePage):

    def user_name(self) -> PxInput: return PxInput(self.page, "input[name='login']")

    def password(self) -> PxInput: return PxInput(self.page, "input[name='password']")

    def login_button(self) -> PxButton: return PxButton(self.page, button="Sign in")

    def __init__(self, page: Page):
        super().__init__(page)

    def verify_page(self) -> bool:
        self.user_name().is_ready()
        self.password().is_ready()
        self.login_button().is_ready()
        return True

    def navigate(self, base_url: str) -> None:
        self.goto(base_url, "/")

    def login(self, organization: str, user_name: str, password: str) -> None:
        with allure.step(f"Login to Trademe web portal as user: {user_name}'"):
            self.organization().fill(organization)
            self.user_name().fill(user_name)
            self.password().fill(password)
            self.login_button().click()


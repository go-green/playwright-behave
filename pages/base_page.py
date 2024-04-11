"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""

from abc import abstractmethod, ABC

import allure
from playwright.sync_api import Page


class BasePage(ABC):

    def __init__(self, page: Page):
        self.page: Page = page

    @abstractmethod
    def verify_page(self) -> bool:
        pass

    def delete_cookies(self) -> None :
        self.page.context.clear_cookies()

    def reload(self) -> None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until="domcontentloaded")

    def goto(self, base_url: str, path: str) -> None:
        with allure.step(f'Opening the url "{base_url}{path}"'):
            self.page.goto(f"{base_url}{path}", wait_until="networkidle")

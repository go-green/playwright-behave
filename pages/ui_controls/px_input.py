"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""

from playwright.sync_api import Page, Locator

from pages.ui_controls.page_component import PageComponent


class PxInput(PageComponent):

    def __init__(self, page: Page, selector: str = None, parents: list[Locator] = None, **kwargs):
        super().__init__(page, selector, parents, **kwargs)

    @property
    def type_of(self) -> str:
        return "PxInput"

    def fill(self, text: str) -> str:
        self.element.scroll_into_view_if_needed()
        self.element.fill(text)

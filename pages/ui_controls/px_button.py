"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""

from playwright.sync_api import Page

from pages.ui_controls.page_component import PageComponent


class PxButton(PageComponent):

    def __init__(self, page: Page, selector: str = None, parents: list[str] = None, **kwargs):
        super().__init__(page, selector, parents, **kwargs)

    @property
    def type_of(self) -> str:
        return "PxButton"

    def click(self) -> None:
        self.element.scroll_into_view_if_needed()
        self.element.click()

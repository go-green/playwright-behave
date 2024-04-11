"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""

from abc import ABC, abstractmethod

from playwright.sync_api import Page, Locator, expect


class PageComponent(ABC):

    def __init__(self, page: Page, selector: str = None, selectors: list[str] = None, **kwargs):
        self.element: Locator = None
        self.page: Page = page
        self.selector: str = selector
        self.selectors: list[str] = selectors
        self.kwargs = kwargs
        self.init_element()

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'page_component'

    def init_element(self) -> None:
        if self.selector is None and self.selectors is not None:
            tmp_element: Locator = None
            tmp_element = self.page.locator(self.selectors[0])
            self.page.locator()
            # Skip the first element (1:) as it has already been used to find the parent element above
            for parent in self.selectors[1:]:
                tmp_element = tmp_element.locator(parent)
            self.element = tmp_element
        elif self.selectors is None and self.selector is not None:
            self.element = self.page.locator(self.selector)
        elif "label" in self.kwargs:
            self.element = self.page.get_by_label(self.kwargs.get("label"))
        elif "placeholder" in self.kwargs:
            self.element = self.page.get_by_placeholder(self.kwargs.get("placeholder"))
        elif "text" in self.kwargs:
            self.element = self.page.get_by_text(self.kwargs.get("text"))
        elif bool(self.kwargs) is True:
            for key, value in self.kwargs.items():
                self.element = self.page.get_by_role(key, name=value)
                break
        else:
            raise Exception(f"Element selector or selectors not defined. Please enter arguments: 'selector=<str>',  "
                            f"'selectors=<list[str]>', label, place_holder, text or role")

    def is_ready(self) -> None:
        expect(self.element).to_be_in_viewport()
        expect(self.element).to_be_visible()
        expect(self.element).to_be_enabled()

    def focus(self) -> None:
        self.element.focus()

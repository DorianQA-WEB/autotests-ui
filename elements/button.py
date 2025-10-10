from elements.base_element import BaseElement
from playwright.sync_api import expect


class Button(BaseElement):
    def check_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).not_to_be_enabled()

    def check_disabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).not_to_be_disabled()


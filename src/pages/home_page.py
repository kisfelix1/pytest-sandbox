from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        self.page = page
        components = {
            "compare search": self.page.locator("llg-cta-button.submit")
        }
        super().__init__(page, components)

class BasePage:
    def __init__(self, page, components=None):
        self.page = page
        self.components = components or {}

    async def go_to_page(self):
        await self.page.goto(self.url)

    async  def navigate(self, url):
        if not url.startswith("http") and not url.startswith("https"):
            raise ValueError("URL must start with http or https")
        await self.page.goto(url)

    async def click_on_element(self, selector):
        if selector not in self.components:
            raise ValueError(f"Selector '{selector}' not found in components")
        element = self.components[selector]
        return element.click()

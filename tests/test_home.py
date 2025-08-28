import pytest
from src.pages.home_page import HomePage
from playwright.async_api import Page


@pytest.mark.anyio
async def test_home_page_loads(page: Page):
    home_page = HomePage(page)
    await home_page.navigate("https://www.liligo.fr")
    await home_page.click_on_element("compare search")

@pytest.mark.anyio
@pytest.mark.regression
async def test_home_page_loads(page: Page):
    home_page = HomePage(page)
    await home_page.navigate("https://www.google.com")

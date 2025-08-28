import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from typing import AsyncGenerator



@pytest.fixture(scope="module")
async def browser() -> AsyncGenerator[Browser, None]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()

@pytest.fixture(scope="function")
async def context(browser: Browser) -> AsyncGenerator[BrowserContext, None]:
    context = await browser.new_context()
    yield context
    await context.close()

@pytest.fixture(scope="function")
async def page(context: BrowserContext) -> AsyncGenerator[Page, None]:
    page = await context.new_page()
    yield page
    await page.close()

@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"
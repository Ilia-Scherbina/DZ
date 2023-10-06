from typing import Dict, Callable, Generator

import pytest
from playwright.async_api import Page, BrowserType, Browser
from pytest_playwright.pytest_playwright import artifacts_folder

@pytest.fixture(scope='function')
def viewport_width():
    return 1920
@pytest.fixture(scope='function')
def viewport_height():
    return 1080
@pytest.fixture(scope='function')
def ru_page(browser, viewport_width: int, viewport_height: int) -> Page:
    new_context = browser.new_context(locale='ru-RU')
    r_page = new_context.new_page()
    vs = {'width': viewport_width, 'height': viewport_height}
    r_page.set_viewport_size(viewport_size=vs)
    yield r_page
    r_page.close()

@pytest.fixture(scope="session")
def launch_browser(
    browser_type_launch_args: Dict,
    browser_type: BrowserType,
) -> Callable[..., Browser]:
    def launch(**kwargs: Dict) -> Browser:
        launch_options = {**browser_type_launch_args, **kwargs}
        browser = browser_type.launch(**launch_options)
        return browser

    return launch


@pytest.fixture(scope="session")
def browser(launch_browser: Callable[[], Browser]) -> Generator[Browser, None, None]:
    browser = launch_browser()
    yield browser
    browser.close()
    artifacts_folder.cleanup()

from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(ru_page) -> None:
    page=ru_page

    page.goto("https://cloud.ru")
    page.locator("Header_menuItem__g6VzI header-mainMenu").page.locator("#__next > div > header > div.Header_headerBottom__T7xqO > div > nav > ul > li:nth-child(2)").click()
    page.locator("#scrollbar-products > div.ScrollbarsCustom-Wrapper > div > div > div > div:nth-child(1) > div > div:nth-child(1)").click()
    page.locator("#product-detail-NewHeroProduct-button-modal-Оставить\ заявку").click()
    page.wait_for_load_state("load")
    expect(page.get_by_text("Заявка на консультацию")).to_be_visible()








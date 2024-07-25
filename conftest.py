import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_settings():
        browser.config.base_url = "https://google.com"
        browser.config.window_width = 600
        browser.config.window_height = 800

        yield

        browser.quit()
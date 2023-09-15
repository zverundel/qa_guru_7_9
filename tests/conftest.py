from selene import browser
import pytest


@pytest.fixture
def browser_firefox_open():
    browser.config.driver_name = 'firefox'


@pytest.fixture
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def browser_open_url(browser_firefox_open, browser_size):
    browser.config.base_url = 'https://github.com'
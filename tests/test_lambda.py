import allure
from selene import be, browser, by


def test_github_decorator(browser_open_url):
    browser.open("/")

    with allure.step("Ввод поискового запроса"):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').should(be.blank).type('eroshenkoam/allure-example').press_enter()

    with allure.step("Выбор репозитория"):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Переход в issues"):
        browser.element('#issues-tab').click()

    with allure.step("Поиск задачи"):
        browser.element(by.partial_text('#74')).should(be.visible)
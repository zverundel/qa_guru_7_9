import allure
from selene import be, browser, by


@allure.step("Открываем главную страницу GitHub")
def open_github():
    browser.open('/')


@allure.step("Ввод поискового запроса")
def input_search():
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').should(be.blank).type('eroshenkoam/allure-example').press_enter()


@allure.step("Выбор репозитория")
def repository_selection():
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step("Переход в issues")
def go_to_issues():
    browser.element('#issues-tab').click()


@allure.step("Поиск задачи")
def search_task():
    browser.element(by.partial_text('#74')).should(be.visible)
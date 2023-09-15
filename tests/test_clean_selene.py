from selene import be, browser, by


def test_github_selene(browser_open_url):
    browser.open("/")
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').should(be.blank).type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#74')).should(be.visible)
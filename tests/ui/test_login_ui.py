from tests.ui.pages.login_page import LoginPage


def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.enter_username("student")
    page.enter_password("Password123")
    page.click_login()

    assert page.is_login_successful()


def test_login_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.enter_username("student")
    page.enter_password("WrongPassword")
    page.click_login()

    assert page.is_error_displayed()

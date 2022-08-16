from selenium import webdriver
from selenium.webdriver.common.by import By
from browsers.browser_factory import browserFactory


class SignInPage(object):

    def __init__(self) -> None:
        pass

    def email(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(By.ID, 'username')

    def password(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(By.ID, 'password')

    def sign_in(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(
            By.XPATH, '//button[@data-litms-control-urn="login-submit"]')

    def fillin_email(self, email) -> None:
        self.email().clear()
        self.email().send_keys(email)

    def fillin_password(self, password) -> None:
        self.password().clear()
        self.password().send_keys(password)

    def click_submit(self) -> None:
        self.sign_in().click()


signInPage = SignInPage()

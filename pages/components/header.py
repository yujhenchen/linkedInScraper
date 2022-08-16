from selenium import webdriver
from selenium.webdriver.common.by import By
from browsers.browser_factory import browserFactory


class Header(object):

    def __init__(self) -> None:
        pass

    def sign_in(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(
            By.XPATH,
            '//a[@data-tracking-control-name="public_jobs_nav-header-signin"]')

    def click_signin(self) -> None:
        self.sign_in().click()


header = Header()

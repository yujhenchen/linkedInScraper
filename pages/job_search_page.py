from selenium import webdriver
from selenium.webdriver.common.by import By
from browsers.browser_factory import browserFactory


class JobSearchPage(object):

    def __init__(self) -> None:
        pass

    def open(self) -> None:
        browserFactory.chrome_driver().get('https://www.linkedin.com/jobs')

    def keyword_input(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(By.NAME, 'keywords')

    def location_input(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(By.NAME, 'location')

    def search_submit(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(
            By.XPATH,
            '//button[@data-tracking-control-name="homepage-jobseeker_search-jobs-search-btn"]'
        )

    def sign_in(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(
            By.XPATH,
            '//a[@data-tracking-control-name="guest_homepage-jobseeker_nav-header-signin"]'
        )

    def click_signin(self) -> None:
        self.sign_in().click()

    def fillin_keyword(self, keyword) -> None:
        self.keyword_input().clear()
        self.keyword_input().send_keys(keyword)

    def fillin_location(self, location) -> None:
        self.location_input().clear()
        self.location_input().send_keys(location)

    def click_search_submit(self) -> None:
        self.search_submit().click()


jobSearchPage = JobSearchPage()

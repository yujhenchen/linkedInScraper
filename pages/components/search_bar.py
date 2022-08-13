from selenium import webdriver
from selenium.webdriver.common.by import By
from browsers.browser_factory import browserFactory


class SearchBar(object):

    def keyword_input(self) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(By.ID, '')

    def fillin_keyword(self, keyword) -> None:
        self.keyword_input().send_keys(keyword)


searchBar = SearchBar()

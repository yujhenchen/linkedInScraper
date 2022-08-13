from selenium import webdriver
from browsers.chrome import Chrome


class BrowserFactory(object):
    _chrome = None

    def __init__(self) -> None:
        super().__init__()
        self._chrome = Chrome()

    def chrome_driver(self) -> webdriver:
        return self._chrome.driver


# Create instance allow cross modules to use
browserFactory = BrowserFactory()

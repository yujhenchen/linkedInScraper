from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Chrome(object):

    def __init__(self) -> None:
        super().__init__()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

from pages.job_search_page import jobSearchPage
from pages.sign_in_page import signInPage
from pages.job_search_results_page import jobSearchResultsPage
from pages.components.header import header
from browsers.browser_factory import browserFactory
import pytest
from time import sleep
import random


def setup():
    browserFactory.chrome_driver().delete_all_cookies()


def test_search_signin_filter():
    # search
    jobSearchPage.open()
    jobSearchPage.fillin_keyword('selenium')
    jobSearchPage.fillin_location('Gothenburg, Vastra Gotaland County, Sweden')
    jobSearchPage.click_search_submit()

    header.click_signin()

    # signin
    signInPage.fillin_email('')
    sleep(random.randint(0, 2))
    signInPage.fillin_password('')
    sleep(random.randint(1, 3))
    signInPage.click_submit()

    # filter
    jobSearchResultsPage.job_filter.select_time(True, 'Month')
    # jobSearchResultsPage.job_filter.select_distance('100')
    # jobSearchResultsPage.job_filter.select_type('Full')

    sleep(10)
    # sleep(random.randint(4, 5))


def teardown():
    browserFactory.chrome_driver().delete_all_cookies()
    browserFactory.chrome_driver().quit()

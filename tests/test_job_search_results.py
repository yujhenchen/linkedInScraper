from pages.job_search_page import jobSearchPage
from pages.job_search_results_page import jobSearchResultsPage
from browsers.browser_factory import browserFactory
# import pytest
# from time import sleep


def setup_function():
    jobSearchPage.open()
    jobSearchPage.fillin_keyword('selenium')
    jobSearchPage.fillin_location('Gothenburg, Vastra Gotaland County, Sweden')
    jobSearchPage.click_search_submit()


def test_fillin_keyword_location_filter_time():
    jobSearchResultsPage.job_filter.select_time('Month')
    # sleep(5)


def test_fillin_keyword_location_filter_distance():
    jobSearchResultsPage.job_filter.select_distance('100')
    # sleep(5)


def test_fillin_keyword_location_filter_type():
    jobSearchResultsPage.job_filter.select_type('Full')
    # sleep(5)


def teardown_function():
    browserFactory.chrome_driver().delete_all_cookies()


def teardown():
    browserFactory.chrome_driver().quit()

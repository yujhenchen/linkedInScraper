from pages.job_search_page import jobSearchPage
from browsers.browser_factory import browserFactory
import pytest
from time import sleep


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_keyword_input():
    jobSearchPage.open()
    keyword_input = jobSearchPage.keyword_input()
    print(keyword_input.text)


@pytest.mark.skip(reason="no way of currently testing this")
def test_fillin_keyword():
    jobSearchPage.open()
    jobSearchPage.fillin_keyword('selenium')
    browserFactory.chrome_driver()
    # sleep(5)


@pytest.mark.skip(reason="no way of currently testing this")
def test_fillin_locationd():
    jobSearchPage.open()
    jobSearchPage.fillin_location('Gothenburg, Vastra Gotaland County, Sweden')
    # sleep(5)


def test_fillin_keyword_location_submit():
    jobSearchPage.open()
    jobSearchPage.fillin_keyword('selenium')
    jobSearchPage.fillin_location('Gothenburg, Vastra Gotaland County, Sweden')
    jobSearchPage.click_search_submit()
    sleep(5)


def teardown():
    browserFactory.chrome_driver().quit()

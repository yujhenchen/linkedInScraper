from selenium import webdriver
from selenium.webdriver.common.by import By
from browsers.browser_factory import browserFactory


class JobFilter(object):

    def __init__(self) -> None:
        pass

    def filter_element(self,
                       selector) -> webdriver.remote.webelement.WebElement:
        return browserFactory.chrome_driver().find_element(By.XPATH, selector)

    def filter_option(self,
                      optionText) -> webdriver.remote.webelement.WebElement:
        option_xpath = "//label[contains(text(), '{optionText}')]".format(
            optionText=optionText)
        return browserFactory.chrome_driver().find_element(
            By.XPATH, option_xpath)

    def filter_done(self,
                    filterAttribute) -> webdriver.remote.webelement.WebElement:
        done_xpath = "//button[@data-tracking-control-name='{filterAttribute}' and @type='submit']".format(
            filterAttribute=filterAttribute)
        return browserFactory.chrome_driver().find_element(
            By.XPATH, done_xpath)

    # actions
    def select_filter_option(self, control_name, optionText):
        selector = '//button[@data-tracking-control-name="{control_name}"]'.format(
            control_name=control_name)
        self.filter_element(selector).click()
        self.filter_option(optionText).click()
        self.filter_done(control_name).click()

    def select_time(self, postedTime) -> None:
        control_name = 'public_jobs_f_TPR'
        self.select_filter_option(control_name, postedTime)

    def select_distance(self, distance) -> None:
        control_name = 'public_jobs_distance'
        self.select_filter_option(control_name, distance)

    def select_type(self, jobType) -> None:
        control_name = 'public_jobs_f_JT'
        self.select_filter_option(control_name, jobType)


jobFilter = JobFilter()

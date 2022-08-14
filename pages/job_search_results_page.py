from pages.components.job_filter import jobFilter


class JobSearchResultsPage(object):

    def __init__(self) -> None:
        self.job_filter = jobFilter


jobSearchResultsPage = JobSearchResultsPage()
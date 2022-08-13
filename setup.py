from setuptools import setup

setup(name='linkedinscraper',
      version='0.1',
      author='yujhenchen',
      packages=['browsers', 'pages', 'scraper'],
      install_requires=['wheel', 'pytest', 'webdriver-manager', 'selenium'])

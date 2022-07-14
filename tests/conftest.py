import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():

    chrome_options = ChromiumOptions()
    
    chrome_options.add_experimental_option("w3c", True)
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--window-size=1920,1480")
    chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--allow-running-insecure-content")
    # chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-setuid-sandbox")
    print(os.environ)
    
    if os.environ['RUN_HEADLESS'] == 'True':
        chrome_options.add_argument("--headless")

    return chrome_options


@pytest.fixture
def get_webdriver(get_chrome_options):

    chrome_options = get_chrome_options
    # chromedriver = Service("/usr/local/bin/chromedriver")
    chromedriver = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chromedriver, options=chrome_options)
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver):
    driver = get_webdriver

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()

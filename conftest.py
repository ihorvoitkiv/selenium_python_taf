import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en")

@pytest.yield_fixture(scope='function')
def driver(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
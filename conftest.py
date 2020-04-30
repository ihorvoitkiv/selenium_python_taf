import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                     action='store', \
                     default='chrome', \
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', \
                     action='store', \
                     default='es', \
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart browser chrome for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart browser firefox for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Browser '{browser_name}' still is not implemented")
    yield browser
    print("\nquit browser...")
    browser.quit()







"""
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                    action ='store', \
                    default = "Chrome", \
                    help = "Choose browser: Chrome or Firefox")
    parser.addoption('--language', \
                    action = 'store', \
                    default = None, \
                    help = "Choose lenguage: eng,ua...etc")

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options
        options.add_experimental_option('prefs',\
                                        {'intl.accept_languages': user_language})
        print("\n start Chrome to test...")
        browser = webdriver.Chrome(options=options)
    elif (browser_name == "firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print("\n start Firefox to test...")
        browser = webdriver.firefox(firefox_profile=fp)
    else:
        print("Browser <browser_name> still is noy=t implemented")
    yield browser
    print("\nQuit the browser")
    browser.quit()
"""



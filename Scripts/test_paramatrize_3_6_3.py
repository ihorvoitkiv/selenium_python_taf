from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

def calc():
    return str(math.log(int(time.time())))

@pytest.fixture(scope='function')
def driver():
    print("/start browser for the test")
    driver = webdriver.Chrome()
    yield driver
    print("/close browser after test")
    driver.quit()

class TestParametrize():

    @pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_param1 (self, driver, id):
        driver.get(f'https://stepik.org/lesson/{id}/step/1')
        driver.implicitly_wait(10)
        input_field = driver.find_element(By.CSS_SELECTOR,'.string-quiz__textarea')
        answer = calc()
        input_field.send_keys(answer)
        driver.find_element(By.CSS_SELECTOR,'.submit-submission').click()
        option = driver.find_element(By.CSS_SELECTOR, ".hints__component_showed")
        """
        option = WebDriverWait(driver,5).until(
            EC.presence_of_element_located(By.CSS_SELECTOR,'.hints__component_showed')
        )
        """
        feedback = option.text
        assert feedback == "Correct!", f"expected 'Correct!', got '{feedback}'"



The project autotests are implemented using Selenium Webdriver+Python+Pytest+Allure Framework,
<br>based on a Page Object pattern for this <a href="http://selenium1py.pythonanywhere.com/en-gb/">Resource</a>: 

## Getting started

```
git clone https://github.com/ihorvoitkiv/WebUI_test_automation.git
cd WebUI_test_automation
python3 -m venv selenium_env
source selenium_env/bin/activate
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve ./allure-results
deactivate
```

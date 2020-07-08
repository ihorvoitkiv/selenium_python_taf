The project autotests are implemented using Selenium Webdriver+Python+Pytest+Allure Framework,
<br>based on a Page Object pattern for this <a href="http://selenium1py.pythonanywhere.com/en-gb/">Resource</a>: 

##Getting started

These instructions will get you a copy of the project up and running on your local machine for testing purposes:

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
Thanks,
<img src="https://camo.githubusercontent.com/0c7864cfef5de26e967d5ba390371727ce210880/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f68654958354866576745596c572f67697068792e676966">

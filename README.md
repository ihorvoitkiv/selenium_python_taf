The project autotests are implemented using SeleniumWebdriver+Python+Pytest+Allure Framework,
<br>based on a Page Object pattern for this <a href="http://selenium1py.pythonanywhere.com/en-gb/">Resource</a>

## Getting started

1. clone the project repository:
```
git clone https://github.com/ihorvoitkiv/WebUI_test_automation.git
cd WebUI_test_automation
```
2. create and activate a virtual environment:
```
python3 -m venv selenium_env
source selenium_env/bin/activate
```
3. install the requirements:
```
pip install -r requirements.txt
```
4. to enable Allure listener to collect results during the test execution simply add --alluredir option and provide path to the folder where results should be stored. E.g.:
```
pytest --alluredir=allure-results
```
5. to see the actual report after your tests have finished, you need to use Allure commandline utility to generate report from the results:
```
allure serve ./allure-results
```
6. deactivate a virtual environment:
```
deactivate
```

Thanks,

<img src="https://media3.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy-downsized.gif">

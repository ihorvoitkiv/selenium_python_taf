The project autotests are implemented using Selenium Webdriver+Python+Pytest+Allure Framework,
based on a Page Object pattern for this <a href="http://http://selenium1py.pythonanywhere.com/en-gb/">Resource</a>: 

#!/bin/bash
echo '#### Create Virtual Environment ####'
python3 -m venv selenium_env

echo '#### Activate Virtual Environment ####'
source selenium_env/bin/activate

echo '#### Install requirements ####'
pip install -r requirements.txt

echo '#### Run tests ####'
pytest --alluredir=allure-results

echo ### deactivate virtual environment ###
deactivate

Thanks,
<img src=“https://camo.githubusercontent.com/0c7864cfef5de26e967d5ba390371727ce210880/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f68654958354866576745596c572f67697068792e676966”>
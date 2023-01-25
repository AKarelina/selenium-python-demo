
#Automation
# python-selenium-demo

Automation demo framework using Selenium with PyTest. 

### technical stack
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![Selenium](https://img.shields.io/badge/selenium-4-blue.svg)]()


## Quick start:
* clone this repo to your local drive
```commandline
git clone https://github.com/AKarelina/selenium-python-demo
```
* create virtual env
```commandline
python -m venv venv
```
* activate virtual env
  * Windows
  ```commandline
  venv/Activate/script
  ```
  * MacOS/Linux
  ```commandline
  source venv/bin/activate
  ```
* install dependencies 
```commandline
pip install -r requirements.txt
```
* run tests
  * you can run all tests by below command
  ```commandline
  pytest
  ```
  * in example below only smoke tests will be run
  ```commandline
  pytest -k "smoke"



# Python-Selenium Test Automation: To automate browser based web testing using 
- Page Object Model Framework
- Pytest

## Required Packages
### Python3.x
### pip3
- ddt (1.4.1)
- pytest (5.4.2)
- pytest-html (2.1.1)
- pytest-ordering (0.6)
- selenium (3.141.0)

## Run test
`
command  
python -m py.test tests/test.py --browser chrome --html=./reports/report.html
`

### config.yml
- driver location is provided in config.yml
- base Url is provided in config.yml

### test_data
- test data for data driven testing is provided from data.csv file using ddt

### conftest
- One time setup
- take cares about creating driver instance and available throughout the test class
- take cares of browser instance that is passed from command line and available throughout the test session

### page_objects
- base page class inherits from custom selenium webdriver class
- each page class should inherit from base_page class


## Directory tree structure
python-selenium/  
├── config  
│   └── config.yml  
├── page_objects  
│   ├── base_page.py  
│   ├── __init__.py  
│   ├── login_page.py  
├── README.md  
├── reports  
│   ├── logs  
│   │   └── Automation  
│   └── report.html  
├── screenshots  
│   ├── Login Verified.1590141831530.png  
│   ├── Title Verified.1590141828298.png  
├── test_data  
│   └── data.csv  
├── tests  
│   ├── conftest.py  
│   ├── __init__.py  
│   └── test.py  
└── utilities 
    ├── __init__.py   
    ├── config_file_reader.py  
    ├── custom_logger.py   
    ├── read_data.py  
    ├── selenium_driver.py  
    ├── test_status.py  
    ├── util.py  
    └── webdriver_factory.py  


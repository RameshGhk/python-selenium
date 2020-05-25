"""
@package tests
user credentials are passed from data.csv with ddt
browserType is passed from command line arguments:
example:
python -m py.test tests/test.py --browser chrome
"""

from page_objects.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_test_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class GithubLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

        # to keep track of all assertions
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("test_data/data.csv"))
    @unpack
    def test_login(self, userName, password):
        self.lp.userLogin(userName, password)
        titleResult = self.lp.verifyTitle()
        self.ts.mark(titleResult, "Title Verified")
        loginResult = self.lp.verifyLogin()
        self.ts.markFinal("test_login", loginResult, "Login Verified")
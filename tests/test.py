from page_objects.login_page import LoginPage
import unittest
import pytest
import time

"""
@pending_task
parameterize user credentials
"""

@pytest.mark.usefixtures("oneTimeSetUp")
class GithubLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_Login(self):
        self.lp.userLogin("username", "password")
        time.sleep(5)
        result=self.lp.verifyLogin()
        assert result==True
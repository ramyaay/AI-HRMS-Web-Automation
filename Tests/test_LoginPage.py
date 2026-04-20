import time
import pytest
from Config.config import TestData
from WebPages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.LoginPage=LoginPage(self.driver)
        title = self.LoginPage.get_title("Login")
        assert "Login" in title

    def test_login(self):
        self.LoginPage=LoginPage(self.driver)
        time.sleep(3)
        self.LoginPage.do_login(TestData.EMAIL,TestData.PASSWORD)
        time.sleep(3)

    def test_logout(self):
        self.LoginPage=LoginPage(self.driver)
        self.LoginPage.do_logout()
        time.sleep(2)

    def test_default_login(self):
        self.LoginPage=LoginPage(self.driver)
        self.LoginPage.do_click(self.LoginPage.LOGIN_BUTTON)
        time.sleep(2)
        assert False
        # self.LoginPage.alert_text()

    def test_invalid_email(self):
        self.LoginPage=LoginPage(self.driver)
        time.sleep(3)
        self.LoginPage.do_invalid_email(TestData.INVALID_EMAIL,TestData.PASSWORD)
        time.sleep(3)
        assert False

    def test_invalid_password(self):
        self.LoginPage=LoginPage(self.driver)
        time.sleep(3)
        self.LoginPage.do_invalid_password(TestData.EMAIL,TestData.INVALID_PASSWORD)
        time.sleep(3)
        assert False
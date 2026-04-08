from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.LoginPage import LoginPage
from WebPages.TL_HomePage import TL_HomePage
import time

class Test_TL_Home(BaseTest):
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        home_page=self.LoginPage.do_login(TestData.TL_LOGIN_EMAIL, TestData.TL_LOGIN_PASSWORD)
        time.sleep(5)
        title=home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_assigned_candidates(self):
        self.TL_HomePage = TL_HomePage(self.driver)
        self.TL_HomePage.assigned_candidates()



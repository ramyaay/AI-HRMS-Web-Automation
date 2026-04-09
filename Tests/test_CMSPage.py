from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.LoginPage import LoginPage
from WebPages.SA_CMSPage import CMSPage
from WebPages.HomePage import HomePage
import time

class Test_CMSPage(BaseTest):
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        home_page=self.LoginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(5)
        title=home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_CMS_Creation(self):
        self.SA_CMSPage = CMSPage(self.driver)
        self.SA_CMSPage.CMS_Creation(TestData.FIELD_NAME)

    def test_CMS_Preview(self):
        self.SA_CMSPage = CMSPage(self.driver)
        self.SA_CMSPage.CMS_Preview()

    def test_CMS_Delete(self):
        self.SA_CMSPage = CMSPage(self.driver)
        self.SA_CMSPage.CMS_Delete()
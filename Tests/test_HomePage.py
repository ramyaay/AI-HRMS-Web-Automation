from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.LoginPage import LoginPage
from WebPages.HomePage import HomePage
import time

class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        home_page=self.LoginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(5)
        title=home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.HomePage = HomePage(self.driver)
        header=self.HomePage.get_header_value()
        assert header==TestData.HOME_PAGE_HEADER

    # def test_HomePage_Navigation(self):
    #     self.HomePage = HomePage(self.driver)
    #     self.HomePage.navigate_to_all_elements()

    # def test_ProfileUpdate(self):
    #     self.HomePage=HomePage(self.driver)
    #     self.HomePage.profile_update(TestData.ADMIN_PHONE_NO)

    def test_domain_creation(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.domain_creation(TestData.DOMAIN_NAME1)

    def test_domain_deletion_cancel(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.domain_deletion_cancel()

    def test_domain_deletion(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.domain_deletion()

    def test_default_domain_creation(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.default_domain_creation()
        assert False

    def test_inactive_domain_creation(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.inactive_domain_creation(TestData.DOMAIN_NAME1)

    def test_existing_domain_creation(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.create_existing_domain(TestData.DOMAIN_NAME1)
        assert False

    def test_edit_domain(self):
        self.HomePage=HomePage(self.driver)
        self.HomePage.edit_domain()

    # def test_domain_view__edit_cancel(self):
    #     self.HomePage=HomePage(self.driver)
    #     self.HomePage.domain_view_edit_cancel()
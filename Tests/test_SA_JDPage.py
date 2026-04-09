from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.LoginPage import LoginPage
from WebPages.SA_JDPage import JDPage
from WebPages.HomePage import HomePage
import time

class Test_JDPage(BaseTest):
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        home_page=self.LoginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(5)
        title=home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_create_jd_manually(self):
        self.SA_JDPage = JDPage(self.driver)
        self.SA_JDPage.create_JD_Manually(
            TestData.JOB_NAME,
            TestData.JOB_LOC,
            TestData.JOB_EXP,
            TestData.JOB_VAC,
            TestData.JOB_SKILLS,
            TestData.JOB_SUMMARY,
            TestData.JOB_RESPONSIBILITY
        )
        time.sleep(2)

    def test_default_jd_creation(self):
        self.SA_JDPage = JDPage(self.driver)
        self.SA_JDPage.default_JD_Creation()
        time.sleep(2)

    def test_leave_one_field_jd_creation(self):
        self.SA_JDPage = JDPage(self.driver)
        self.SA_JDPage.leave_one_field_create_jd(
            TestData.JOB_NAME,
            TestData.JOB_LOC,
            TestData.JOB_EXP,
            TestData.JOB_VAC,
            TestData.JOB_SKILLS,
            TestData.JOB_SUMMARY
        )
        time.sleep(2)

    def test_edit_jd(self):
        self.SA_JDPage = JDPage(self.driver)
        self.SA_JDPage.edit_jd()
        time.sleep(2)

    def test_pub_del_pub(self):
        self.SA_JDPage = JDPage(self.driver)
        self.SA_JDPage.publish_delete_publish_jd()
        time.sleep(2)

    def test_delete_jd(self):
        self.SA_JDPage = JDPage(self.driver)
        self.SA_JDPage.delete_jd()
        time.sleep(2)

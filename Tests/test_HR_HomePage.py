from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.LoginPage import LoginPage
from WebPages.HR_HomePage import HR_HomePage
import time

class Test_HR_Home(BaseTest):
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        home_page=self.LoginPage.do_login(TestData.HR_LOGIN_EMAIL, TestData.HR_LOGIN_PASSWORD)
        time.sleep(5)
        title=home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_resume_upload(self):
        self.HR_HomePage = HR_HomePage(self.driver)
        self.HR_HomePage.resume_upload()

    def test_resume_folder_delete(self):
        self.HR_HomePage = HR_HomePage(self.driver)
        self.HR_HomePage.resume_folder_delete()

    def test_resume_extract(self):
        self.HR_HomePage = HR_HomePage(self.driver)
        self.HR_HomePage.resume_extract()

    def test_view_extract_data(self):
        self.HR_HomePage = HR_HomePage(self.driver)
        self.HR_HomePage.view_extract_data()

    def test_interview_panel(self):
        self.HR_HomePage = HR_HomePage(self.driver)
        self.HR_HomePage.interview_panal()

    def test_reports(self):
        self.HR_HomePage = HR_HomePage(self.driver)
        self.HR_HomePage.reports(TestData.SEARCH_NAME)


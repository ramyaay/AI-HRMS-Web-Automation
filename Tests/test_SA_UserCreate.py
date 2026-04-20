from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.LoginPage import LoginPage
from WebPages.SA_UserCreatePage import SA_UserCreatePage
from WebPages.HomePage import HomePage
import time

class Test_UserCreate(BaseTest):
    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        home_page=self.LoginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        time.sleep(5)
        title=home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_create_user_hr(self):
        self.SA_UserCreatePage = SA_UserCreatePage(self.driver)
        self.SA_UserCreatePage.create_user_hr(
                  TestData.USER_NAME,
                  TestData.USER_EMP_ID,
                  TestData.USER_PHN_NO,
                  TestData.USER_EMAIL,
                  TestData.USER_PASSWORD
        )
        time.sleep(2)

    def test_create_blank_user(self):
        self.SA_UserCreatePage = SA_UserCreatePage(self.driver)
        self.SA_UserCreatePage.create_blank_user()
        time.sleep(4)

    def test_leave_one_field_and_create(self):
        self.SA_UserCreatePage = SA_UserCreatePage(self.driver)
        self.SA_UserCreatePage.leave_one_field_and_create(
            TestData.USER_NAME_2,
            TestData.USER_EMP_ID_2,
            TestData.USER_PHN_NO_2,
            TestData.USER_EMAIL_2,
            TestData.USER_PASSWORD_2
        )
        time.sleep(2)

    def test_Edit_User(self):
        self.SA_UserCreatePage = SA_UserCreatePage(self.driver)
        self.SA_UserCreatePage.Edit_User(TestData.EDIT_CREATE_PHN_NO)

    def test_Delete_User(self):
        self.SA_UserCreatePage = SA_UserCreatePage(self.driver)
        self.SA_UserCreatePage.Delete_User()

    def test_Filter_Section(self):
        self.SA_UserCreatePage = SA_UserCreatePage(self.driver)
        self.SA_UserCreatePage.Filter_Section()




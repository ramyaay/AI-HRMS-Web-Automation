import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage
from WebPages.HomePage import HomePage
from Config.config import TestData

class LoginPage(BasePage):
    """By Locater -OR"""
    EMAIL=(By.ID, "loginemail")
    PASSWORD=(By.ID, "password")
    LOGIN_BUTTON=(By.CSS_SELECTOR, "div[class='text-center'] button[type='submit']")
    PROFILE=(By.CSS_SELECTOR, "button[title='Profile'] div")
    LOGOUT_BUTTON=(By.CSS_SELECTOR, ".dropdown-item.text-danger")
    INVALID_EMAIL_MSG=(By.CSS_SELECTOR, ".text-danger.d-block.mt-1")
    INVALID_PASSWORD_MSG=(By.CSS_SELECTOR, "#password-error")
    LOGIN_SUCCESS_MSG=(By.XPATH, "//div[@class='snackbar success success']")
    # SIGNUP_LINK=(By.NAME, "signup")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    """This is used to get the page title"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """This is used to login to app"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        time.sleep(2)
        self.do_send_keys(self.PASSWORD,password)
        time.sleep(2)
        self.do_click(self.LOGIN_BUTTON)
        text=self.get_element_text(self.LOGIN_SUCCESS_MSG)
        print(text)
        return HomePage(self.driver)

    """This is used to logout to app"""
    def do_logout(self):
        time.sleep(5)
        self.do_click(self.PROFILE)
        self.do_click(self.LOGOUT_BUTTON)

    """This is used to login without entering credentials"""
    def default_login(self):
        self.do_click(self.LOGIN_BUTTON)

    """This is used to login by entering invalid email"""
    def do_invalid_email(self,username, password):
        self.do_send_keys(self.EMAIL,username)
        time.sleep(2)
        self.do_send_keys(self.PASSWORD,password)
        time.sleep(2)
        self.do_click(self.LOGIN_BUTTON)
        text=self.get_element_text(self.INVALID_EMAIL_MSG)
        print(text)

    """This is used to login by entering invalid password"""
    def do_invalid_password(self,username, password):
        Email = self.driver.find_element(*self.EMAIL)
        Email.clear()
        Password = self.driver.find_element(*self.PASSWORD)
        Password.clear()
        self.do_send_keys(self.EMAIL, username)
        time.sleep(2)
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.LOGIN_BUTTON)
        text=self.get_element_text(self.INVALID_EMAIL_MSG)
        print(text)


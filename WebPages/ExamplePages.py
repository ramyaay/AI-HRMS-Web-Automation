import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage

class Button(BasePage):
    FOLLOW_BUTTON=(By.XPATH, "//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation2 mb-6 css-x0wmhw']//div[2]//div[1]//div[3]//span[1]//button[1]")
    UNFOLLOW_BUTTON=(By.XPATH, "//button[normalize-space()='Following']")
    REMOVE_BUTTON=(By.XPATH, "//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation2 mb-6 css-x0wmhw']//div[2]//div[1]//div[1]//button[1]//*[name()='svg']")
    NAME=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
    EMAIL=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]")
    PHONENUMBER=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]")
    EVENT=(By.XPATH, "//div[@aria-label='Select Event']")
    SELECT_EVENT=(By.XPATH, "//li[normalize-space()='Automation Summit']")
    TICKETS=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/input[1]")
    REGISTER=(By.XPATH, "//button[normalize-space()='Register']")
    RESET=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[6]/button[2]")

    def __init__(self,driver):
        super().__init__(driver)

    def follow_button(self):
        self.do_click(self.FOLLOW_BUTTON)
        time.sleep(4)

    def unfollow_button(self):
        self.do_click(self.UNFOLLOW_BUTTON)
        time.sleep(4)

    def remove_button(self):
        self.do_click(self.REMOVE_BUTTON)
        time.sleep(2)

    def form_submit(self,name,email,phonenumber):
        self.do_send_keys(self.NAME,name)
        self.do_send_keys(self.EMAIL,email)
        self.do_send_keys(self.PHONENUMBER,phonenumber)
        self.do_click(self.EVENT)
        self.do_click(self.SELECT_EVENT)
        self.do_click(self.REGISTER)
        time.sleep(2)

    def form_submit_without_date(self,name,email):
        self.do_send_keys(self.NAME, name)
        time.sleep(2)
        self.do_send_keys(self.EMAIL, email)
        time.sleep(2)
        self.do_click(self.REGISTER)
        time.sleep(2)

    def form_submit_invalid_email(self, name, email, phonenumber):
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONENUMBER, phonenumber)
        self.do_click(self.EVENT)
        self.do_click(self.SELECT_EVENT)
        self.do_click(self.REGISTER)
        time.sleep(2)

    def form_submit_invalid_phone(self, name, email, phonenumber):
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONENUMBER, phonenumber)
        self.do_click(self.EVENT)
        self.do_click(self.SELECT_EVENT)
        self.do_click(self.REGISTER)
        time.sleep(2)

    def form_submit_invalid_ticket(self, name, email, phonenumber, ticket):
        clear_ticket = self.driver.find_element(*self.TICKETS)
        clear_ticket.clear()
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONENUMBER, phonenumber)
        self.do_click(self.EVENT)
        self.do_click(self.SELECT_EVENT)
        self.do_send_keys(self.TICKETS, ticket)
        self.do_click(self.REGISTER)
        time.sleep(2)

    def form_submit_reset(self, name, email, phonenumber, ticket):
        clear_ticket = self.driver.find_element(*self.TICKETS)
        clear_ticket.clear()
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONENUMBER, phonenumber)
        self.do_click(self.EVENT)
        self.do_click(self.SELECT_EVENT)
        self.do_send_keys(self.TICKETS, ticket)
        time.sleep(3)
        self.do_click(self.RESET)
        time.sleep(2)

    def form_submit_multiple_ticket(self, name, email, phonenumber, ticket):
        clear_ticket = self.driver.find_element(*self.TICKETS)
        clear_ticket.clear()
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONENUMBER, phonenumber)
        self.do_click(self.EVENT)
        self.do_click(self.SELECT_EVENT)
        self.do_send_keys(self.TICKETS, ticket)
        self.do_click(self.REGISTER)
        time.sleep(4)

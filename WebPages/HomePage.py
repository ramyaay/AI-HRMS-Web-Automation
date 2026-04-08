import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage

class HomePage(BasePage):
    HEADER=(By.XPATH, "//h2[normalize-space()='Welcome Amaresh Patil!']")
    PROFILE=(By.CSS_SELECTOR, "button[title='Profile'] div")
    NOTIFICATION_SYMBOL=(By.XPATH, "//a[@id='bell-icon-btn']//*[name()='svg']")
    MANAGE_USERS_BTN=(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > nav:nth-child(1) > a:nth-child(2)")
    JD_BTN=(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > nav:nth-child(1) > a:nth-child(3)")
    SETTINGS_BTN=(By.CSS_SELECTOR, ".nav-link.d-flex.justify-content-between.align-items-center[data-bs-toggle='collapse']")
    NOTIFICATIONS_BTN=(By.CSS_SELECTOR, "a[class='nav-link d-flex align-items-center justify-content-between']")
    MY_PROFILE_BTN=(By.XPATH, "//a[normalize-space()='My Profile']")
    MY_PROFILE_EDIT=(By.XPATH, "//button[normalize-space()='Edit']")
    MY_PROFILE_UPDATE=(By.XPATH, "//button[normalize-space()='Update']")
    MY_PROFILE_PHN_EDIT=(By.ID, "edit_phone_no")
    MY_PROFILE_PASSWORD=(By.ID, "edit_password")
    MY_PROFILE_CON_PASSWORD=(By.ID, "edit_confirm_password")
    DOMAIN_BTN=(By.XPATH, "//a[normalize-space()='Domain']")
    CREATE_DOMAIN_BTN=(By.XPATH, "//button[normalize-space()='Create Domain']")
    DOMAIN_INPUT=(By.ID, "createDomainInput")
    ACTIVATE_DOMAIN=(By.ID, "activateDomain")
    DOMAIN_SUBMIT=(By.XPATH, "//form[@action='/domains/create/']//div[@class='d-flex justify-content-between align-items-center mt-4']//div//button[@type='submit'][normalize-space()='Submit']")
    REMOVE_DOM_PAGE_BTN=(By.CSS_SELECTOR, "div[id='createDomainModal'] button[type='button']")
    SEL_DOMAIN_DEL=(By.XPATH, "//tbody/tr[1]/td[1]/input[1]")
    DOMAIN_DEL_BTN=(By.XPATH, "//button[normalize-space()='Delete']")
    CON_DOMAIN_DEL=(By.XPATH, "//button[normalize-space()='Ok']")
    CANCEL_DOMAIN_DEL=(By.XPATH, "//button[normalize-space()='Cancel']")
    DUPLICATE_DOMAIN_CREATION_MSG=(By.ID, "createDomainError")
    DOM_3_DOTS_CLICK=(By.XPATH, "//tbody/tr[1]/td[4]/div[1]/button[1]//*[name()='svg']")
    DOM_CLICK_VIEW=(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-end show']//a[@class='dropdown-item view-domain-btn'][normalize-space()='View']")
    DOM_EDIT_BTN=(By.XPATH, "/html[1]/body[1]/div[2]/div[5]/div[1]/div[1]/div[2]/div[1]/button[1]")
    DOM_ACTIVE_INACT_CHECK_BOX=(By.XPATH, "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]")
    DOM_EDIT_SUBMIT=(By.XPATH, "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/button[1]")
    DOM_VIEW_REMOVE_PAGE=(By.XPATH, "/html[1]/body[1]/div[2]/div[5]/div[1]/div[1]/div[1]/button[1]")
    DOM_EDIT_REMOVE_PAGE=(By.XPATH, "/html[1]/body[1]/div[2]/div[6]/div[1]/div[1]/div[1]/button[1]")
    SUCCESS_MSG = (By.XPATH, "//div[@class='snackbar success']")

    def __init__(self,driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def navigate_to_all_elements(self):
        self.do_click(self.PROFILE)
        time.sleep(2)
        self.do_click(self.NOTIFICATION_SYMBOL)
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.do_click(self.MANAGE_USERS_BTN)
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.do_click(self.JD_BTN)
        time.sleep(2)
        self.do_click(self.SETTINGS_BTN)
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.do_click(self.NOTIFICATIONS_BTN)
        time.sleep(2)
        self.driver.back()

    def profile_update(self,phn_no):
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.MY_PROFILE_BTN)
        time.sleep(1)
        self.do_click(self.MY_PROFILE_EDIT)
        time.sleep(1)
        Phone = self.driver.find_element(*self.MY_PROFILE_PHN_EDIT)
        Phone.clear()
        self.do_send_keys(self.MY_PROFILE_PHN_EDIT,phn_no)
        self.do_click(self.MY_PROFILE_UPDATE)
        text = self.get_element_text(self.SUCCESS_MSG)
        print(text)

    def domain_creation(self, domain_name):
        self.do_click(self.SETTINGS_BTN)
        time.sleep(1)
        self.do_click(self.DOMAIN_BTN)
        time.sleep(1)
        self.do_click(self.CREATE_DOMAIN_BTN)
        time.sleep(1)
        self.do_send_keys(self.DOMAIN_INPUT,domain_name)
        time.sleep(1)
        self.do_click(self.ACTIVATE_DOMAIN)
        time.sleep(1)
        self.do_click(self.DOMAIN_SUBMIT)
        time.sleep(1)
        text = self.get_element_text(self.SUCCESS_MSG)
        print(text)


    def domain_deletion_cancel(self):
        self.do_click(self.SEL_DOMAIN_DEL)
        time.sleep(2)
        self.do_click(self.DOMAIN_DEL_BTN)
        time.sleep(1)
        self.do_click(self.CANCEL_DOMAIN_DEL)
        time.sleep(1)

    def domain_deletion(self):
        self.do_click(self.DOMAIN_DEL_BTN)
        time.sleep(1)
        self.do_click(self.CON_DOMAIN_DEL)
        time.sleep(1)
        text = self.get_element_text(self.SUCCESS_MSG)
        print(text)

    def default_domain_creation(self):
        self.do_click(self.CREATE_DOMAIN_BTN)
        time.sleep(1)
        self.do_click(self.DOMAIN_SUBMIT)
        time.sleep(1)

    def inactive_domain_creation(self,domain_name):
        self.do_click(self.REMOVE_DOM_PAGE_BTN)
        time.sleep(1)
        self.do_click(self.CREATE_DOMAIN_BTN)
        time.sleep(1)
        self.do_send_keys(self.DOMAIN_INPUT, domain_name)
        time.sleep(1)
        self.do_click(self.DOMAIN_SUBMIT)
        time.sleep(2)
        text = self.get_element_text(self.SUCCESS_MSG)
        print(text)

    def create_existing_domain(self,domain_name):
        self.do_click(self.CREATE_DOMAIN_BTN)
        time.sleep(1)
        self.do_send_keys(self.DOMAIN_INPUT, domain_name)
        time.sleep(1)
        self.do_click(self.DOMAIN_SUBMIT)
        time.sleep(1)
        text = self.get_element_text(self.DUPLICATE_DOMAIN_CREATION_MSG)
        print(text)
        time.sleep(1)
        self.do_click(self.REMOVE_DOM_PAGE_BTN)
        time.sleep(1)

    def edit_domain(self):
        self.do_click(self.DOM_3_DOTS_CLICK)
        time.sleep(1)
        self.do_click(self.DOM_CLICK_VIEW)
        time.sleep(2)
        self.do_click(self.DOM_EDIT_BTN)
        time.sleep(1)
        self.do_click(self.DOM_ACTIVE_INACT_CHECK_BOX)
        time.sleep(1)
        self.do_click(self.DOM_EDIT_SUBMIT)
        time.sleep(2)
        text = self.get_element_text(self.SUCCESS_MSG)
        print(text)

    def domain_view_edit_cancel(self):
        self.do_click(self.DOM_3_DOTS_CLICK)
        time.sleep(1)
        self.do_click(self.DOM_CLICK_VIEW)
        time.sleep(1)
        self.do_click(self.REMOVE_DOM_PAGE_BTN)
        time.sleep(1)
        self.do_click(self.DOM_3_DOTS_CLICK)
        time.sleep(1)
        self.do_click(self.DOM_CLICK_VIEW)
        time.sleep(1)
        self.do_click(self.DOM_EDIT_BTN)
        time.sleep(1)
        self.do_click(self.REMOVE_DOM_PAGE_BTN)
        time.sleep(1)







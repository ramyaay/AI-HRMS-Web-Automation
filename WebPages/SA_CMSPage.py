import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage

class CMSPage(BasePage):
    """By Locater -OR"""
    SETTINGS_BTN = (By.XPATH, "//span[normalize-space()='Settings']")
    CMS_FORM_BTN = (By.XPATH, "//a[normalize-space()='CMS Form']")
    CREATE_CMS_BTN = (By.ID, "createFieldBtn")
    FIELD_NAME = (By.ID, "fieldLabel")
    INPUT_TYPE_DD = (By.ID, "inputType")
    INPUT_TYPE = (By.XPATH, "//option[@value='star_rating']")
    VISIBILITY_HR = (By.ID, "visHR")
    OPERATION_HR = (By.ID, "opHR")
    VISIBILITY_TL = (By.ID, "visTL")
    OPERATION_TL = (By.ID, "opTL")
    SAVE_FIELD = (By.ID, "saveFieldBtn")
    PREVIEW_BTN = (By.ID, "previewBtn")
    CLOSE_PREVIEW_PAGE = (By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/button[1]")
    CHECK_BOX_BTN = (By.XPATH, "(//input[@class='form-check-input select-checkbox'])[1]")
    DELETE_BTN = (By.ID, "deleteFieldBtn")
    CON_DELETE = (By.ID, "confirmDeleteBtn")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """This is used to create the CMS field"""
    def CMS_Creation(self, field_name):
        self.do_click(self.SETTINGS_BTN)
        time.sleep(1)
        self.do_click(self.CMS_FORM_BTN)
        time.sleep(1)
        self.do_click(self.CREATE_CMS_BTN)
        time.sleep(1)
        self.do_send_keys(self.FIELD_NAME, field_name)
        time.sleep(1)
        self.do_click(self.INPUT_TYPE_DD)
        time.sleep(1)
        self.do_click(self.INPUT_TYPE)
        time.sleep(1)
        self.do_click(self.VISIBILITY_HR)
        time.sleep(1)
        self.do_click(self.OPERATION_HR)
        time.sleep(1)
        self.do_click(self.VISIBILITY_TL)
        time.sleep(1)
        self.do_click(self.OPERATION_TL)
        time.sleep(1)
        self.do_click(self.SAVE_FIELD)
        time.sleep(2)

    """This is used to preview the CMS Page"""
    def CMS_Preview(self):
        self.do_click(self.PREVIEW_BTN)
        time.sleep(1)
        self.do_click(self.CLOSE_PREVIEW_PAGE)
        time.sleep(2)

    """This is used to delete the CMS field"""
    def CMS_Delete(self):
        self.do_click(self.CHECK_BOX_BTN)
        time.sleep(1)
        self.do_click(self.DELETE_BTN)
        time.sleep(1)
        self.do_click(self.CON_DELETE)
        time.sleep(1)
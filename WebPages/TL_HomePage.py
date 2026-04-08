import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage

class TL_HomePage(BasePage):
    ASSIGNED_CANDIDATES_BTN=(By.XPATH, "//a[normalize-space()='Assigned Candidates']")
    SELECT_CANDIDATE_DROPDOWN=(By.ID, "dropdownLabel")
    SELECT_CANDIDATE=(By.XPATH, "(//a[@class='dropdown-item'])[2]")
    TL_BACK_BTN=(By.ID, "tlBackButton")

    def __init__(self,driver):
        super().__init__(driver)

    def assigned_candidates(self):
        self.do_click(self.ASSIGNED_CANDIDATES_BTN)
        time.sleep(1)
        self.do_click(self.SELECT_CANDIDATE_DROPDOWN)
        time.sleep(1)
        self.do_click(self.SELECT_CANDIDATE)
        time.sleep(1)
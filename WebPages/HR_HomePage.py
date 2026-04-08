import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage

class HR_HomePage(BasePage):
    RESUME_BTN=(By.XPATH, "//a[normalize-space()='Resume']")
    UPLOAD_BTN=(By.ID, "openUploadBtn")
    DROP_FILE_CONTAINER=(By.ID, "dropAreaContent")
    UPLOAD_RESUME_BTN=(By.ID, "uploadBtn")
    SELECT_RESUME_FOLDER=(By.XPATH, "(//input[@class='form-check-input custom-checkbox folder-toggle'])[2]")
    DELETE_BTN=(By.ID, "deleteSelectedBtn")
    CON_DELETE=(By.ID, "confirmDeleteYes")
    SELECT_RESUME_FOLDER_TO_EXTRACT=(By.XPATH, "(//div[@class='card-body d-flex justify-content-between align-items-start'])[1]")
    SELECT_RESUME=(By.XPATH, "(//input[@class='form-check-input custom-checkbox file-checkbox'])[1]")
    EXTRACT_RESUME_BUTTON=(By.ID, "extractResumesBtn")
    VIEW_EXTRACT_DATA=(By.PARTIAL_LINK_TEXT, "AluruSaitejasree_fresher.pdf")
    BACK_BTN=(By.PARTIAL_LINK_TEXT, "← Back")
    INIERVIEW_PANEL_BTN=(By.XPATH, "//a[normalize-space()='Interview Panel']")
    RESUME_SELECT=(By.XPATH, "(//input[@type='radio'])[9]")
    JD_SELECT=(By.XPATH, "(//input[@class='form-check-input jd-checkbox'])[1]")
    MATCH_CANDIDATE_BTN=(By.XPATH, "//button[@onclick='matchCandidates()']")
    TO_VIEW_MATCHING_SCORE=(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/button[1]/*[name()='svg'][1]")
    CLOSE_BTN=(By.XPATH, "(//button[@class='btn-close'])[3]")
    TO_MOVE_INTERVIEW_PAGE=(By.ID, "action-cell-69a0320e04cd68a0f76339d4")
    CONDUCT_INTERVIEW_BTN=(By.ID, "conductInterviewBtn")
    GENERATE_QA=(By.ID, "generateTechQA")
    ANSWER=(By.NAME, "rating_0")
    SUBMIT_ANS_BTN=(By.ID, "submitTechFinalBtn")
    CON_SUBMIT_ANS_BTN=(By.ID, "confirmTechSubmitBtn")
    STATUS_DROPDOWN=(By.ID, "statusDropdown")
    SELECT_STATUS=(By.LINK_TEXT, "Select")
    STAR_RATING=(By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[5]/div[2]/div[1]/div[1]/span[3]")
    FINAL_SUBMIT=(By.XPATH, "//button[@onclick='submitFeedbackFromCard2()']")
    CON_FINAL_SUBMIT=(By.ID, "confirmActionBtn")
    BACK_BTN_AFTER_INTERVIEW=(By.ID, "backButtonText")
    REPORTS_BTN=(By.XPATH, "//a[normalize-space()='Reports']")
    SEARCH_INPUT=(By.ID, "searchInput")

    def __init__(self,driver):
        super().__init__(driver)

    def resume_upload(self):
        self.do_click(self.RESUME_BTN)
        time.sleep(1)
        self.do_click(self.UPLOAD_BTN)
        time.sleep(1)
        # self.do_click(self.DROP_FILE_CONTAINER)
        # time.sleep(1)
        file_input = self.get_element((By.XPATH, "//input[@type='file']"))
        file_input.send_keys(r"D:\Folder1\Downloads\resumes 1\resumes\AluruSaitejasree_fresher.pdf")
        time.sleep(2)
        self.do_click(self.UPLOAD_RESUME_BTN)
        time.sleep(4)

    def resume_folder_delete(self):
        self.do_click(self.SELECT_RESUME_FOLDER)
        time.sleep(1)
        self.do_click(self.DELETE_BTN)
        time.sleep(1)
        self.do_click(self.CON_DELETE)
        time.sleep(1)

    def resume_extract(self):
        self.do_click(self.SELECT_RESUME_FOLDER_TO_EXTRACT)
        time.sleep(1)
        self.do_click(self.SELECT_RESUME)
        time.sleep(1)
        self.do_click(self.EXTRACT_RESUME_BUTTON)
        time.sleep(4)

    def view_extract_data(self):
        self.do_click(self.VIEW_EXTRACT_DATA)
        time.sleep(3)
        self.do_click(self.BACK_BTN)
        time.sleep(2)

    def interview_panal(self):
        self.do_click(self.INIERVIEW_PANEL_BTN)
        time.sleep(1)
        self.do_click(self.RESUME_SELECT)
        time.sleep(1)
        self.do_click(self.JD_SELECT)
        time.sleep(1)
        self.do_click(self.MATCH_CANDIDATE_BTN)
        time.sleep(4)
        self.do_click(self.TO_VIEW_MATCHING_SCORE)
        time.sleep(1)
        self.do_click(self.CLOSE_BTN)
        time.sleep(1)
        self.do_click(self.TO_MOVE_INTERVIEW_PAGE)
        time.sleep(1)
        self.do_click(self.CONDUCT_INTERVIEW_BTN)
        time.sleep(2)
        self.do_click(self.GENERATE_QA)
        time.sleep(1)
        self.do_click(self.ANSWER)
        time.sleep(1)
        self.do_click(self.SUBMIT_ANS_BTN)
        time.sleep(1)
        self.do_click(self.CON_SUBMIT_ANS_BTN)
        time.sleep(1)
        self.do_click(self.STATUS_DROPDOWN)
        time.sleep(3)
        # self.do_click(self.SELECT_STATUS)
        # time.sleep(1)
        self.do_click(self.STAR_RATING)
        time.sleep(1)
        self.do_click(self.FINAL_SUBMIT)
        time.sleep(1)
        self.do_click(self.CON_FINAL_SUBMIT)
        time.sleep(5)
        self.do_click(self.BACK_BTN_AFTER_INTERVIEW)
        time.sleep(2)

    def reports(self, name):
        self.do_click(self.REPORTS_BTN)
        time.sleep(1)
        self.do_send_keys(self.SEARCH_INPUT, name)
        time.sleep(3)











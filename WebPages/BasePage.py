from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        return self.driver.title

    def do_send_keys(self, by_locater, text):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locater)).send_keys(text)

    def get_element_text(self,by_locater):
        element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locater))
        return element.text

    def do_click(self, by_locater):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locater)).click()

    def is_visible(self, by_locater):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locater))
        return element.is_displayed()

    def alert_text(self):
        alert=self.driver.switch_to.alert
        return alert.text

    def select_dropdown_value(self, dropdown_locator, options_locator, data_value):
        self.do_click(dropdown_locator)
        options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(options_locator))
        for option in options:
            if option.text.strip() == data_value:
                option.click()
                return True

        raise Exception(f"Value '{data_value}' not found in dropdown")

    def get_element(self, locator):
        return self.driver.find_element(*locator)



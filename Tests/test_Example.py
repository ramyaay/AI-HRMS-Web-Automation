from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.ExamplePages import Button

class Test_button(BaseTest):
    # def test_follow(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.follow_button()
    #
    # def test_unfollow(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.unfollow_button()
    #
    # def test_remove(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.remove_button()

    # def test_form_submit(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.form_submit(
    #         TestData.EXNAME,
    #         TestData.EXEMAIL,
    #         TestData.EXPHNNUMBER
    #     )

    # def test_form_submit_without_data(self):
    #     self.ExamplePage = Button(self.driver)
    #     self.ExamplePage.form_submit_without_date(
    #         TestData.EXNAME,
    #         TestData.EXEMAIL
    #     )

    # def test_form_submit_invalid_email(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.form_submit_invalid_email(
    #         TestData.EXNAME,
    #         TestData.EXEMAIL,
    #         TestData.EXPHNNUMBER
    # )

    # def test_form_submit_invalid_phone(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.form_submit_invalid_phone(
    #         TestData.EXNAME,
    #         TestData.EXEMAIL,
    #         TestData.EXPHNNUMBER
    # )

    # def test_form_submit_invalid_ticket(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.form_submit_invalid_ticket(
    #         TestData.EXNAME,
    #         TestData.EXEMAIL,
    #         TestData.EXPHNNUMBER,
    #         TestData.TICKET
    # )

    # def test_form_submit_reset(self):
    #     self.ExamplePage=Button(self.driver)
    #     self.ExamplePage.form_submit_reset(
    #         TestData.EXNAME,
    #         TestData.EXEMAIL,
    #         TestData.EXPHNNUMBER,
    #         TestData.TICKET
    # )

    def test_form_submit_multiple_ticket(self):
        self.ExamplePage=Button(self.driver)
        self.ExamplePage.form_submit_multiple_ticket(
            TestData.EXNAME,
            TestData.EXEMAIL,
            TestData.EXPHNNUMBER,
            TestData.TICKET
    )



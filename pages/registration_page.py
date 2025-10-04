from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect



class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form_component = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.visible_ui_course_title = page.get_by_test_id('authentication-ui-course-title-text')




    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()


    def visible_ui_course_title(self):
        expect(self.visible_ui_course_title).to_be_visible()
        expect(self.visible_ui_course_title).to_have_text("UI Course")
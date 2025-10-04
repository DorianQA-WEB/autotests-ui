from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.button = page.get_by_test_id('create-course-toolbar-create-course-button')


    def check_visible(self, is_create_course_disabled=True):
        if is_create_course_disabled == True:
            expect(self.title).to_be_visible()
            expect(self.title).to_have_value("Create course")
            expect(self.button).to_be_visible()
            expect(self.button).to_be_disabled()
        else:
            expect(self.title).to_be_visible()
            expect(self.title).to_have_value("Create course")
            expect(self.button).to_be_visible()
            expect(self.button).not_to_be_enabled()
            self.button.click()
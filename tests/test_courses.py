from playwright.sync_api import expect
import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.check_visible_courses_title()
        courses_list_page.check_visible_create_course_button()
        courses_list_page.check_empty_view_icon()


        # chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        #
        # title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        # expect(title_courses).to_be_visible()
        # expect(title_courses).to_have_text('Courses')
        #
        # there_is_not_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        # expect(there_is_not_result).to_be_visible()
        # expect(there_is_not_result).to_have_text('There is no results')
        #
        # icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        # expect(icon).to_be_visible()
        #
        # result_from_the_load = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        # expect(result_from_the_load).to_be_visible()
        # expect(result_from_the_load).to_have_text('Results from the load test pipeline will be displayed here')

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disable_create_course_button()
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.check_visible_image_upload_view()
        create_course_page.check_visible_create_course_form(
                title='',
                estimated_time='',
                description='',
                max_score='0',
                min_score='0')
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.upload_preview_image('./testdata/files/image.png')
        create_course_page.check_visible_image_upload_view()

        create_course_page.fill_create_course_form(
                title='Playwright',
                estimated_time='2 weeks',
                description='Playwright',
                max_score='100',
                min_score='10'
        )
        create_course_page.click_create_course_button()
        courses_list_page.check_visible_courses_title()
        courses_list_page.check_visible_create_course_button()
        courses_list_page.check_visible_course_card(
                index=0,
                title='Playwright',
                estimated_time='2 weeks',
                max_score='100',
                min_score='10'
        )
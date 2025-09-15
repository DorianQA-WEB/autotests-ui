from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):

        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_courses).to_be_visible()
        expect(title_courses).to_have_text('Courses')

        there_is_not_result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(there_is_not_result).to_be_visible()
        expect(there_is_not_result).to_have_text('There is no results')

        icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()

        result_from_the_load = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_from_the_load).to_be_visible()
        expect(result_from_the_load).to_have_text('Results from the load test pipeline will be displayed here')
from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_visible_page_courses():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        user_name_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_courses).to_be_visible()
        expect(title_courses).to_have_text('Courses')

        there_is_not_result = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(there_is_not_result).to_be_visible()
        expect(there_is_not_result).to_have_text('There is no results')

        icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()

        result_from_the_load = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_from_the_load).to_be_visible()
        expect(result_from_the_load).to_have_text('Results from the load test pipeline will be displayed here')
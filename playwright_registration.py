from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input = page.locator('//div//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    user_name_input = page.locator('//div//input[@id=":r1:"]')
    user_name_input.fill("username")

    password_input = page.locator('//div//input[@id=":r2:"]')
    password_input.fill('password')

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    dashboard = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text("Dashboard")

    page.wait_for_timeout(2000)

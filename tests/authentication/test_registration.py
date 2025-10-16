import pytest
import allure

from config import settings
from pages.dasboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGISTRATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestRegistration:
        @allure.title('Registration with correct email and password')
        @allure.severity(Severity.CRITICAL)
        def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage, ):
                registration_page.visit(
                        AppRoute.REGISTRATION)
                registration_page.registration_form.fill(
                        email=settings.test_user.email,
                        username=settings.test_user.username,
                        password=settings.test_user.password
                )
                registration_page.click_registration_button()

                dashboard_page.dashboard_toolbar_view.check_visible()

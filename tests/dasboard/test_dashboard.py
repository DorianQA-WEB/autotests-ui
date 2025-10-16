import pytest
import allure
from pages.dasboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSION, AllureTags.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.DASHBOARD)
@allure.story(AllureStories.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.DASHBOARD)
@allure.sub_suite(AllureStories.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.activities_chart.check_visible("Activities")
        dashboard_page_with_state.students_chart.check_visible('Students')
        dashboard_page_with_state.courses_chart.check_visible('Courses')
        dashboard_page_with_state.scores_chart.check_visible('Scores')




import pytest
import unittest


@pytest.mark.usefixtures("onetimesetup")
class EasyTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self,onetimesetup):
        print("In easy setup")

    def test_easy_login(self):
        print("Verifying easy login")
        self.driver.get("https://easy.techmahindra.com")
        assert "EASY - Login" in self.driver.title
        pass

    def test_navigate_to_timesheet(self):
        print("Verify MyTime navigation")
        pass

    def test_select_the_desired_week(self):
        print("verifying desired week is selected")
        pass


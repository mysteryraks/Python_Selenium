import pytest
import unittest


@pytest.mark.usefixtures("onetimesetup")
class BasicTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, onetimesetup):
        print("In setup")

    def test_twitter(self):
        self.driver.get("http://www.twitter.com")
        assert "Twitter" in self.driver.title

    def test_facebook(self):
        self.driver.get("http://www.facebook.com")
        assert "Facebook" in self.driver.title
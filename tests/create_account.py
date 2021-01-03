
import random
import pytest

from pages.my_accout_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_creat_account_fail(self):

        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("arti_arti@op.pl","testeroprogramowaniapython")

        msg = ' An account is already registered with your email address. Please log in.'
        assert msg in my_account_page.get_error_msg()

    def test_creat_account_pass(self):

        email = str(random.randint(0,10000)) + "arti_arti@op.pl"

        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email,"testeroprogramowaniapython")

        assert my_account_page.is_logout_link_displayed()


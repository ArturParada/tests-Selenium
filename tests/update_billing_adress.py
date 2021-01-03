import random

import pytest


from pages.billing_address_page import BillingAddressPage
from pages.my_accout_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0,10000)) + "arti_arti@op.pl"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email,"testeroprogramowaniapython")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John","Smith")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Kwiatowa 1","98-300", "Lodz")
        billing_address_page.set_phone_number("888888888")
        billing_address_page.save_address()
        assert 'Address changed successfully' in billing_address_page.get_message_text()


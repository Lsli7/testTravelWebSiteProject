
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.login_success_page import LoginSuccessPage
from resources.constants import TEST_SITE_URL, LOGIN_SUCCESS_PAGE_TXT
from tests.conftest import username_password


class TestLogin:

    # Test Case 1 ( Registering the user)
    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"

    def test_signIn_registered_user(self,driver, username_password):
        register_success_page = RegisterSuccessPage(driver)
        register_success_page.click_login_url()

        login_page = LoginPage(driver)
        login_page.wait_and_type_user_name(username_password)
        login_page.type_password(username_password)
        login_page.click_submit_btn()

        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert login_success_lbl.__contains__ (LOGIN_SUCCESS_PAGE_TXT), "User login failed"



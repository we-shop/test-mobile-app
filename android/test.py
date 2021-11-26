import pytest
import os

# LIST OF TESTS
def atest_login_and_logout(login_model, debug_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_with_assert(selenium)
	login_model.logout(selenium)

def atest_login_with_incorrect_pass(login_model, debug_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_with_incorrect_creds(selenium)

def atest_search_request_n_clear_field(login_model, debug_model, search_model, selenium):
	debug_model.switch_to_uat(selenium)
	login_model.login_only(selenium)
	search_model.search_and_clear_field(selenium)

# def test_login_exit(login_model, debug_model, selenium):
# 	debug_model.switch_to_uat(selenium)
# 	login_model.login_only(selenium)
# 	login_model.logout_from_main_screen(selenium)
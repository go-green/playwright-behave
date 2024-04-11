"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""

from behave import *
from behave.runner import Context

from pages.login_page import LoginPage


@given("I have navigated to GitHub login page")
def i_have_navigated_to_prm_login_page(context: Context):
    base_url = context.settings["base_url"]
    context.login_page = LoginPage(context.page)
    context.login_page.navigate(base_url)
    assert context.prm_login_page.verify_page() is True


@when("I enter my valid credentials")
def i_enter_my_credentials(context: Context):
    context.login_page.login("sample@github.com", "password")


@then("I am navigated to the default landing page")
def i_am_navigated_to_the_default_prm_landing_page(context: Context):
    context.login_page.verify_page()

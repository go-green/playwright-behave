"""
  @filename:    environment.py
  @author:      Rasika Ranawaka
  @date:        22/01/2024
"""
import allure
from allure_commons.types import AttachmentType
from behave.model import Scenario, Step
from behave.runner import Context
from playwright.sync_api import sync_playwright

from configuration_settings import ConfigurationSettings


def before_all(context) -> None:
    settings = ConfigurationSettings.get_config()
    context.settings = settings


def before_scenario(context: Context, scenario: Scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()


def after_scenario(context: Context, scenario: Scenario):
    context.browser.close()
    context.playwright.stop()


def after_step(context: Context, step: Step):
    allure.attach(context.page.screenshot(), name=step.name, attachment_type=AttachmentType.PNG)

"""
  @Filename:    configuration_settings.py
  @Author:      Rasika Ranawaka
  @Time:        22/01/2024
"""

import json


class ConfigurationSettings:
    configuration_settings: dict = {}

    @classmethod
    def init_config_settings(cls):
        with open("config.json", encoding="utf-8") as file:
            cls.configuration_settings = json.load(file)

    @classmethod
    def get_config(cls) -> dict:
        if bool(cls.configuration_settings) is False:
            cls.init_config_settings()
        return cls.configuration_settings

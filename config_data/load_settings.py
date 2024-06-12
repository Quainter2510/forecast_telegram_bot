import json
from config_data import config
from distutils.util import strtobool

def load():
    with open("settings.json", "r") as settings:
        setup = json.load(settings)
        config.ALL_FUNCTION_READY = strtobool(setup["all_func_ready"])
        config.REGISTRATION_IS_OPEN = strtobool(setup["registration_is_open"])


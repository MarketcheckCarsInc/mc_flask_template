import os
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    os.environ["BT_MAPPING"] = "{}"
    os.environ["BT_TABLE_NAME"] = ""
    os.environ["BT_ROW_KEYS"] = ""
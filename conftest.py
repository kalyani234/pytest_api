import json
import os.path

import pytest
from datetime import datetime

from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Set the path for the reports directory
    report_dir = "/Users/navyakalyani/Documents/pytest_framwork/reports"
    now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

    # Ensure the reports directory exists
    os.makedirs(report_dir, exist_ok=True)

    # Set the HTML report path with a timestamp
    config.option.html = f"{report_dir}/reports_{now}.html"



@pytest.fixture(scope='session',autouse=True)
def setup_teardown():
    print('\nstarting up resources.........')
    yield
    print('\nTearing down resources........')

@pytest.fixture
def load_user_data():
    # file path = "/Users/navyakalyani/Documents/pytest_framwork/data/test_data.json
    json_file_path= os.path.join(os.path.dirname(__file__),"data","test_data.json")
    # open the file
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data
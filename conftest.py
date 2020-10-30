#Contents of conftest.py
import pytest
 
#Command line options:
def pytest_addoption(parser):
    parser.addoption("-U","--url",
                      dest="base_url",
                      default="http://localhost:6464/",
                      help="Base url for the application under test")
 
#Test arguments:
@pytest.fixture
def base_url():
    "pytest fixture for base url"
    return pytest.config.getoption("-U")
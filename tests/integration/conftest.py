import pytest 


def pytest_addoption(parser): 
    parser.addoption("--urlreqs", 
                     default='http://opsitcdkr01:5067/', 
                     help="Specify URL where the APIs are hosted") 


@pytest.fixture 
def url(request): 
     return request.config.getoption('--urlreqs')

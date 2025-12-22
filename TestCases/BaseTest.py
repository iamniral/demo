import pytest

@pytest.mark.usefixtures("log_on_failure","appium driver")
class BaseTest:
    pass

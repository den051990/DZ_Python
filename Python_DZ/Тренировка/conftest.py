import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NDZkOWJhZWItYzBlNy00MjUwLTlmNWMtZWMxNjhjYjg3MzZm",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
    "name": "cookiesAccepted",
    "value": "true",
    "domain": "gitflic.ru"
    })
    driver.refresh()
    yield driver
    driver.quit()
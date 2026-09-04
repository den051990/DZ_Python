import pytest
from selenium import webdriver
from driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберете браузер для тестов: chrome, firefox, safari, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
         default=False,
         help="Запуск в headless режиме (без UI)"
    )


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless_mode)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "YjY4ZjVhNzctZGI3NS00MGMyLWE4MjUtMGJhNjNlMzA4MDkx",
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
    
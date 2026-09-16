from Python_DZ.lesson_10.pages.shop2_page import ShopPage
from selenium import webdriver
import allure


@allure.feature("Магазин")
@allure.title("Тестирование работы интернет магазина")
@allure.description("Тест проверяет функции: выбор товара,"
                    "оформление товара, проверка корректной итоговой суммы")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page(driver):
    driver = webdriver.Firefox()
    driver.maximize_window()

    shop = ShopPage(driver)
    shop.open_shop()
    shop.product_selection()
    shop.get_vaile()
    summa = shop.summary_total()

    driver.quit
    with allure.step("Проверка полученного результата с ожидаемым"):
        assert summa == "$58.29"

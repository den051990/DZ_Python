from Python_DZ.lesson_10.pages.calc2_page import CalcPage  
from selenium import webdriver
import allure

@allure.feature("Калькулятор")
@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет функцию задержки "
                    "и работу  калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_page(driver):
    driver = webdriver.Chrome()
    driver.maximize_window()

    get_calc = CalcPage(driver)
    get_calc.open_calc()

    second = "45"
    get_calc.delay_time(second)

    get_calc.click_button()

    element = get_calc.expect_result()

    with allure.step("Проверка полученного результата с ожидаемым"):
        assert element.text == "15"

    driver.quit()
    
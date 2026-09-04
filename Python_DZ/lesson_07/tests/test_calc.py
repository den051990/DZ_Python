from Python_DZ.lesson_07.pages.calc_page import CalcPage  
from selenium import webdriver

def test_calc_page(driver):
    driver = webdriver.Chrome()
    driver.maximize_window()

    get_calc = CalcPage(driver)
    get_calc.open_calc()

    second = "1"
    get_calc.delay_time(second)

    get_calc.click_button()

    element = get_calc.expect_result()

    assert element.text == "15"

    driver.quit()
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 20)

    personal_info = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "job-position": "QA",
            "company": "SkyPro"
    }
    for name, value in personal_info.items():
        wait.until(EC.presence_of_element_located(
            (By.NAME, name))).send_keys(value)

    Submit_click = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn-outline-primary"))).click()

    wait = WebDriverWait(driver, 10)
    zip_code_element = driver.find_element(By.ID, 'zip-code')
    border_color_red = zip_code_element.value_of_css_property('border-color')
    assert border_color_red == 'rgb(245, 194, 199)', "Поле 'Zip code' подсвечено красным"

    green_element_ids = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for id in green_element_ids:
        element = driver.find_element(By.ID, id)
        border_color_green = element.value_of_css_property('border-color')
        assert border_color_green == 'rgb(186, 219, 204)', "Остальные поля подсвечены зеленым"

    driver.quit()

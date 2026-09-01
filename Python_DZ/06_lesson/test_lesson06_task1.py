from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу 
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start" #start button
    start_click = driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # 3. Дождитесь появления текста "Hello World!" 
    Hello_World_text = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#finish h4")
    ))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("Python_DZ/screenshots/Hello World.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert Hello_World_text.text == "Hello World!"

    driver.quit()

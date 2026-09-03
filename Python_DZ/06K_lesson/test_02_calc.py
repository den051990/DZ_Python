from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 20)

    time_value = wait.until(EC.presence_of_element_located(
        (By.ID, "delay")
        ))
    time_value.clear()
    time_value.send_keys("45")


    wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='=']"))).click()

    WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"))

    element = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert element.text == "15"

    driver.quit()

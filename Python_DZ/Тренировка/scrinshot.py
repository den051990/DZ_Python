from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ru.wikipedia.org/wiki/")
wait = WebDriverWait(driver, 10)

driver.save_screenshot("Python_DZ/Тренировка/screens/full_screen.png")

main_icon = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "mw-logo-icon")
))

main_icon.screenshot("Python_DZ/Тренировка/screens/icon_screen.png")

driver.quit()
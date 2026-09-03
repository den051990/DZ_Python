from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_element_located(
        (By.ID, "user-name"))).send_keys("standard_user")
    
    wait.until(EC.presence_of_element_located(
        (By.ID, "password"))).send_keys("secret_sauce")
    
    wait.until(EC.element_to_be_clickable(
        (By.ID, "login-button"))).click()

    Backpack_click = wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    Bolt_click = wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    Onesie_click = wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    shop_clic = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".shopping_cart_link"))).click()

    checkout_clic = wait.until(EC.presence_of_element_located(
        (By.ID, "checkout"))).click()

    wait.until(EC.presence_of_element_located(
        (By.ID, "first-name"))).send_keys("Денис")
    
    wait.until(EC.presence_of_element_located(
        (By.ID, "last-name"))).send_keys("Денисов")
    
    wait.until(EC.presence_of_element_located(
        (By.ID, "postal-code"))).send_keys("555555")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "continue"))).click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    total_element = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))

    total_text = total_element.text
    total_value = total_text.replace("Total: ", "").strip()

    driver.quit()

    assert total_value == "$58.29"

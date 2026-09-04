from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    U_NAME = (By.ID, "user-name")
    PASS = (By.ID, "password")
    LOGIN = (By.ID, "login-button")
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    SHOP_CLIC = (By.CSS_SELECTOR, ".shopping_cart_link")
    CHECKOUT = (By.ID, "checkout")
    F_NAME = (By.ID, "first-name")
    L_NAME = (By.ID, "last-name")
    INDEX = (By.ID, "postal-code")
    CONT_CLICK = (By.ID, "continue")
    SUM_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_shop(self):
        self.driver.get("https://www.saucedemo.com/")
        self.wait.until(EC.presence_of_element_located(
            self.U_NAME)).send_keys("standard_user")
        self.wait.until(EC.presence_of_element_located(
            self.PASS)).send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable(
            self.LOGIN)).click()
        
    def product_selection(self):
        self.wait.until(EC.element_to_be_clickable(
            self.BACKPACK)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BOLT)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.ONESIE)).click()
        self.wait.until(EC.presence_of_element_located(
            self.SHOP_CLIC)).click()
        self.wait.until(EC.presence_of_element_located(
            self.CHECKOUT)).click()

    def get_vaile(self):
        self.wait.until(EC.presence_of_element_located(
            self.F_NAME)).send_keys("Денис")
        self.wait.until(EC.presence_of_element_located(
            self.L_NAME)).send_keys("Денисов")
        self.wait.until(EC.presence_of_element_located(
            self.INDEX)).send_keys("555555")
        self.wait.until(EC.element_to_be_clickable(
            self.CONT_CLICK)).click()

    def summary_total(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        total_element = self.wait.until(EC.presence_of_element_located(
            self.SUM_TOTAL))
        total_text = total_element.text
        return total_text.replace("Total: ", "").strip()
        
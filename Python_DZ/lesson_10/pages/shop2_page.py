from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:
    """
        Класс Page Object для страницы магазина.
        Позволяет зайти в магазин с помощью логина и пароля,
        выбрать товары, перейти в корзину и оформить покупку.
    """

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
        """
        Конструктор класса CalcPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Авторизация в магазине")
    def open_shop(self):
        """Открывает страницу магазина в браузере
        и авторизируется с помощью своего логина и пароля.
        """
        self.driver.get("https://www.saucedemo.com/")
        self.wait.until(EC.presence_of_element_located(
            self.U_NAME)).send_keys("standard_user")
        self.wait.until(EC.presence_of_element_located(
            self.PASS)).send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable(
            self.LOGIN)).click()

    @allure.step("Выбор товаров")
    def product_selection(self):
        """Выбираем товары, переходим в
        корзину и переходим к оформлению заказа.
        """
        self.wait.until(EC.element_to_be_clickable(
            self.BACKPACK)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BOLT)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.ONESIE)).click()

        with allure.step("Переход в корзину"):
            self.wait.until(EC.presence_of_element_located(
                self.SHOP_CLIC)).click()

        with allure.step("Переход к оформлению заказа"):
            self.wait.until(EC.presence_of_element_located(
                self.CHECKOUT)).click()

    @allure.step("Оформление заказа ввод своих данных")
    def get_vaile(self):
        """Оформляем заказ вводим имя, фамилию и индекс"""
        self.wait.until(EC.presence_of_element_located(
            self.F_NAME)).send_keys("Денис")
        self.wait.until(EC.presence_of_element_located(
            self.L_NAME)).send_keys("Денисов")
        self.wait.until(EC.presence_of_element_located(
            self.INDEX)).send_keys("555555")
        self.wait.until(EC.element_to_be_clickable(
            self.CONT_CLICK)).click()

    @allure.step("Проверяем итоговую сумму заказа")
    def summary_total(self):
        """Проверяем что итоговая сумма равна ожидаемой"""
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        total_element = self.wait.until(EC.presence_of_element_located(
            self.SUM_TOTAL))
        total_text = total_element.text
        return total_text.replace("Total: ", "").strip()

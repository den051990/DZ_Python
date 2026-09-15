from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """
    Класс Page Object для страницы калькулятора.
    Позволяет задавать задержку, выполнять вычисления и получать результат.
    """

    TIME_VALIE = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 =  (By.XPATH, "//span[text()='8']")
    BUTTON_RAVNO = (By.XPATH, "//span[text()='=']")
    ELEMENT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        """
        Конструктор класса CalcPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Открытие страницы калькулятора")
    def open_calc(self):
        """Открывает страницу калькулятора в браузере."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки {second} секунд")
    def delay_time(self, second):
        """Устанавливает значение задержки в поле ввода.
        :param second: int — время задержки в секундах.
        """
        time_second = self.driver.find_element(*self.TIME_VALIE)
        time_second.clear()
        time_second.send_keys(second)

    @allure.step("Нажатие кнопок")
    def click_button(self):
        """Выполняет последовательное нажатие кнопок для вычисления выражения (7+8=)."""
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_7)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_PLUS)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_8)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_RAVNO)).click()

    @allure.step("Ожидание и получение результата с экрана калькулятора")
    def expect_result(self):
        """Ожидает, пока в поле результата появится число 15, затем возвращает его.
        Return:
            str: Текст, отображаемый в поле результата (ожидается '15')."""
        self.wait.until(EC.text_to_be_present_in_element(
        self.ELEMENT, "15"))
        return self.driver.find_element(*self.ELEMENT)
    
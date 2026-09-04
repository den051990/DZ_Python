from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    TIME_VALIE = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 =  (By.XPATH, "//span[text()='8']")
    BUTTON_RAVNO = (By.XPATH, "//span[text()='=']")
    ELEMENT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def open_calc(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay_time(self, second):
        time_second = self.driver.find_element(*self.TIME_VALIE)
        time_second.clear()
        time_second.send_keys(second)

    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_7)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_PLUS)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_8)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_RAVNO)).click()

    def expect_result(self):
        self.wait.until(EC.text_to_be_present_in_element(
        self.ELEMENT, "15"))
        return self.driver.find_element(*self.ELEMENT)
    
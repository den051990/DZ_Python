import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    EDIT_BUTTON = (By.CSS_SELECTOR, ".user-profile__edit")
    NAME_INPUT = (By.ID, "name")
    LAST_NAME_INPUT = (By.ID, "surname")
    SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, ".gf-button.--success")
    USER_NAME_MAIN = (By.CSS_SELECTOR, "h6.mb-0")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    def open_profile_page(self, username):
        self.driver.get(f"{self.url}user/{username}")
        self.driver.save_screenshot("Python_DZ/Тренировка/screens/full.png")

    def update_profile(self, new_user_name, new_last_name):
        edit_button = self.wait.until(EC.presence_of_element_located(
            self.EDIT_BUTTON
        ))
        edit_button.click()
        username_input = self.wait.until(EC.presence_of_element_located(
            self.NAME_INPUT
        ))
        username_input.clear()
        username_input.send_keys(new_user_name)
        
        surname_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        surname_input.clear()
        surname_input.send_keys(new_last_name)

        save_button = self.wait.until(EC.presence_of_element_located(
            self.SAVE_PROFILE_BUTTON
        ))
        save_button.click()

    def get_user_name(self):
        user_name = self.wait.until(EC.presence_of_element_located(
            self.USER_NAME_MAIN
        ))
        user_name.screenshot("Python_DZ/Тренировка/screens/fu.png")
        return user_name.text
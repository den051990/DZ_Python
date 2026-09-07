from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage:

    PROJECT_MENU = (By.CSS_SELECTOR, '[href="/project"]')
    PROJECT_PAGE_TITLE = (By.TAG_NAME, 'h1')
    ADD_PROJECT_BUTTON = (By.CSS_SELECTOR, '.btn-success')
    TITLE_PROJECT_INPUT = (By.CSS_SELECTOR, '#projectTitle')
    SAVE_PROJECT_BUTTON = (By.CSS_SELECTOR, '.btn-success')
    PROJECT_HEADER = (By.CSS_SELECTOR, '.h3.mb-3')
    PROJECT_LIST = (By.CSS_SELECTOR, '.gf-entity-card')

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open_project_page(self):
        self.driver.get(self.url)
        self.wait.until(
            EC.presence_of_element_located(self.PROJECT_MENU)).click()

    def get_project_title_page(self):
        return self.wait.until(
            EC.presence_of_element_located(self.PROJECT_PAGE_TITLE)).text

    def create_project(self):
        self.wait.until(
            EC.presence_of_element_located(self.ADD_PROJECT_BUTTON)).click()
        self.wait.until(
            EC.presence_of_element_located(self.TITLE_PROJECT_INPUT)
        ).send_keys()
        self.driver.find_element(*self.SAVE_PROJECT_BUTTON).clic()

    def get_project_page_header(self):
        return self.wait.until(
            EC.presence_of_element_located(self.PROJECT_HEADER)).text

    def get_project_list(self):
        projects = self.wait.until(
            EC.presence_of_all_elements_located(self.PROJECT_LIST))
        return len(projects)

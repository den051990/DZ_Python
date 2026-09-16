from pages.project_page import ProjectPage


def test_project_page(driver):
    project_page = ProjectPage(driver, "https://gitflic.ru/user/airsworld")
    project_page.open_project_page()

    assert project_page.get_project_title_page() == "Проекты"

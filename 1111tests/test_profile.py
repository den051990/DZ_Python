from pages111.profile_page import ProfilePage
import faker
import config
import pytest


faker = faker.Faker()
first_name = faker.first_name()
last_name = faker.last_name()
full_name = f"{first_name} {last_name}"


def test_change_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("airsworld")
    profile.update_profile(first_name, last_name)
    profile.open_profile_page("airsworld")

    assert profile.get_user_name() == full_name, "Имя профеля не было обновлено"

def test_check_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("airsworld")
    name = profile.get_user_name()

    assert name != "", "Имя профеля должно быть не пустым"
    assert len(name) > 0, "Имя профеля содержит хотя бы один символ"

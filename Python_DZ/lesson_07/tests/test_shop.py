from Python_DZ.lesson_07.pages.shop_page import ShopPage
from selenium import webdriver

def test_shop_page(driver):
    driver = webdriver.Firefox()
    driver.maximize_window()

    shop = ShopPage(driver)
    shop.open_shop()
    shop.product_selection()
    shop.get_vaile()
    summa = shop.summary_total()

    driver.quit

    assert summa == "$58.29"
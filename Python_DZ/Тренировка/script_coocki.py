from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://gitflic.ru/")


driver.add_cookie({
    "name": "SESSION",
    "value": "NDZkOWJhZWItYzBlNy00MjUwLTlmNWMtZWMxNjhjYjg3MzZm",
    "domain": "gitflic.ru"
})

driver.add_cookie({
    "name": "cookiesAccepted",
    "value": "true",
    "domain": "gitflic.ru"
})

driver.refresh()

driver.get("https://gitflic.ru/user/airsworld")

sleep(5)

driver.delete_all_cookies()
driver.refresh()
sleep(5)

driver.quit()
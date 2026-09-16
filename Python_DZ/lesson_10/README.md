# Домашнее задание №10: Allure

## Описание проекта
Этот проект содержит автотесты для интернет-магазина SauceDemo и slow-калькулятора, написанные с использованием **Page Object** и **Allure** для генерации отчётов.

## Структура проекта
- `Python_DZ/lesson_10/pages/` – классы Page Object:
  - `shop2_page.py` – страница магазина
  - `calc2_page.py` – страница калькулятора
- `Python_DZ/lesson_10/tests/` – тестовые файлы:
  - `test_03_shop.py` – тест корзины
  - `test_slow_calculator.py` – тест калькулятора

## Требования
- Python 3.14.6
- Установленные пакеты: `pytest`, `selenium`, `webdriver-manager`, `allure-pytest`
- Установленный Allure (команда `allure` должна быть доступна в PATH)
- Браузер Chrome (или Firefox с соответствующим драйвером)

## Перейдите в дерикторию с тестами
cd Python_DZ/lesson_10/tests/

## Запустите тесты с сохранением Allure-результатов в папку allure-results:
pytest --alluredir allure-result
## После успешного запуска тестов запустите команду
allure serve allure-results
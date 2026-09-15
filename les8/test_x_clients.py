import allure
from Python_DZ.Тренировка.les8.companyapi import CompanyApi
from Python_DZ.Тренировка.les8.company_table import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

@allure.id("SKYPRO-1")
@allure.story("Получение компаний")
@allure.epic("Компании")
@allure.feature("Read")
@allure.title("Получение полного списка организаций")
@allure.severity("TRIVIAL")
def test_get_companies():
    api_result = api.get_company_list()

    with allure.step("получить список компаний из БД"):    
        db_result = db.get_companies()

    with allure.step("сравнить размеры двух списков"):
        assert len(api_result) == len(db_result)
    

# Проверка получения активных компаний
@allure.id("SKYPRO-2")
@allure.story("Получение активных компаний")
@allure.epic("Компании")
@allure.feature("Read")
@allure.title("Получение полного списка активных организаций")
@allure.description("Запрос организаций c параметром activ = True")
def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)

 # Проверка добавления новой компании
@allure.id("SKYPRO-3")
@allure.story("Создание новой компании")
@allure.epic("Компании")
@allure.feature("Read")
@allure.title("Создание организаций")
@allure.severity("blocker")
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Auto555test"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    with allure.step("проверить поля новой организации, корректно заполнены"):
        found = False
        for company in body:
            if company["name"] == name:
                found = True
                assert company["description"] == descr
                break
                assert found
    
    body = api.get_company_list()
    len_after = len(body)

    with allure.step("Проверить что список ДО меньше списка ПОСЛЕ на 1"):
        assert len_after - len_before == 1

    with allure.step("Удаление из БД новую организацию"):
            db.delete(new_id)

@allure.id("SKYPRO-4")
@allure.story("Вызов компании")
@allure.epic("Компании")
@allure.feature("creat")
@allure.title("Вызов организаций по id")
def test_get_one_company():
    # Создаем компанию
    name = "garage"
    db.creat(name)
    max_id = db.get_max_id()

    # Обращаемся к компании
    new_company = api.get_company(max_id)
    db.delete(max_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    # assert new_company["description"] == description
    assert new_company["is_active"] is True

@allure.id("SKYPRO-5")
@allure.story("Редактирование названия компаний")
@allure.epic("Компании")
@allure.feature("update")
@allure.title("Редактирование организаций")
def test_edit():
    name = "garage"
    db.creat(name)
    max_id = db.get_max_id()

    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit_company(max_id, new_name, new_descr)
    db.delete(max_id)
    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr

@allure.id("SKYPRO-6")
@allure.story("Удаление компаний")
@allure.epic("Компании")
@allure.feature("delete")
@allure.title("Удаление организаций")
def test_delete():
    name = "garage"
    db.creat(name)
    max_id = db.get_max_id()

    # Обращаемся к компании
    new_company = api.get_company(max_id)
    # Проверим название, описание и статус компании:
    assert new_company["name"] == name
    assert new_company["is_active"] is True

    # Получаем список компаний и сохраняем его длину
    body = api.get_company_list()
    len_before = len(body)

    # Удаляем компанию
    deleted = api.delete_company(max_id)

    # Проверяем, что список компаний меньше на 1
    body = api.get_company_list()
    len_after = len(body)
    assert len_before - len_after == 1

    # Проверяем, что удаленная компания не находится по id
    deleted = api.get_company(max_id)
    assert deleted['detail'] == 'Компания не найдена'

@allure.id("SKYPRO-7")
@allure.story("Удаление компаний v.2")
@allure.epic("Компании")
@allure.feature("delete")
@allure.title("Удаление организаций")
def test_delete_p():
    # Добавили компанию через базу:
    name = "Skypro"
    db.creat(name)
    max_id = db.get_max_id()

    # Удалили компанию:
    deleted = api.delete_company(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

@allure.id("SKYPRO-8")
@allure.story("Деактивация компаний")
@allure.epic("Компании")
@allure.feature("is_activ")
@allure.title("Деактиваци организаций")
def test_deactivate():
    # Создаем компанию
    name = "Skypro"
    db.creat(name)
    max_id = db.get_max_id()
    # Деактивируем компанию
    body = api.set_active_state(max_id, False)
    db.delete(max_id)
    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False

@allure.id("SKYPRO-9")
@allure.story("Деактивация и активация компаний")
@allure.epic("Компании")
@allure.feature("is_activ")
@allure.title("активаци организаций")
def test_deactivate_and_activate_back():
    #Создаем компанию:
    name = "Skypro"
    db.creat(name)
    max_id = db.get_max_id()

    # Деактивируем компанию с помощью параметра False
    body_d = api.set_active_state(max_id, False)

    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(max_id, True)
    db.delete(max_id)
    # Проверяем, что компания активная
    assert body_a["is_active"] is True
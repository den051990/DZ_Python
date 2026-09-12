from Python_DZ.Тренировка.les8.companyapi import CompanyApi
from les9.company_table import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)
    

# Проверка получения активных компаний
def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)

 # Проверка добавления новой компании

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Auto555test"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1

    found = False
    for company in body:
        if company["name"] == name:
            found = True
            assert company["description"] == descr
            break

    assert found

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

def test_delete_p():
    # Добавили компанию через базу:
    name = "Skypro"
    db.creat(name)
    max_id = db.get_max_id()

    # Удалили компанию:
    deleted = api.delete_company(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

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
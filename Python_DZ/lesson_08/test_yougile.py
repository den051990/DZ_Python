from Python_DZ.lesson_08.api_yougile import ApiYougile

api = ApiYougile("https://yougile.com")

def test_activ_token():
    resp = api.get_token()

    assert resp == ""

def test_create_project_positive():
    api.get_token()
    title = "Учеба"
    resp = api.create_project(title)
    new_id = resp.json().get("id")

    assert resp.status_code == 201

    data = resp.json()

    assert "id" in data
    assert isinstance(data.get("id"), str)

def test_create_project_negative():
    api.get_token()
    title = ""
    resp = api.create_project(title)

    assert resp.status_code == 400

    data = resp.json()
    print("Тело ответа:", resp.json())

def test_redact_project_pozitive():
    api.get_token()
    title = "Старое задание"
    resp = api.create_project(title)
    project_id = resp.json().get("id")
    new_title = "Новое задание"
    redact = api.redact_project(project_id, new_title)

    assert redact.status_code == 200

    get_resp = api.get_project_id(project_id)
    assert get_resp.status_code == 200

    data_after_get = get_resp.json()
    assert data_after_get["title"] == new_title

def test_redact_project_negative():
    api.get_token()
    project_id = "0a0000cb-000c-0fe0-b000-d00000cea0a0"
    new_title = "Второе задание"
    redact = api.redact_project(project_id, new_title)

    assert redact.status_code == 404

    data = redact.json()
    print("Тело ответа:", redact.json())

def test_get_project_id_pozitive():
    api.get_token()
    title = "Третье задание"
    resp = api.create_project(title)
    project_id = resp.json().get("id")
    get_resp = api.get_project_id(project_id)

    assert get_resp.status_code == 200

    data = get_resp.json()
    returned_id = data["id"]

    assert returned_id == project_id

def test_get_project_id_negative():
    api.get_token()
    project_id = "0a0000cb-111c-0fe0-b000-d00000cea0a0"
    get_resp = api.get_project_id(project_id)

    assert get_resp.status_code == 404

    data = get_resp.json()
    print("Тело ответа:", get_resp.json())

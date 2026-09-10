import requests


class ApiYougile:
    def __init__(self, url) -> None:
        self.url = url

    def get_token(self, login='', password=''):
        creds = {
            "login": login,
            "password": password
        }
        resp = requests.post(
            self.url + '/api-v2/auth/keys/get', json=creds)
        return resp.json()[0]["key"]

    def get_company_list(self, params_to_add=None):
        resp = requests.get(
            self.url + '/api-v2/projects', params=params_to_add)
        return resp.json()

    def create_project(self, title):
        token = self.get_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token}
        project_new = {"title": title}
        resp = requests.post(self.url + '/api-v2/projects', json=project_new,
                             headers=headers)
        return resp

    def redact_project(self, project_id, new_title):
        token = self.get_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        new_project = {"title": new_title}

        resp = requests.put(f"{self.url}/api-v2/projects/{project_id}",
                            json=new_project, headers=headers)
        return resp

    def get_project_id(self, project_id):
        token = self.get_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        url = f"{self.url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=headers)

import json


class Config:
    def __init__(self):
        data = self.read_file()
        self.email = data['email']
        self.password = data['password']
        self.name = data['name']
        self.base_url = "https://mail.ru/"

    def read_file(self):
        with open('../userdata.json', 'r', encoding='utf-8') as userdata:
            return json.loads(userdata.read())

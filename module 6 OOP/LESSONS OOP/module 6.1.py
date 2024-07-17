class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __del__(self):
        DataBase._instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Cоединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие БД")

    def read(self):
        print("Данные из БД")

    def write(self, data):
        print(f"Запись в БД {data}")

db = DataBase("root", 123312, 8080)
db2 = DataBase("root2", 1201, 4400)
print(db)
print(db2)
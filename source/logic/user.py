import csv

from PyQt5.QtCore import QObject, pyqtSignal


class UserManager(QObject):
    signal_failed_login = pyqtSignal(str)
    signal_failed_register = pyqtSignal(str)
    signal_success_login = pyqtSignal()
    signal_success_register = pyqtSignal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def login(self, data):
        success = False

        with open(self.path, "r", encoding="utf-8") as file:
            users = csv.DictReader(file)

            for user in users:
                user = dict(user)

                if data["user"] == user["user"]:
                    if data["hash"] == user["hash"]:
                        success = True
                        self.signal_success_login.emit()
                        break
                    else:
                        break

        if not success:
            self.signal_failed_login.emit("Usuario o contraseña incorrecta")

    def register(self, data):
        found = False

        with open(self.path, "r", encoding="utf-8") as file:
            users = csv.DictReader(file)

            for user in users:
                user = dict(user)

                if user["user"] == data["user"]:
                    found = True
                    self.signal_failed_register.emit("El nombre de usuario ya existe")
                    break

        if not found:
            with open(self.path, "a", encoding="utf-8") as file:
                file.write(f"{data['user']},{data['hash']}\n")

            self.signal_success_register.emit("Registrado con éxito")

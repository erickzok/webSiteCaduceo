from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, idEmpleado, username, password, idRol, fullname="") -> None:
        self.idEmpleado = idEmpleado
        self.username = username
        self.password = password
        self.idRol    = idRol
        self.fullname = fullname
    def get_id(self):
        return int(self.idEmpleado)
    def get_idRol(self):
        return int(self.idRol)
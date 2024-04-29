from MySQLdb import IntegrityError
from flask_login import UserMixin


class newUser(UserMixin):

    def __init__(self, db, idEmpleado, username, password, dni , fullname=""):
        self.db = db
        self.idEmpleado = idEmpleado
        self.username = username
        self.password = password
        self.dni = dni
        self.fullname = fullname

    def get_id(self):
        return str(self.idEmpleado)

    def insertar_en_tablas(self):
        cursor = self.db.connection.cursor()
        error_message = None
        
        try:
            # Insertar en la tabla empleado
            cursor.execute("INSERT INTO empleado (nombreEmpleado, dni) VALUES (%s, %s)",
                        (self.fullname, self.dni))
            
            # Obtener el ID del empleado insertado
            new_id_empleado = cursor.lastrowid
            
            # Insertar en la tabla usuario
            cursor.execute("INSERT INTO usuario (Usuario, contrasena, idEmpleado) VALUES (%s, %s, %s)",
                        (self.username, self.password, new_id_empleado))
            
            self.db.connection.commit()
            return True, None
        except IntegrityError as e:
            self.db.connection.rollback()
            error_message = "Error: El nombre de usuario ya existe. Por favor, elige otro nombre de usuario."
            return False, error_message
        except Exception as e:
            self.db.connection.rollback()
            error_message = "Error al insertar en las tablas: {}".format(str(e))
            return False, error_message
        finally:
            cursor.close()



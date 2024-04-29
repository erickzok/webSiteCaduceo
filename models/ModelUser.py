from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = f"SELECT u.idEmpleado, u.usuario, u.contrasena, e.nombreEmpleado , u.idRol FROM usuario as u JOIN  empleado as e on u.idEmpleado = e.idEmpleado WHERE u.usuario = '{user.username}' "
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:  
                if row[2]== user.password:
                    user = User(row[0], row[1], row[2], row[4], row[3])

                    print(row[4])
                    print(row[3])
                    print(user.get_idRol())
                    print("Ingreso correcto")
                    return user
                else :
                    print("contraseña incorrecta")
                    return None
            else:
                print("No existe usuario")
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = f"SELECT u.idEmpleado, u.usuario, u.contrasena, e.nombreEmpleado ,u.idRol FROM usuario as u JOIN  empleado as e on u.idEmpleado = e.idEmpleado WHERE u.idEmpleado = {id}"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], row[4], row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

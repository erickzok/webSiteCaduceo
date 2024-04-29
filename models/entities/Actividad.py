
from flask_login import UserMixin

class Actividad(UserMixin):

    def __init__(self, db, proyecto, JefeInmediato, actividad, Porcentaje, FechaFin, hora, FechaRegistro, comentarios="",idActividad=None, idEmpleado=None) -> None:
        self.db=db
        self.idActividad = idActividad
        self.proyecto = proyecto
        self.JefeInmediato = JefeInmediato
        self.actividad = actividad
        self.Porcentaje = Porcentaje
        self.FechaFin = FechaFin
        self.hora = hora
        self.FechaRegistro = FechaRegistro
        self.comentarios = comentarios
        self.idEmpleado = idEmpleado

    def insertar_actividad(self):
        print("Realizando insercion")
        cursor = self.db.connection.cursor()

        cursor.execute("INSERT INTO actividad (proyecto, JefeInmediato, actividad, Porcentaje, FechaFin, hora, FechaRegistro, comentarios, idEmpleado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (self.proyecto, self.JefeInmediato, self.actividad, self.Porcentaje, self.FechaFin, self.hora, self.FechaRegistro, self.comentarios, self.idEmpleado))
        self.db.connection.commit()
        self.idActividad = cursor.lastrowid



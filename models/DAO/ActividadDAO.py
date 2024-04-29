import MySQLdb
from models.entities.Actividad import Actividad
class ActividadDAO:
    def __init__(self, db, id):
        self.db = db
        self.id=id

    def get_all_actividades(self):
        print("obtencion de actividades")
        cursor = self.db.connection.cursor()
        cursor.execute(f"SELECT idActividad, proyecto, JefeInmediato, actividad, Porcentaje, FechaFin, hora, FechaRegistro FROM actividad WHERE idEmpleado={self.id}")
        actividades = []
        for row in cursor.fetchall():
            actividad = Actividad(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            actividades.append(actividad)
        print(actividades)
        return actividades
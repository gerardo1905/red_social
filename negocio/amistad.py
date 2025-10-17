from datos.conexion import obtener_conexion
from datetime import date

class Amistad:
    def __init__(self, id_usuario_1, id_usuario_2):
        self.id_usuario_1 = id_usuario_1
        self.id_usuario_2 = id_usuario_2

    def solicitar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO amistad (id_usuario_1, id_usuario_2, estado, fecha_inicio) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.id_usuario_1, self.id_usuario_2, 'pendiente', date.today()))
        conexion.commit()
        conexion.close()
        print("🤝 Solicitud de amistad enviada.")

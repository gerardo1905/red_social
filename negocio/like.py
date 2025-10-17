from datos.conexion import obtener_conexion
from datetime import datetime

class Like:
    def __init__(self, id_publicacion, id_usuario):
        self.id_publicacion = id_publicacion
        self.id_usuario = id_usuario

    def dar_like(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT IGNORE INTO `like` (id_publicacion, id_usuario, fecha_hora) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.id_publicacion, self.id_usuario, datetime.now()))
        conexion.commit()
        conexion.close()
        print("👍 Like registrado.")

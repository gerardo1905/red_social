from datos.conexion import obtener_conexion
from datetime import datetime
from mysql.connector import Error

class Comentario:
    def __init__(self, id_publicacion, id_usuario, contenido):
        self.id_publicacion = id_publicacion
        self.id_usuario = id_usuario
        self.contenido = contenido

    def guardar(self):
        """Guarda un nuevo comentario en la base de datos."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql = """
                INSERT INTO comentarios (id_publicacion, id_usuario, texto, fecha_hora)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (self.id_publicacion, self.id_usuario, self.contenido, datetime.now()))
            conexion.commit()
            print("Comentario agregado correctamente.")
        except Error as e:
            print("Error al guardar comentario:", e)
        finally:
            try:
                cursor.close()
                conexion.close()
            except:
                pass

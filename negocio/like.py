from datos.conexion import obtener_conexion
from datetime import datetime

def guardar_like(id_publicacion, id_usuario):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        # Si renombraste la tabla a 'likes', usa FROM likes; si no, mantén `like` entre backticks pero no es ideal.
        sql = "INSERT IGNORE INTO likes (id_publicacion, id_usuario, fecha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id_publicacion, id_usuario, datetime.now()))
        conexion.commit()
        filas = cursor.rowcount if hasattr(cursor, "rowcount") else "n/a"
        cursor.close()
        conexion.close()
        print(" Like registrado. Filas afectadas:", filas)
        return True
    except Exception as e:
        print("Error al guardar like:", repr(e))
        try:
            cursor.close()
        except Exception:
            pass
        try:
            conexion.close()
        except Exception:
            pass
        return False

class Like:
    def __init__(self, id_publicacion, id_usuario):
        self.id_publicacion = id_publicacion
        self.id_usuario = id_usuario

    def dar_like(self):
        return guardar_like(self.id_publicacion, self.id_usuario)

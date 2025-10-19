from datos.conexion import obtener_conexion
from mysql.connector import Error
from datetime import datetime

print(">>> Cargando módulo: negocio.amistad")

class Amistad:
    def __init__(self, id_usuario1, id_usuario2):
        self.id_usuario_1 = id_usuario1
        self.id_usuario_2 = id_usuario2

    def guardar(self):
        """Registra una nueva amistad entre dos usuarios."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql = """
                INSERT IGNORE INTO amistad (id_usuario_1, id_usuario_2, fecha_inicio)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (self.id_usuario_1, self.id_usuario_2, datetime.now()))
            conexion.commit()
            print(" Amistad registrada correctamente.")
        except Error as e:
            print(" Error al guardar amistad:", e)
        finally:
            try:
                cursor.close()
                conexion.close()
            except Exception:
                pass

    # ¡Alineación de @staticmethod y def listar_amistades() debe ser PERFECTA!
    @staticmethod
    def listar_amistades():
        """Obtiene todas las amistades registradas."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT a.id,
                    u1.nombre AS usuario1,
                    u2.nombre AS usuario2,
                    a.fecha_inicio
                FROM amistad a
                JOIN usuarios u1 ON a.id_usuario_1 = u1.id
                JOIN usuarios u2 ON a.id_usuario_2 = u2.id
                ORDER BY a.fecha_inicio DESC
            """
            cursor.execute(sql)
            amistades = cursor.fetchall()
            conexion.close()
            return amistades
        except Error as e:
            print(" Error al listar amistades:", e)
            return []
            
print(">>> Clase Amistad cargada correctamente.")
from datos.conexion import obtener_conexion
from datetime import datetime
from mysql.connector import Error

class Mensaje:
    def __init__(self, id_emisor, id_receptor, contenido):
        self.id_emisor = id_emisor
        self.id_receptor = id_receptor
        self.contenido = contenido

    def enviar(self):
        """Guarda un nuevo mensaje privado."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql = """
                INSERT INTO mensajes (contenido, id_emisor, id_receptor, fecha_hora, leido)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (self.contenido, self.id_emisor, self.id_receptor, datetime.now(), False))
            conexion.commit()
            print("Mensaje enviado correctamente.")
        except Error as e:
            print("Error al enviar mensaje:", e)
        finally:
            try:
                cursor.close()
                conexion.close()
            except:
                pass

    @staticmethod
    def listar_mensajes(id_usuario):
        """Lista todos los mensajes recibidos por un usuario y los marca como leídos."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor(dictionary=True)

            # Obtener mensajes
            sql_select = """
                SELECT m.id, u.nombre AS emisor, m.contenido, m.fecha_hora, m.leido
                FROM mensajes m
                JOIN usuarios u ON m.id_emisor = u.id
                WHERE m.id_receptor = %s
                ORDER BY m.fecha_hora DESC
            """
            cursor.execute(sql_select, (id_usuario,))
            mensajes = cursor.fetchall()

            # Marcar como leídos
            if mensajes:
                sql_update = """
                    UPDATE mensajes
                    SET leido = TRUE
                    WHERE id_receptor = %s AND leido = FALSE
                """
                cursor.execute(sql_update, (id_usuario,))
                conexion.commit()

            return mensajes

        except Error as e:
            print("Error al listar mensajes:", e)
            return []
        finally:
            try:
                cursor.close()
                conexion.close()
            except:
                pass

    @staticmethod
    def listar_no_leidos(id_usuario):
        """Muestra solo los mensajes no leídos por un usuario."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT m.id, u.nombre AS emisor, m.contenido, m.fecha_hora
                FROM mensajes m
                JOIN usuarios u ON m.id_emisor = u.id
                WHERE m.id_receptor = %s AND m.leido = FALSE
                ORDER BY m.fecha_hora DESC
            """
            cursor.execute(sql, (id_usuario,))
            mensajes = cursor.fetchall()
            return mensajes
        except Error as e:
            print("Error al listar mensajes no leídos:", e)
            return []
        finally:
            try:
                cursor.close()
                conexion.close()
            except:
                pass



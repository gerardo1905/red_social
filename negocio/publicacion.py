from datos.conexion import obtener_conexion
from datetime import datetime

class Publicacion:
    def __init__(self, id_autor, contenido, tipo="texto"):
        self.id_autor = id_autor
        self.contenido = contenido
        self.tipo = tipo

    def guardar(self):
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            # usar la tabla 'publicaciones' (plural)
            sql = "INSERT INTO publicaciones (contenido, id_autor, tipo, fecha) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.contenido, self.id_autor, self.tipo, datetime.now()))
            conexion.commit()
            cursor.close()
            conexion.close()
            print(" Publicación creada con éxito.")
        except Exception as e:
            print("Error al guardar publicación:", repr(e))
            raise

    @staticmethod
    def listar_publicaciones():
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            # usar 'publicaciones' y 'usuarios' (plural)
            cursor.execute("""
                SELECT p.id, p.contenido, p.fecha, u.nombre AS autor
                FROM publicaciones p
                JOIN usuarios u ON p.id_autor = u.id
                ORDER BY p.fecha DESC
            """)
            publicaciones = cursor.fetchall()
            cursor.close()
            conexion.close()
            return publicaciones
        except Exception as e:
            print("Error al listar publicaciones:", repr(e))
            raise

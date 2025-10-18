from datos.conexion import obtener_conexion
from datetime import datetime

class Publicacion:
    def __init__(self, id_autor, contenido, tipo="texto"):
        self.id_autor = id_autor
        self.contenido = contenido
        self.tipo = tipo

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO publicacion (contenido, id_autor, tipo, fecha) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.contenido, self.id_autor, self.tipo, datetime.now()))
        conexion.commit()
        conexion.close()
        print("✅ Publicación Creada con Exito.")

    @staticmethod
    def listar_publicaciones():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id, p.contenido, p.fecha, u.nombre AS autor
            FROM publicacion p
            JOIN usuario u ON p.id_autor = u.id
            ORDER BY p.fecha DESC
        """)
        publicaciones = cursor.fetchall()
        conexion.close()
        return publicaciones

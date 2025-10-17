from datos.conexion import obtener_conexion
from datetime import date

class Usuario:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def registrar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuario (nombre, correo, password, fecha_registro) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.nombre, self.correo, self.password, date.today()))
        conexion.commit()
        conexion.close()
        print("✅ Usuario registrado con éxito.")

    @staticmethod
    def listar_usuarios():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, correo, fecha_registro FROM usuario")
        usuarios = cursor.fetchall()
        conexion.close()
        return usuarios

from datos.conexion import obtener_conexion

class Usuario:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def registrar(self):
        print("DEBUG: entrar a Usuario.registrar() con:", self.nombre, self.correo)
        try:
            conn = obtener_conexion()
            cur = conn.cursor()
            sql = "INSERT INTO usuarios (nombre, correo, password, fecha_registro) VALUES (%s, %s, %s, NOW())"
            cur.execute(sql, (self.nombre, self.correo, self.password))
            conn.commit()
            filas = cur.rowcount if hasattr(cur, "rowcount") else "n/a"
            cur.close()
            conn.close()
            print("DEBUG: inserción realizada OK, filas afectadas:", filas)
            return True
        except Exception as e:
            print("DEBUG: excepción en Usuario.registrar():", repr(e))
            raise

    @staticmethod
    def listar_usuarios():
        """Devuelve lista de diccionarios desde la tabla 'usuarios'."""
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT id, nombre, correo, fecha_registro FROM usuarios")
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        except Exception as e:
            print("DEBUG: excepción en listar_usuarios():", repr(e))
            raise

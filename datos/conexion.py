from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import mysql.connector
from mysql.connector import Error

# Herramientas necesarias para trabajar con DB
# pip install sqlalchemy
# pip install mysql-connector-python

# Definir cadena de conexion
# mysql+mysqlconnector://user:password@host:port/database_name
# Reemplazar user, password, host, port, y database con sus credenciales de DB

DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/red_social"
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)

# Leer credenciales (mejor: ponerlas en variables de entorno)
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")  # si no hay contraseña, dejar vacío
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "red_social")


def obtener_conexion():
    """Devuelve una conexión mysql.connector.connect — lanzar excepción si falla."""
    try:
        conn = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )
        return conn
    except Error as e:
        # Re-lanzar para que el import muestre el error completo
        raise


# Prueba rápida al ejecutar el archivo directamente
if __name__ == "__main__":
    try:
        c = obtener_conexion()
        print("Conexión MySQL OK")
        c.close()
    except Exception as e:
        print("Fallo al conectar:", e)


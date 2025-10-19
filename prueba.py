from datos.conexion import obtener_conexion

if __name__ == "__main__":
    try:
        c = obtener_conexion()
        print("Conexión MySQL exitosa")
        c.close()
    except Exception as e:
        print("Fallo al conectar:", e)
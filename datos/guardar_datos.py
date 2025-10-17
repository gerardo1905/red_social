from datos.conexion import Session
from sqlalchemy import func



# def guardar_modelo():
#     nombre = input('Ingrese nombre marca: ')
#     marca = obtener_marca_nombre(nombre)
#     if not marca:
#         guardar_marca()
#     modelo = input('Ingrese nombre del modelo: ')
#     descripcion = input('Ingrese descripción del modelo: ')
#     tipo_combustible = input('Ingrese tipo de combustible: ')
#     combustible = obtener_combustible_nombre(tipo_combustible)
#     nuevo_modelo = Modelo(
#         nombre_modelo=modelo.title(),
#         descripcion_modelo=descripcion.title())
#     sesion.add(nuevo_modelo)
#     try:
#         sesion.commit()
#         print(
#             f"La marca '{nuevo_modelo.nombre_marca}' se ha guardado correctamente.")
#     except Exception as e:
#         sesion.rollback()
#         print(f"Error al guardar la marca: {e}")
#     finally:
#         sesion.close()
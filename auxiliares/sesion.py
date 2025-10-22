
usuario_actual = None  # Guardará el ID del usuario logeado

def iniciar_sesion(id_usuario):
    global usuario_actual
    usuario_actual = id_usuario

def obtener_usuario_actual():
    return usuario_actual

def cerrar_sesion():
    global usuario_actual
    usuario_actual = None

import traceback
from negocio.usuario import Usuario
from negocio.like import guardar_like

def alguna_funcion():
    print("Función definida en principal ejecutada")

def registrar_usuario_cb(nombre, correo, password):
    try:
        u = Usuario(nombre, correo, password)
        if hasattr(u, "registrar"):
            u.registrar()
            print("Usuario registrado desde callback.")
        elif hasattr(Usuario, "registrar"):
            Usuario.registrar(u)
            print("Usuario registrado (método en la clase).")
        else:
            print("No existe método 'registrar' en Usuario.")
    except Exception as e:
        print("Error al registrar usuario:", e)
        traceback.print_exc()

try:
    from iu.menu_principal import mostrar_menu
except Exception:
    print("Fallo al importar iu.menu_principal:")
    traceback.print_exc()
    raise

if __name__ == "__main__":
    try:
        actions = {
            "registrar_usuario": registrar_usuario_cb,
            "opcion1": alguna_funcion,
        }
        mostrar_menu(actions)
        print(guardar_like(1, 1))
    except Exception:
        print("Error al ejecutar mostrar_menu():")
        traceback.print_exc()
        raise

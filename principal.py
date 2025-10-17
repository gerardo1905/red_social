import traceback

def alguna_funcion():
    print("Función definida en principal ejecutada")

try:
    from iu.menu_principal import mostrar_menu
except Exception:
    print("Fallo al importar iu.menu_principal:")
    traceback.print_exc()
    raise

if __name__ == "__main__":
    try:
        actions = {
            "opcion1": alguna_funcion,
            # "opcion2": otra_funcion,  # añade más callbacks si hace falta
        }
        mostrar_menu(actions)
    except Exception:
        print("Error al ejecutar mostrar_menu():")
        traceback.print_exc()
        raise

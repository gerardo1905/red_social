from auxiliares.informacion_app import nombre_aplicacion
from negocio.usuario import Usuario
from negocio.publicacion import Publicacion
from negocio.like import Like
from negocio.amistad import Amistad

def mostrar_menu(actions=None):
    """Mostrar menú e invocar callbacks opcionales pasados en `actions`."""
    while True:
        print("\n===============================")
        print(f"     🌐 {nombre_aplicacion.upper()}      ")
        print("===============================")
        print("1. Registrar usuario")
        print("2. Ver usuarios registrados")
        print("3. Crear publicación")
        print("4. Ver publicaciones")
        print("5. Dar 'Me gusta' a una publicación")
        print("6. Enviar solicitud de amistad")
        print("7. Ver amistades")
        print("0. Salir")
        print("===============================\n")

        opcion = input("👉 Elige una opción: ").strip()

        if opcion == "0":
            print("Saliendo...")
            break

        # 1 - Registrar usuario
        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            password = input("Contraseña: ")
            if actions and callable(actions.get("registrar_usuario")):
                actions["registrar_usuario"](nombre, correo, password)
            else:
                try:
                    u = Usuario(nombre, correo, password)
                    u.registrar()
                except Exception as e:
                    print("Error al registrar usuario:", e)

        # 2 - Ver usuarios
        elif opcion == "2":
            if actions and callable(actions.get("listar_usuarios")):
                usuarios = actions["listar_usuarios"]()
            else:
                try:
                    usuarios = Usuario.listar_usuarios()
                except Exception as e:
                    print("Error al listar usuarios:", e)
                    usuarios = []
            print("\n👥 Usuarios registrados:")
            for u in usuarios:
                try:
                    print(f"ID: {u['id']} | Nombre: {u['nombre']} | Correo: {u['correo']} | Fecha: {u.get('fecha_registro','')}")
                except Exception:
                    print(u)

        # 3 - Crear publicación
        elif opcion == "3":
            try:
                id_autor = int(input("ID del usuario que publica: "))
            except ValueError:
                print("ID inválido.")
                continue
            contenido = input("Escribe el contenido de la publicación: ")
            if actions and callable(actions.get("crear_publicacion")):
                actions["crear_publicacion"](id_autor, contenido)
            else:
                try:
                    p = Publicacion(id_autor, contenido)
                    # método esperado: crear() / guardar() / registrar(); probar en orden
                    if hasattr(p, "crear"):
                        p.crear()
                    elif hasattr(p, "guardar"):
                        p.guardar()
                    elif hasattr(p, "registrar"):
                        p.registrar()
                    else:
                        print("Función para guardar publicación no encontrada en Publicacion.")
                except Exception as e:
                    print("Error al crear publicación:", e)

        # 4 - Ver publicaciones
        elif opcion == "4":
            if actions and callable(actions.get("listar_publicaciones")):
                publicaciones = actions["listar_publicaciones"]()
            else:
                try:
                    publicaciones = Publicacion.listar_publicaciones()
                except Exception as e:
                    print("Error al listar publicaciones:", e)
                    publicaciones = []
            print("\n📝 Publicaciones:")
            for p in publicaciones:
                print(p)

        # 5 - Dar like
        elif opcion == "5":
            try:
                id_pub = int(input("ID de la publicación: "))
                id_usr = int(input("Tu ID de usuario: "))
            except ValueError:
                print("ID inválido.")
                continue
            if actions and callable(actions.get("dar_like")):
                actions["dar_like"](id_pub, id_usr)
            else:
                try:
                    like = Like(id_pub, id_usr)
                    like.dar_like()
                except Exception as e:
                    print("Error al dar like:", e)

        # 6 - Enviar amistad
        elif opcion == "6":
            try:
                id_origen = int(input("Tu ID: "))
                id_destino = int(input("ID del usuario a quien enviar solicitud: "))
            except ValueError:
                print("ID inválido.")
                continue
            if actions and callable(actions.get("enviar_amistad")):
                actions["enviar_amistad"](id_origen, id_destino)
            else:
                try:
                    a = Amistad(id_origen, id_destino)
                    if hasattr(a, "enviar_solicitud"):
                        a.enviar_solicitud()
                    elif hasattr(a, "solicitar"):
                        a.solicitar()
                    else:
                        print("Método para enviar solicitud no encontrado en Amistad.")
                except Exception as e:
                    print("Error al enviar amistad:", e)

        # 7 - Ver amistades
        elif opcion == "7":
            if actions and callable(actions.get("listar_amistades")):
                amistades = actions["listar_amistades"]()
            else:
                try:
                    amistades = Amistad.listar_amistades()
                except Exception as e:
                    print("Error al listar amistades:", e)
                    amistades = []
            print("\n🤝 Amistades:")
            for a in amistades:
                print(a)

        else:
            print("Opción no válida. Intenta de nuevo.")



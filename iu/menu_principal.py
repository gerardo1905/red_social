from auxiliares.informacion_app import nombre_aplicacion
from auxiliares.sesion import iniciar_sesion, obtener_usuario_actual, cerrar_sesion
from negocio.usuario import Usuario
from negocio.publicacion import Publicacion
from negocio.like import Like
from negocio.amistad import Amistad
from auxiliares.version import numero_version


def mostrar_menu(actions=None):
    # Inicio de sesión básico
    try:
        print(f"Bienvenido a {nombre_aplicacion} (v{numero_version})"
        )
        id_usuario_actual = int(input("Ingresa tu ID de usuario para iniciar sesión: "))
        iniciar_sesion(id_usuario_actual)
    except ValueError:
        print("ID inválido. Se usará ID = 1 por defecto.")
        iniciar_sesion(1)

    # Notificación breve de mensajes nuevos
    try:
        from negocio.mensaje import Mensaje
        mensajes_nuevos = Mensaje.listar_no_leidos(obtener_usuario_actual())
        if mensajes_nuevos:
            print(f"Tienes {len(mensajes_nuevos)} mensaje(s) nuevos sin leer.\n")
        else:
            print("No tienes mensajes nuevos.\n")
    except Exception:
        pass

    # Menú principal
    while True:
        print("\n===============================")
        print(f"      {nombre_aplicacion.upper()} ")
        print("===============================")
        print("1. Registrar usuario")
        print("2. Ver usuarios registrados")
        print("3. Crear publicación")
        print("4. Ver publicaciones")
        print("5. Dar 'Me gusta' a una publicación")
        print("6. Enviar solicitud de amistad")
        print("7. Ver amistades")
        print("8. Agregar comentario a una publicación")
        print("9. Enviar mensaje privado")
        print("10. Ver mensajes recibidos")
        print("11. Ver solo mensajes no leídos")
        print("0. Salir")
        print("===============================\n")

        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            cerrar_sesion()
            print("Sesión cerrada. Hasta pronto.")
            break

        elif opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            password = input("Contraseña: ")
            try:
                u = Usuario(nombre, correo, password)
                u.registrar()
                print("Usuario registrado correctamente.")
            except Exception as e:
                print("Error al registrar usuario:", e)

        elif opcion == "2":
            try:
                usuarios = Usuario.listar_usuarios()
                print("\nUsuarios registrados:")
                for u in usuarios:
                    print(f"ID: {u['id']} | Nombre: {u['nombre']} | Correo: {u['correo']}")
            except Exception as e:
                print("Error al listar usuarios:", e)

        elif opcion == "3":
            try:
                id_autor = obtener_usuario_actual()
                contenido = input("Escribe el contenido de la publicación: ")
                p = Publicacion(id_autor, contenido)
                p.guardar()
                print("Publicación creada correctamente.")
            except Exception as e:
                print("Error al crear publicación:", e)

        elif opcion == "4":
            try:
                publicaciones = Publicacion.listar_publicaciones()
                print("\nPublicaciones:")
                for p in publicaciones:
                    print(p)
            except Exception as e:
                print("Error al listar publicaciones:", e)

        elif opcion == "5":
            try:
                id_pub = int(input("ID de la publicación: "))
                id_usr = obtener_usuario_actual()
                like = Like(id_pub, id_usr)
                like.dar_like()
            except Exception as e:
                print("Error al dar like:", e)

        elif opcion == "6":
            try:
                id_origen = obtener_usuario_actual()
                id_destino = int(input("ID del usuario a quien enviar solicitud: "))
                a = Amistad(id_origen, id_destino)
                a.guardar()
                print("Solicitud de amistad enviada.")
            except Exception as e:
                print("Error al enviar amistad:", e)

        elif opcion == "7":
            try:
                amistades = Amistad.listar_amistades()
                print("\nAmistades registradas:")
                for a in amistades:
                    print(a)
            except Exception as e:
                print("Error al listar amistades:", e)

        elif opcion == "8":
            try:
                id_pub = int(input("ID de la publicación a comentar: "))
                id_user = obtener_usuario_actual()
                texto = input("Escribe tu comentario: ")
                from negocio.comentario import Comentario
                c = Comentario(id_pub, id_user, texto)
                c.guardar()
                print("Comentario guardado con éxito.")
            except Exception as e:
                print("Error al agregar comentario:", e)

        elif opcion == "9":
            try:
                id_emisor = obtener_usuario_actual()
                id_receptor = int(input("ID del usuario receptor: "))
                contenido = input("Escribe tu mensaje: ")
                from negocio.mensaje import Mensaje
                m = Mensaje(id_emisor, id_receptor, contenido)
                m.enviar()
                print("Mensaje enviado correctamente.")
            except Exception as e:
                print("Error al enviar mensaje:", e)

        elif opcion == "10":
            try:
                id_user = obtener_usuario_actual()
                from negocio.mensaje import Mensaje
                mensajes = Mensaje.listar_mensajes(id_user)
                print("\nMensajes recibidos:")
                if not mensajes:
                    print("No tienes mensajes.")
                for msg in mensajes:
                    estado = "Leído" if msg["leido"] else "No leído"
                    print(f"De: {msg['emisor']} | {msg['contenido']} | {estado} | {msg['fecha_hora']}")
            except Exception as e:
                print("Error al mostrar mensajes:", e)

        elif opcion == "11":
            try:
                id_user = obtener_usuario_actual()
                from negocio.mensaje import Mensaje
                mensajes = Mensaje.listar_no_leidos(id_user)
                print("\nMensajes no leídos:")
                if not mensajes:
                    print("No tienes mensajes nuevos.")
                for msg in mensajes:
                    print(f"De: {msg['emisor']} | {msg['contenido']} | {msg['fecha_hora']}")
            except Exception as e:
                print("Error al mostrar mensajes no leídos:", e)

        else:
            print("Opción no válida. Intenta de nuevo.")

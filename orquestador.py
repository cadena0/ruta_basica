from ingreso_session import leer_usuarios , validar_login 
from crud import crear_equipo,listar_equipos,actualizar_equipo,eliminar_equipo
def menu_crud():
    while True:
        print("\n===== MENÚ CRUD DE EQUIPOS =====")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Actualizar equipo")
        print("4. Eliminar equipo")
        print("5. Cerrar sesión")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            actualizar_equipo()
        elif opcion == "4":
            eliminar_equipo()
        elif opcion == "5":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")


def main():
    print("=== SISTEMA DE LOGIN ===")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    if validar_login(usuario, password,usuario):
        print("Inicio de sesión exitoso.")
        menu_crud()
    else:
        print("Credenciales incorrectas. Saliendo del programa.")


if __name__ == "__main__":
    main()

equipos = []  

def crear_equipo():
    nombre = input("Nombre del equipo: ")
    ciudad = input("Ciudad: ")

    equipos.append({
        "nombre": nombre,
        "ciudad": ciudad
    })
    print("Equipo creado con éxito.")


def listar_equipos():
    if not equipos:
        print("No hay equipos registrados.")
        return

    print("\n--- LISTA DE EQUIPOS ---")
    for i, eq in enumerate(equipos):
        print(f"{i+1}. {eq['nombre']} ({eq['ciudad']})")
    print()


def actualizar_equipo():
    listar_equipos()
    if not equipos:
        return

    indice = int(input("Número del equipo a actualizar: ")) - 1

    if 0 <= indice < len(equipos):
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_ciudad = input("Nueva ciudad: ")

        equipos[indice]["nombre"] = nuevo_nombre
        equipos[indice]["ciudad"] = nueva_ciudad

        print("Equipo actualizado con éxito.")
    else:
        print("Índice inválido.")


def eliminar_equipo():
    listar_equipos()
    if not equipos:
        return

    indice = int(input("Número del equipo a eliminar: ")) - 1

    if 0 <= indice < len(equipos):
        equipos.pop(indice)
        print("Equipo eliminado.")
    else:
        print("Índice inválido.")
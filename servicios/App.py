from servicio import *
from archivos import *
import os

# Crear carpeta para guardar archivos si no existe
if not os.path.exists("Semana3"):
    os.makedirs("Semana3")

lista_productos = []

while True:
    print("""
--------- MENÚ ---------
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Ver estadísticas
7. Guardar inventario
8. Cargar inventario
9. Salir
------------------------
""")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = input("Precio del producto: ")
        cantidad = input("Cantidad del producto: ")
        agregar_producto(lista_productos, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(lista_productos)

    elif opcion == "3":
        nombre_busqueda = input("Nombre del producto a buscar: ")
        producto_encontrado = buscar_producto(lista_productos, nombre_busqueda)
        if producto_encontrado:
            print("Producto encontrado:", producto_encontrado)
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        nombre_busqueda = input("Producto a actualizar: ")
        nuevo_precio = input("Nuevo precio (Enter para no cambiar): ")
        nueva_cantidad = input("Nueva cantidad (Enter para no cambiar): ")

        actualizar_producto(
            lista_productos,
            nombre_busqueda,
            float(nuevo_precio) if nuevo_precio else None,
            int(nueva_cantidad) if nueva_cantidad else None
        )

    elif opcion == "5":
        nombre_busqueda = input("Producto a eliminar: ")
        eliminar_producto(lista_productos, nombre_busqueda)

    elif opcion == "6":
        calcular_estadisticas(lista_productos)

    elif opcion == "7":
        archivo_destino = "Semana3/inventario.csv"
        exportar_inventario_csv(lista_productos, archivo_destino)
        print("Inventario guardado correctamente.")

    elif opcion == "8":
        archivo_origen = "data/inventario.csv"
        productos_nuevos, productos_no_leidos = leer_inventario_csv(archivo_origen)

        if productos_nuevos is None:
            print("No se pudo leer el archivo, revisa que exista.")
            continue

        print(f"{len(productos_nuevos)} productos leídos, {productos_no_leidos} no se pudieron leer.")

        decision = input("¿Deseas reemplazar el inventario actual con estos productos? (S/N): ").upper()

        if decision == "S":
            lista_productos = productos_nuevos
            print("Inventario actualizado con los productos del archivo.")
        else:
            print("Agregando productos del archivo al inventario actual...")
            for producto in productos_nuevos:
                producto_en_lista = buscar_producto(lista_productos, producto["nombre"])
                if producto_en_lista:
                    producto_en_lista["cantidad"] += producto["cantidad"]
                    producto_en_lista["precio"] = producto["precio"]
                else:
                    lista_productos.append(producto)
            print("Productos agregados al inventario actual.")

    elif opcion == "9":
        print("Fin del programa.")
        break

    else:
        print("Opción inválida. Intenta otra vez.")
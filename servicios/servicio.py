def agregar_producto(lista_productos, nombre, precio, cantidad):
    """
    Agrega un producto a la lista de productos.
    """
    producto = {
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    lista_productos.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")


def mostrar_inventario(lista_productos):
    """
    Muestra todos los productos de la lista de productos.
    """
    if len(lista_productos) == 0:
        print("El inventario está vacío.")
        return
    
    print("\n--- INVENTARIO ---")
    for producto in lista_productos:
        print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    print("------------------\n")


def buscar_producto(lista_productos, nombre_busqueda):
    """
    Busca un producto por nombre y lo retorna si existe.
    """
    for producto in lista_productos:
        if producto["nombre"].lower() == nombre_busqueda.lower():
            return producto
    return None


def actualizar_producto(lista_productos, nombre_busqueda, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto existente.
    """
    producto_encontrado = buscar_producto(lista_productos, nombre_busqueda)
    if producto_encontrado is None:
        print("Producto no encontrado.")
        return False

    if nuevo_precio is not None:
        producto_encontrado["precio"] = float(nuevo_precio)

    if nueva_cantidad is not None:
        producto_encontrado["cantidad"] = int(nueva_cantidad)

    print(f"Producto '{nombre_busqueda}' actualizado con éxito.")
    return True


def eliminar_producto(lista_productos, nombre_busqueda):
    """
    Elimina un producto si existe en la lista.
    """
    producto_encontrado = buscar_producto(lista_productos, nombre_busqueda)
    if producto_encontrado:
        lista_productos.remove(producto_encontrado)
        print(f"Producto '{nombre_busqueda}' eliminado.")
        return True

    print("Producto no encontrado.")
    return False


def calcular_estadisticas(lista_productos):
    """
    Calcula estadísticas: unidades totales, valor total,
    producto más caro y producto con mayor stock.
    """
    if len(lista_productos) == 0:
        print("No hay estadísticas porque el inventario está vacío.")
        return

    unidades_totales = sum(p["cantidad"] for p in lista_productos)
    valor_total = sum(p["precio"] * p["cantidad"] for p in lista_productos)

    producto_mas_caro = max(lista_productos, key=lambda p: p["precio"])
    producto_mayor_stock = max(lista_productos, key=lambda p: p["cantidad"])

    print("\n--- ESTADÍSTICAS ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con más stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']})")
    print("----------------------\n")
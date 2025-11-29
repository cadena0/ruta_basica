import csv

def exportar_inventario_csv(lista_productos, archivo_destino, guardar_titulos_columnas=True):
    """
    Guarda la lista de productos en un archivo CSV.
    
    Parámetros:
    - lista_productos: lista de diccionarios con productos.
    - archivo_destino: ruta y nombre del archivo donde se guardará el CSV.
    - guardar_titulos_columnas: si True, se escribe la primera fila con los nombres de las columnas.
    """
    if len(lista_productos) == 0:
        print("No se puede guardar un inventario vacío.")
        return

    try:
        with open(archivo_destino, "w", newline="", encoding="utf-8") as archivo:
            escritor_csv = csv.writer(archivo)

            if guardar_titulos_columnas:
                escritor_csv.writerow(["nombre", "precio", "cantidad"])

            for producto in lista_productos:
                escritor_csv.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])

        print(f"Inventario guardado en: {archivo_destino}")

    except Exception as e:
        print(f"Error al guardar CSV: {e}")


def leer_inventario_csv(archivo_origen):
    """
    Lee un archivo CSV y devuelve los productos válidos y el número de filas inválidas.

    Retorna:
    - lista_productos_validos: lista de productos correctamente cargados.
    - filas_invalidas: cantidad de filas que no pudieron cargarse.
    """
    lista_productos_validos = []
    filas_invalidas = 0

    try:
        with open(archivo_origen, "r", encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo)
            encabezado = next(lector_csv)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido en el archivo CSV.")
                return None, 0

            for fila in lector_csv:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio_texto, cantidad_texto = fila

                try:
                    precio = float(precio_texto)
                    cantidad = int(cantidad_texto)

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    lista_productos_validos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    filas_invalidas += 1

        return lista_productos_validos, filas_invalidas

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None, 0

    except Exception as e:
        print(f"Error al leer el CSV: {e}")
        return None, 0
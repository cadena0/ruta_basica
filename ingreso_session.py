import csv

def leer_usuarios():
    usuarios = []

    with open("usuarios.csv", "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  

        for fila in reader:
            if len(fila) >= 2:
                usuarios.append({
                    "username": fila[0],
                    "password": fila[1]
                })

    return usuarios


def validar_login(usuario_ingresado, password_ingresado, usuarios):
    for u in usuarios:
        if u["username"] == usuario_ingresado and u["password"] == password_ingresado:
            return True
    return False
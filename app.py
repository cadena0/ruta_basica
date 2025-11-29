import csv
from ingreso_session import registro, ingresa_usuario

usuarios_creados = [
    {"usuario":"andres" , "contrasena" :"1234"},
    {"usuario":"maria" , "contrasena" :"abcd"},
    {"usuario":"pedro" , "contraseña" :"pass1a"}
]

with open ("usuario_creados.csv",  newline="") as f:
    data = csv.reader(f, delimiter=";")
def inici_sesion():
    while True :
        print ("-------inicio de session-------")
        print ("1. registrate")
        print ("2. inicia session")
        print ("0. salir")
        opcion = int(input("ingresa una opcion valida: "))
        
        if opcion == 1:
            registro()
        elif opcion == 2:
            ingresa_usuario()
        elif opcion == 0:
            print("--------Hasta luego--------")
            return
        else:
            print ("Numero invalido. Elige una opcion correcta.")
 

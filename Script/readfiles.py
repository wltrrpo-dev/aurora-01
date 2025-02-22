import os
import random
from datetime import datetime

print("="*32 + "\n" + "=       MENÚ PRINCIPAL         =" + "\n" + "="*32)
print("=" + " Este menú fue creado para    =")
print("=" + " facilitarte la manera de     =")
print("=" + " como utilizar la aplicación  =")
print("="*32)
print("=" + "   1. Opción 1" + "                =")
print("=" + "   2. Opción 2" + "                =")
print("=" + "   3. Opción 3" + "                =")
print("=" + "   4. Salir" + "                   =")
print("="*32)


def listar_archivos_csv(ruta):
    """
    Función que lista los archivos CSV de una carpeta
    """
    for raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(".csv"):
                print(archivo)

ruta_carpeta = r"C:\Users\jose.duque\OneDrive - arus.com.co\Documentos\readFile"

opcion = input("Seleccione una opción: ")

def crear_carpetas_y_archivos(n, ruta_base="./output"):
    """
    Crea entre 1 y N carpetas, y dentro de cada carpeta, crea entre 1 y N archivos CSV con la hora actual.
    
    :param n: Número máximo de carpetas y archivos a crear.
    :param ruta_base: Ruta base donde se crearán las carpetas y archivos.
    autor: José Duque
    version: 1.0
    return: None
    """
    if not os.path.exists(ruta_base):
        os.makedirs(ruta_base)
    
    for i in range(1, random.randint(1, n) + 1):
        carpeta = os.path.join(ruta_base, f"carpeta_{i}")
        os.makedirs(carpeta, exist_ok=True)
        
        for j in range(1, random.randint(1, n) + 1):
            archivo = os.path.join(carpeta, f"archivo_{j}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
            with open(archivo, "w") as f:
                f.write("columna1,columna2,columna3\n") 
                f.write("valor1,valor2,valor3\n") 
    
    print(f"Se crearon las carpetas y archivos en: {ruta_base}")

if opcion == "1":
    listar_archivos_csv(ruta_carpeta)
elif opcion == "2":
    cantFolders = int(input("Ingrese la cantidad de carpetas que quiere crear: "))
    ruta_base = input("Ingrese la ruta base donde se crearán las carpetas y archivos: ")
    crear_carpetas_y_archivos(cantFolders, ruta_base)
elif opcion == "3":
    cantEvent = int(input("Ingrese la cantidad de eventos que quiere crear: "))
    crear_n_eventos(cantEvent)
elif opcion == "4":
    print("Salir")
else:
    print("Opción no válida") 


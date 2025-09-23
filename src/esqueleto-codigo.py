import os

nom_archivo = input("Ingrese el nombre del archivo de ventas: ")
filepath = f"{nom_archivo}.txt"

try:
    if not os.path.exists(filepath):
        print(f"El archivo: {filepath} fue creado con éxito.")
        file = open(filepath, "w+")
    else:
        print(f"El archivo: {filepath} ya existe.")
        file = open(filepath, "a+")
except IOError as e:
    print(f"Error: No se pudo acceder o generar el archivo. {e}")
    exit()

def normalizar(texto):
    return texto.lower().strip()

def agegar_producto(): #Oscar
        with open(f"{nom_archivo}.txt", "a") as file:
            print(f"{"="*5} Registro de producto {"="*5}")
            codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            print("Cual sera la cantidad?")
            cantidad = try_int()
            print("Cual sera el costo individual del producto?")
            costo = try_float()
            file.write(f"{codigo},{normalizar(nombre)},{cantidad},{costo}\n")
            print("Producto agregado correctamente.")

def try_int():
    try:
        escribe = int(input('Escribe: '))
        return escribe
    except ValueError:
        print('\nEl numero es invaliddo, escribelo de nuevo.\n')
        return try_int()
    
def try_float():
    try:
        escribe = float(input('Escribe: '))
        return escribe
    except ValueError:
        print('\nEl numero es invaliddo, escribelo de nuevo.\n')
        return try_int()
    
def quitar_producto(): #Bryan
    #Necesario tener:
    # - codigo del producto
    # - nombre
    # - cantidad
    # - costo individual
    pass

def ver_inventario(): #Oscar
    with open(f"{nom_archivo}.txt", "r") as file:
        print(f"| {'Codigo':<10} | {'Nombre':<15} | {'Cantidad':<15} | {'Costo individual':<16} | {'Costo total':<15} |")
        for linea in file.readlines():
            lista = linea.split(",")
            total = int(lista[2])*float(lista[3])
            print(f"| {(lista[0]):<10} | {(lista[1].title()):<15} | {(lista[2]):<15} | {(lista[3]):<16} | {total:<15} |")
    
def buscar_producto(): #Bryan
    pass

def calcular_total(): #Oscar
    with open(f"{nom_archivo}.txt", "r") as file:
        contador = 0
        for linea in file.readlines():
            lista = linea.split(",")
            contador += int(lista[2]) * float(lista[3])
        print(f"{'='*50}\nEl total es de ${contador}\n{'='*50}")
            

def generar_reporte_final(): #Bryan
    pass

def menu():
    while True:
        print("\n === Menú ===")
        print("1. Agregar producto a inventario.")
        print("2. Quitar producto de inventario.")
        print("3. Ver los productos registrados.")
        print("4. Buscar producto.")
        print("5. Calcular total de los productos.")
        print("6. Generar reporte final.")
        print("7. Salir.")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agegar_producto()
        elif opcion == "2":
            quitar_producto()
        elif opcion == "3":
            ver_inventario()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            calcular_total()
        elif opcion == "6":
            generar_reporte_final()
        elif opcion == "7":
            file.close()
            print("\nSaliendo del sistema de inventario...")
            break
        else:
            print("Opción no valida. Intende de nuevo.")

if __name__ == "__main__":
    menu()
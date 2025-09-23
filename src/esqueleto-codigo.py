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

def ver_inventario():  # Oscar
    with open(f"{nom_archivo}.txt", "r") as file:
        print("-" * 100)
        print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Código", "Producto", "Cantidad", "Precio", "Total"))
        print("-" * 100)
        for linea in file:
            lista = linea.strip().split(",")
            codigo = lista[0]
            producto = lista[1].title()
            cantidad = int(lista[2])
            precio = float(lista[3])
            total = cantidad * precio
            print("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}".format(codigo, producto, cantidad, precio, total))
    
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

def actualizar_inventario():
    print("=====================\n¿Que desea realizar?")
    print("1. Actualizar cantidad")
    print("2. Actualizar precio")
    opcion = input("Escribe: ")
    encontrado = False
    nuevo_write = ""

    if opcion == "1":
        ver_inventario()
        with open(f"{nom_archivo}.txt", "r") as file:
            act_cantidad = input("Escribe el codigo del producto a modificar: ")
            lista = file.readlines()
        for linea in lista:
            lista_individual = linea.strip().split(",")
            if lista_individual[0] == act_cantidad:
                modificar = lista_individual
                encontrado = True
        if encontrado:
            for string in lista:
                lista_datos = string.split(",")
                if str(lista_datos[0]) != str(act_cantidad):
                    nuevo_write += f"{lista_datos[0]},{lista_datos[1]},{lista_datos[2]},{lista_datos[3]}"
            print("\n¿Cual vaa a ser la nueva cantidad?")
            nueva_cantidad = try_int()
            nuevo_write += f"{modificar[0]},{modificar[1]},{nueva_cantidad},{modificar[3]}\n"
            with open(f"{nom_archivo}.txt", "w") as file:
                file.write(nuevo_write)
                print('Actualizado con exito')
        else:  
            print("\nNo se encontro el codigo\n")

    elif opcion == "2":
        ver_inventario()
        with open(f"{nom_archivo}.txt", "r") as file:
            act_cantidad = input("Escribe el codigo del producto a modificar: ")
            lista = file.readlines()
        for linea in lista:
            lista_individual = linea.strip().split(",")
            if lista_individual[0] == act_cantidad:
                modificar = lista_individual
                encontrado = True
        if encontrado:
            for string in lista:
                lista_datos = string.split(",")
                if str(lista_datos[0]) != str(act_cantidad):
                    nuevo_write += f"{lista_datos[0]},{lista_datos[1]},{lista_datos[2]},{lista_datos[3]}"
            print("\n¿Cual va a ser el precio unitario?")
            nueva_cantidad = try_float()
            nuevo_write += f"{modificar[0]},{modificar[1]},{modificar[2]},{nueva_cantidad}\n"
            with open(f"{nom_archivo}.txt", "w") as file:
                file.write(nuevo_write)
                print('Actualizado con exito')
        else:  
            print("\nNo se encontro el codigo\n")

    else:
        print("\nOpcion invalida, se te regresara al menu\n")


def menu():
    while True:
        print("\n === Menú ===")
        print("1. Agregar producto a inventario.")
        print("2. Quitar producto de inventario.")
        print("3. Ver los productos registrados.")
        print("4. Buscar producto.")
        print("5. Calcular total de los productos.")
        print("6. Generar reporte final.")
        print("7. Actualizar cantidad o precio.")
        print("8. Salir.")

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
            actualizar_inventario()
        elif opcion == "8":
            file.close()
            print("\nSaliendo del sistema de inventario...")
            break
        else:
            print("Opción no valida. Intende de nuevo.")

if __name__ == "__main__":
    menu()
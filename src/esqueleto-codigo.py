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

def agregar_producto(): #Oscar
        print(f"\n{"="*5} Registro de producto {"="*5}")
        codigo = try_codigo()
        nombre = input("\n¿Cual es el nombre del producto?\nEscribe: ")
        cantidad = try_int()
        print("\n¿Cual sera el costo individual del producto?")
        costo = try_float()
        with open(f"{nom_archivo}.txt", "a") as file:
            file.write(f"{codigo},{normalizar(nombre)},{cantidad},{costo}\n")
            print("Producto agregado correctamente.")

def try_codigo(): #funcion utilizada en la funcion agregar_producto()
    # Esta funcion retorna el codigo si no existe, y si el codigo ya existe
    # evitara que se duplique el codigo.
    codigo = input("\n¿Cual es el codigo del producto?\nEscribe: ")
    encontrado = False
    with open(f"{nom_archivo}.txt", "r") as file:
        archivo = file.readlines()
    for linea in archivo:
        lista = linea.strip().split(",")
        if codigo == lista[0]:
            encontrado = True
            print("\nEl codigo ya existe en el inventario.\nEscribe un nuevo codigo")
            return try_codigo()
    if encontrado == False:
        return codigo
    
def try_int(): #funcion utilizada en la funcion agregar_producto()
    # la utilidad de esto es que no se permita agregar al archivo de
    # un dato erroneo, asi aumentando la practicidad del codigo
    try:
        escribe = int(input('\n¿Cual sera la cantidad?\nEscribe: '))
        return escribe
    except ValueError:
        print('\nEl numero es invalido, escribelo de nuevo.\n')
        return try_int()
    
def try_float(): #funcion utilizada en la funcion agregar_producto()
    # la misma utilidad del codigo de try_int() solo que este es para float
    try:
        escribe = float(input('Escribe: $'))
        return escribe
    except ValueError:
        print('\nEl numero es invalido, escribelo de nuevo.\n')
        return try_float()
    
def quitar_producto(): #Bryan
    #Necesario tener:
    # - codigo del producto
    # - nombre
    # - cantidad
    # - costo individual
    pass

def ver_inventario():  # Oscar
    with open(f"{nom_archivo}.txt", "r") as file:
        productos = file.readlines()
    print("-" * 100)
    print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Código", "Producto", "Cantidad", "Precio", "Total"))
    print("-" * 100)
    for linea in productos:
        lista = linea.strip().split(",")
        codigo = lista[0]
        producto = lista[1].title()
        cantidad = int(lista[2])
        precio = float(lista[3])
        total = cantidad * precio
        print("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}".format(codigo, producto, cantidad, precio, total))
    print("-" * 100)

def buscar_producto(): #Bryan
    pass

def calcular_total(): #Oscar
    with open(f"{nom_archivo}.txt", "r") as file:
        archivo = file.readlines()
    contador = 0
    for linea in archivo:
        lista = linea.split(",")
        contador += int(lista[2]) * float(lista[3])
    print(f"{'='*50}\nEl total es de ${contador}\n{'='*50}")

def generar_reporte_final(): #Bryan
    pass

def actualizar_inventario(): #Nota esto lo agregue (Oscar)porque senti que faltaba, espero les guste el funcionamiento
    #Esto es para modiicar la cantidad o el precio de algun articulo
    # Aqui tambien se usan mis funciones de try_int() y try_float()
    print("\n=====================\n¿Que desea realizar?")
    print("1. Actualizar cantidad")
    print("2. Actualizar precio")
    opcion = input("Elige una de las opciones: ")
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
            print("\n¿Cual va a ser la nueva cantidad?")
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
        print("\nOpcion invalida. Intente de nuevo.")
        return actualizar_inventario()

def menu():
    while True:
        print("\n === Menú ===")
        print("1. Agregar producto a inventario.")
        print("2. Quitar producto de inventario.")
        print("3. Ver los productos registrados.")
        print("4. Buscar producto.")
        print("5. Calcular total de los productos.")
        print("6. Actualizar cantidad o precio de producto.")
        print("7. Generar reporte final.")
        print("8. Salir.")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            quitar_producto()
        elif opcion == "3":
            ver_inventario()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            calcular_total()
        elif opcion == "6":
            actualizar_inventario()
        elif opcion == "7":
            generar_reporte_final()
        elif opcion == "8":
            file.close()
            print("\nSaliendo del sistema de inventario...")
            break
        else:
            print("Opción no valida. Intende de nuevo.")

if __name__ == "__main__":
    menu()

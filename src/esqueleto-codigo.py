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
    print("\n" + "="*5 + " Registro de producto " + "="*5)
    codigo = try_codigo()
    nombre = input("\n¿Cual es el nombre del producto?\nEscribe: ")
    print("\n¿Cual sera la cantidad?")
    cantidad = try_int()
    print("\n¿Cual sera el costo individual del producto?")
    costo = try_float()
    with open(f"{nom_archivo}.txt", "a") as file:
        file.write(f"{codigo},{normalizar(nombre)},{cantidad},{costo}\n")
        print("Producto agregado correctamente.")

def try_codigo(): #funcion utilizada en la funcion agregar_producto()
    codigo = input("\n¿Cual es el codigo del producto?\nEscribe: ")
    with open(f"{nom_archivo}.txt", "r") as file:
        for linea in file:
            lista = linea.strip().split(",")
            if codigo == lista[0]:
                print("\nEl codigo ya existe en el inventario\nEscribe un nuevo codigo")
                return try_codigo()
    return codigo
    
def try_int(): 
    try:
        escribe = int(input('Escribe: '))
        return escribe
    except ValueError:
        print('\nEl numero es inválido, escríbelo de nuevo.\n')
        return try_int()
    
def try_float(): 
    try:
        escribe = float(input('Escribe: '))
        return escribe
    except ValueError:
        print('\nEl número es inválido, escríbelo de nuevo.\n')
        return try_float()
    
def quitar_producto():
    ver_inventario()
    encontrado = False
    nuevo_write = ""
    with open(f"{nom_archivo}.txt", "r") as file:
        borrar = input("Escribe el codigo del producto a borrar: ")
        lista = file.readlines()
    for linea in lista:
        lista_individual = linea.strip().split(",")
        if lista_individual[0] == borrar:
            encontrado = True
    if encontrado:
        for string in lista:
            lista_datos = string.strip().split(",")
            if str(lista_datos[0]) != str(borrar):
                nuevo_write += f"{lista_datos[0]},{lista_datos[1]},{lista_datos[2]},{lista_datos[3]}\n"
        with open(f"{nom_archivo}.txt", "w") as file:
            file.write(nuevo_write)
            print('Actualizado con exito')
    else:  
        print("\nNo se encontro el codigo\n")

def ver_inventario():  
    with open(f"{nom_archivo}.txt", "r") as file:
        productos = file.readlines()
    if not productos:
        print("\nEl inventario está vacío.\n")
        return
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
    with open(f"{nom_archivo}.txt", "r") as file:
        lista = file.readlines()
    codigo = input("¿Cual es el codigo a buscar?\nEscribe: ")
    encontrado = False
    for producto in lista:
        valores = producto.strip().split(",")
        if codigo == valores[0]:
            encontrado = True
            print("-" * 100)
            print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Código", "Producto", "Cantidad", "Precio", "Total"))
            print("-" * 100)
            codigo = valores[0]
            producto = valores[1].title()
            cantidad = int(valores[2])
            precio = float(valores[3])
            total = round(cantidad * precio, 2)
            print("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}".format(codigo, producto, cantidad, precio, total))
            print("-" * 100)
    if not encontrado:
        print("\nNo se encontro el codigo\n")

def calcular_total(): 
    with open(f"{nom_archivo}.txt", "r") as file:
        contador = 0
        for linea in file.readlines():
            lista = linea.split(",")
            contador += int(lista[2]) * float(lista[3])
        print(f"{'='*50}\nEl total es de ${contador:.2f}\n{'='*50}")

def generar_reporte_final(): #Bryan
    with open(f"{nom_archivo}.txt", "r") as file:
        productos = file.readlines()

    if not productos:
        print("\nNo hay productos en el inventario para generar reporte.\n")
        return

    reporte = []
    total_general = 0
    reporte.append("="*60 + "\nREPORTE FINAL DEL INVENTARIO\n" + "="*60 + "\n")
    reporte.append("{:<15} {:<20} {:<10} {:<10} {:<10}\n".format("Codigo", "Producto", "Cantidad", "Precio", "Total"))
    reporte.append("-"*60 + "\n")

    for linea in productos:
        lista = linea.strip().split(",")
        codigo = lista[0]
        producto = lista[1].title()
        cantidad = int(lista[2])
        precio = float(lista[3])
        total = cantidad * precio
        total_general += total
        reporte.append("{:<15} {:<20} {:<10} ${:<9.2f} ${:<9.2f}\n".format(codigo, producto, cantidad, precio, total))

    reporte.append("-"*60 + "\n")
    reporte.append(f"TOTAL GENERAL: ${total_general:.2f}\n")
    reporte.append("="*60 + "\n")

    with open("reporte_final.txt", "w") as rep_file:
        rep_file.writelines(reporte)

    print("\nReporte final generado con éxito en 'reporte_final.txt'\n")

def actualizar_inventario(): 
    print("\n=====================\n¿Que desea realizar?")
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
                lista_datos = string.strip().split(",")
                if str(lista_datos[0]) != str(act_cantidad):
                    nuevo_write += f"{lista_datos[0]},{lista_datos[1]},{lista_datos[2]},{lista_datos[3]}\n"
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
            act_precio = input("Escribe el codigo del producto a modificar: ")
            lista = file.readlines()
        for linea in lista:
            lista_individual = linea.strip().split(",")
            if lista_individual[0] == act_precio:
                modificar = lista_individual
                encontrado = True
        if encontrado:
            for string in lista:
                lista_datos = string.strip().split(",")
                if str(lista_datos[0]) != str(act_precio):
                    nuevo_write += f"{lista_datos[0]},{lista_datos[1]},{lista_datos[2]},{lista_datos[3]}\n"
            print("\n¿Cual va a ser el precio unitario?")
            nuevo_precio = try_float()
            nuevo_write += f"{modificar[0]},{modificar[1]},{modificar[2]},{nuevo_precio}\n"
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
        print("7. Actualizar cantidad o precio de producto.")
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
            generar_reporte_final()
        elif opcion == "7":
            actualizar_inventario()
        elif opcion == "8":
            file.close()
            print("\nSaliendo del sistema de inventario...")
            break
        else:
            print("Opción no valida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
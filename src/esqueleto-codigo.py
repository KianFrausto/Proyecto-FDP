# Registro de inventario

num_materiales = int(input("¿Cuantos materiales se van a registrar(Numerico): "))

#Variables acumulables:
costo_materiales = 0
cont_materiales = 0
resumen_materiales = ""

#Contadores de materiales:
mat_naturales = 0
mat_artificiales = 0
mat_compuestos = 0

#Registro de inventario:
while cont_materiales < num_materiales:
    print("")
    print("Registro de material N.", cont_materiales + 1)

    nombre=input("Nombre del material (o 'SALIR' para cancelar): ")
    if nombre == "SALIR":
        print("Registro cancelado")
        break
        
    #Tipo de material
    print("Tipos de materiales:")
    print("Natural (Madera,Algodon,Lana y Minerales)")
    print("Artificial (Plastico,Vidrio,Cemento y Metales)")
    print("Compuesto (Hormigon,Telas y Cuero)")
    tipo_material = input("Seleccione el tipo del material a agregar(o 'SALIR' para cancelar): ")
    if tipo_material == "SALIR":
        print("Registro cancelado")
    if not (tipo_material == "Natural" or tipo_material == "Artificial" or tipo_material == "Compuesto"):
        print("Tipo de material no valido. Intente de nuevo")
        continue

    #Cantidad del material:
    cantidad_valida = False
    while not cantidad_valida:
        cantidad_input = input("Cantidad del material (o 'SALIR' para cancelar ): ")
        if cantidad_input == "SALIR":
            print("Registro cancelado")
            break

        es_numero = True
        for p in cantidad_input:
            if p < '0' or p > '9':
                es_numero = False
                break
        if not es_numero:
            print("Cantidad Invalida. Debe ser numerico.")
            continue

        cantidad = int(cantidad_input)
        if cantidad <= 0:
            print("Cantidad Invalida. Debe ser mayor a 0")
            continue

        cantidad_valida = True

    if cantidad_valida == False:
        break

    #Costo del material:
    costo_valido = False
    while not costo_valido:
        costo_input = input("Costo del material (o 'SALIR' para cancelar ): $")
        if costo_input == "SALIR":
            print("Registro cancelado")
            break

        es_numero = True
        for p in costo_input:
            if p < '0' or p > '9':
                es_numero = False
                break
        if not es_numero:
            print("Cantidad Invalida. Debe ser numerico.")
            continue

        costo = int(costo_input)
        if costo <= 0:
            print("Cantidad Invalida. Debe ser mayor a 0")
            continue

        costo_valido = True

    if costo_valido == False:
        break

    #Acumuladores
    costo_materiales += costo * cantidad
    cont_materiales += 1

    if tipo_material == "Natural":
        mat_naturales += 1
    elif tipo_material == "Artificial":
        mat_artificiales += 1
    elif tipo_material == "Compuesto":
        mat_compuestos += 1

resumen_materiales = resumen_materiales + "Nombre Material: " + nombre + "\t | Tipo Material: " + tipo_material + "\t | Cantidad Material: " + str(cantidad) + "\t | Costo Material por unidad: " + str(costo) + "\t | Costo Material Total: " + str(costo * cantidad) + "\n"

#Reporte de inventario:
print("\n====================================")
print(" REPORTE FINAL - INVENTARIO")
print("====================================")
print("Total de materiales registrados:", cont_materiales)
print("\nResumen del inventario:")
print(resumen_materiales)
print("======================================")
print("Costo total del material $" + str(round(costo_materiales, 2)))
if cont_materiales > 0:
    print("Materiales por tipo - Naturales:", mat_naturales, "Artificiales:", mat_artificiales, "Compuestos:", mat_compuestos)
else:
    print("No se regristraron materiales.")
print("======================================")    
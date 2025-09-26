import os
import time
import datetime as dt

dia = dt.date.today()

NOMBRE_REPORTE_PROHIBIDO = f"Reporte Final-{dia.day}-{dia.month}-{dia.year}.txt"

filepath_carga = ""  
filepath_guardado = "" 

while True:
    try:    
        nom_archivo_input = input("Ingrese el nombre del archivo para el inventario: ").strip()

        if not nom_archivo_input:
            print("El nombre del archivo no puede estar vacio. Intente de nuevo.")
            continue

        print("\nIngrese la fecha del archivo (deje en blanco para usar la fecha actual):)")

        year_input = input("Año (YYYY): ")
        month_input = input("Mes (MM): ")
        day_input = input("Día (DD): ")

        if not (year_input and month_input and day_input):
            fecha_busqueda = dt.date.today()
        else:
            fecha_busqueda = dt.date(int(year_input), int(month_input), int(day_input))
        
        filepath_carga= f"{nom_archivo_input}-{fecha_busqueda.day}-{fecha_busqueda.month}-{fecha_busqueda.year}.txt"

        fecha_guardado = dt.date.today()
        filepath_guardado = f"{nom_archivo_input}-{fecha_guardado.day}-{fecha_guardado.month}-{fecha_guardado.year}.txt"

        if filepath_guardado.lower() == NOMBRE_REPORTE_PROHIBIDO.lower():
            print(f"No puede usar: {nom_archivo_input} como nombre, ya que es el mismo nombre del archivo de reporte final de hoy.")
            continue

        if os.path.exists(filepath_carga):
            print(f"El archivo: {filepath_carga} fue cargado con éxito.")
            if not os.path.exists(filepath_guardado):
                print(f"Los cambios se guardarán en el nuevo archivo: {filepath_guardado}.")
                with open(filepath_guardado, "w+") as file:
                    pass
        else:
            print(f"El archivo: {filepath_carga} no existe. Se creará un nuevo inventario para hoy con el nombre: {filepath_guardado}.")
            with open(filepath_guardado, "w+") as file:
                pass
        
        break
    
    except ValueError:
        print("\n¡Error en el formato de la fecha! Asegúrese de ingresar números válidos para año, mes y día.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def normalizar(texto):
    return texto.lower().strip()

def cargando(timepo = float(),palabra = str()):
    for i in range(3):
        for j in range(4):
            print(f"\r{palabra}" + "." * j + " " * (3 - j), end="",flush=True)
            time.sleep(timepo)
    else:
        print("\n")

def cargar_inventario(path):
    inventario = []
    lineas_invalidas = []  # Guardamos las líneas con errores

    try:
        with open(path, "r") as file:
            for num_linea, linea in enumerate(file, start=1):
                try:
                    datos = [c.strip() for c in linea.split(",")]
                    if len(datos) == 4:
                        inventario.append(datos)
                    elif len(datos) < 4:
                        print(f"Advertencia: En la línea {num_linea} tiene valores menores a 4. Se omitió.")
                        lineas_invalidas.append(num_linea)
                    elif len(datos) > 4:
                        print(f"Advertencia: En la línea {num_linea} tiene valores mayores a 4. Se omitió.")
                        lineas_invalidas.append(num_linea)
                except Exception as e:
                    print(f"Error en la línea {num_linea}: {e}. Línea omitida.")
                    lineas_invalidas.append(num_linea)

        if lineas_invalidas: # Preguntar que hacer en caso de lineas invalidas
            print("\nSe encontraron líneas con errores en el archivo:")
            print("Línea inválida:", ", ".join(map(str, lineas_invalidas)))

            opcion = input("¿Desea eliminarlas del archivo? (s/n): ").strip().lower()
            if opcion == "s":
                try:
                    with open(path, "r") as file:
                        lineas = file.readlines()

                    # Filtrar las líneas válidas
                    lineas_corregidas = [
                        linea for i, linea in enumerate(lineas, start=1)
                        if i not in lineas_invalidas
                    ]

                    with open(path, "w") as file: # Reescribir el archivo sin las inválidas
                        file.writelines(lineas_corregidas)

                    print(f"Se eliminaron {len(lineas_invalidas)} línea(s) inválida(s) del archivo '{path}'.")
                except IOError as e:
                    print(f"Error al intentar reescribir el archivo: {e}")
            else:
                print("Se mantuvieron las líneas inválidas en el archivo.")

    except FileNotFoundError:
        return []
    except IOError as e:
        print(f"Advertencia: Error al leer el archivo. {e}")
        return []

    return inventario

def guardar_inventario(path, inventario):
    try:
        with open(path, "w") as file:
            for datos in inventario:
                file.write(f"{datos[0]},{datos[1]},{datos[2]},{datos[3]}\n")
        return True
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")
        return False

def try_codigo():
    while True:
        codigo = input("\n¿Cual es el codigo del producto?\nCodigo a ingresar: ")
        
        if not codigo:
            print("\nEl código no puede estar vacío. Inténtalo de nuevo.")
            continue

        inventario_actual = cargar_inventario(filepath_carga)
            
        encontrado = False
        for datos in inventario_actual:
            if codigo == datos[0]:
                encontrado = True
                break
                
        if encontrado:
            print("\nEl codigo ya existe en el inventario\nEscribe un nuevo codigo")
        else:
            return codigo

def try_nombre():
    while True:
        nombre = input("\n¿Cual es el nombre del producto?\nNombre a ingresar: ")
        
        if not nombre:
            print("\nEl nombre no puede estar vacío. Inténtalo de nuevo.")
            continue
        
        inventario_actual = cargar_inventario(filepath_carga)
            
        encontrado = False
        for datos in inventario_actual:
            if normalizar(nombre) == normalizar(datos[1]):
                encontrado = True
                break

        if encontrado:
            print("\nEste producto ya existe en el inventario.\nIntente otro nombre.")
        else:    
            return nombre
    
def try_int():
    while True:     
        try:
            escribe = int(input('\n¿Cual sera la cantidad?\nCantidad: '))
            if escribe < 0:
                print("La cantidad no puede ser negrativa. Intente de nuevo.")
                continue
            return escribe
        except ValueError:
            print('\nEl numero es invalido, escribelo de nuevo.\n')
    
def try_float(): 
    while True:
        try:
            escribe = float(input('\n¿Cual sera el costo individual del producto?\nCosto: $'))
            if escribe < 0:
                print("El costo no puede ser negativo. Intente de nuevo.")
                continue
            return escribe
        except ValueError:
            print('\nEl numero es invalido, escribelo de nuevo.\n')

def agregar_producto():
    cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
    print("\n"+ "="*5 + " Registro de producto " + "="*5)

    codigo = try_codigo()
    nombre = try_nombre()
    cantidad = try_int()
    costo = try_float()

    inventario = cargar_inventario(filepath_carga)

    nuevo_producto = [codigo, normalizar(nombre), str(cantidad),str(costo)]
    inventario.append(nuevo_producto)

    if guardar_inventario(filepath_guardado, inventario):
        cargando(0.15, "Actualizando inventario")
        print("Producto agregado correctamente.")
    else:
        cargando(0.15, "Actualizando inventario")
        print("Error a guardar el inventario despues de agregar.")

def quitar_producto():
    ver_inventario()

    inventario = cargar_inventario(filepath_carga)

    if not inventario:
        cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
        print("El inventario esta vacio, no hay productos para eliminar.\n")
        return
    
    cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
    codigo_a_borrar = input("Escribe el codigo del producto a borrar: ").strip()

    producto_eliminado = None

    inventario_actualizado = []
    for datos in inventario:
        if datos[0] == codigo_a_borrar:
            producto_eliminado = datos 
        else:
            inventario_actualizado.append(datos)

    if producto_eliminado:
        if guardar_inventario(filepath_guardado, inventario_actualizado):
            nombre = producto_eliminado[1].title()
            cargando(0.15, "Actualizando inventario")
            print(f"\nEl producto '{nombre}' con codigo '{codigo_a_borrar}' ha sido eliminado con exito.")
        else:
            cargando(0.15, "Actualizando inventario")
            print("Error al guardar el inventario despues de eliminar.")
    else:
        cargando(0.15, "Cargando")
        print("\nNo se encontro el codigo en el inventario.\n")

def ver_inventario():
    productos = cargar_inventario(filepath_carga)

    if not productos:
        cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
        print("\nEl inventario esta vacio.\n")
        return
    
    cargando(0.25, "Cargando inventario")
    print("=" * 100)
    print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Codigo", "Producto", "Cantidad", "Precio", "Total"))
    print("=" * 100)

    for datos in productos:
        try:
            codigo = datos[0]
            producto = datos[1].title()
            cantidad = int(datos[2])
            precio = float(datos[3])
            total = round(cantidad * precio, 2)

            print("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}".format(codigo, producto, cantidad, precio, total))
            print("=" * 100)
        except (ValueError, IndexError):
            continue

def buscar_producto():
    productos = cargar_inventario(filepath_carga)

    if not productos:
        cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
        print("\nEl inventario esta vacio.\n")
        return
    
    cargando(0.25, "Buscando codigos")
    print("="* 30)
    print("{:^30}".format("Codigos Disponibles"))
    print("="* 30)
    for datos in productos:
        codigo = datos[0]
        print(f"{codigo:^30}")
    print("="* 30)

    codigo_a_buscar = input("¿Cual es el codigo a buscar?\nCodigo: ").strip()

    encontrado = False
    for datos in productos:
        if codigo_a_buscar == datos[0]:
            encontrado = True

            cargando(0.15, "Buscando codigo")
            print("=" * 100)
            print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Codigo", "Producto", "Cantidad", "Precio", "Total"))
            print("=" * 100)

            producto = datos[1].title()
            cantidad = int(datos[2])
            precio = float(datos[3])
            total = round(cantidad * precio, 2)

            print("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}".format(codigo_a_buscar, producto, cantidad, precio, total))
            print("=" * 100)
            break

    if not encontrado:
        cargando(0.15, "Cargando")
        print(f"\nNo se encontro el codigo: {codigo_a_buscar} en el inventario.\n")

def calcular_total():
    productos = cargar_inventario(filepath_carga)

    if not productos:
        cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
        print("\nEl inventario esta vacio.\n")
        return
    
    total_general = 0
    for datos in productos:
        try:
            cantidad = int(datos[2])
            precio = float(datos[3])
            total_general += cantidad * precio
        except (ValueError, IndexError):
            continue
    
    cargando(0.25, "Calculando valores")
    print(f"{"="*100}\nEl valor total de los productos en el inventario es: ${total_general:.2f}\n{"="*100}\n")

def actualizar_inventario():
    ver_inventario()
    cargando(0.15, "Validando opciones")
    print("\n=====================\n¿Que desea actualizar?")
    print("1. Actualizar cantidad.")
    print("2. Actualizar precio.")
    opcion = input("Seleccione una opcion (1 o 2): ").strip()

    if opcion not in ("1", "2"):
        print("\nOpcion no valida. Regresando al menu principal.\n")
        return
    
    inventario = cargar_inventario(filepath_carga)
    
    if not inventario:
        cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
        print("El inventario esta vacio, no hay productos para actualizar.\n")
        return
    
    codigo_a_modificar = input("Escribe el codigo del producto a modificar: ").strip()
    
    producto_modificado = None
    indice = -1

    for i, datos in enumerate(inventario):
        if datos[0] == codigo_a_modificar:
            producto_modificado = datos
            indice = i
            break

    if producto_modificado:
        nombre_producto = producto_modificado[1].title()

        nueva_linea_datos = list(producto_modificado)

        if opcion == "1":
            print(f"\nActualizando cantidad del producto: {nombre_producto} (Actual: {producto_modificado[2]})")
            nueva_cantidad = try_int()
            nueva_linea_datos[2] = str(nueva_cantidad)
            campo_actualizado = "cantidad"
            valor_actualizado = nueva_cantidad
        
        elif opcion == "2":
            print(f"\nActualizando precio del producto: {nombre_producto} (Actual: ${producto_modificado[3]})")
            nuevo_precio = try_float()
            nueva_linea_datos[3] = str(nuevo_precio)
            campo_actualizado = "precio"
            valor_actualizado = nuevo_precio

        inventario[indice] = nueva_linea_datos

        if guardar_inventario(filepath_carga, inventario):
            cargando(0.15, "Actualizando inventario")
            print(f"\n Producto '{nombre_producto}' actualizado exitosamente.")
            print(f" El nuevo {campo_actualizado} es: {valor_actualizado}\n")
        else:
            cargando(0.15, "Actualizando inventario")
            print("Error al guardar el inventario. El inventario NO fue actualizado.\n")
    else:
        cargando(0.15, f"Accediendo al archivo: {filepath_carga}")
        print(f"\nNo se encontro el codigo: {codigo_a_modificar} en el inventario.\n")

def generar_reporte_final():
    print("\n === Generando Reporte Final === ")

    productos_data = cargar_inventario(filepath_guardado)

    if not productos_data:
        cargando(0.15, f"Accediendo al archivo: {filepath_guardado}")
        print("El inventario esta vacio. No hay datos para generar el reporte.\n")
        return
    
    productos_procesados = []
    total_general = 0

    for datos in productos_data:
        try:
            codigo = datos[0]
            nombre = datos[1]
            cantidad = int(datos[2])
            costo = float(datos[3])
            sub_total = cantidad * costo

            productos_procesados.append({
                "codigo": codigo,
                "nombre": nombre.title(),
                "cantidad": cantidad,
                "costo": costo,
                "sub_total": sub_total
            })
            total_general += sub_total
        except (ValueError, IndexError):
            continue

    try:
        report_path = NOMBRE_REPORTE_PROHIBIDO
        with open(report_path, "w") as report_file:
            report_file.write("=== INVENTARIO Y REPORTE FINAL ===\n")
            report_file.write(f"Numero total de productos unicos: {len(productos_procesados)}\n")
            report_file.write(f"Valor total del inventario: ${total_general:.2f}\n")
            report_file.write("\n=== DETALLES POR PRODUCTO ===\n")
            report_file.write("=" * 100 + "\n")
            report_file.write("{:^25} {:^25} {:^20} {:^10} {:^12}\n".format("Codigo", "Nombre", "Cantidad", "Costo", "Total"))
            report_file.write("=" * 100 + "\n")

            for producto in productos_procesados:
                report_file.write("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}\n".format(
                    producto["codigo"],
                    producto["nombre"],
                    producto["cantidad"],
                    producto["costo"],
                    producto["sub_total"]
                ))
                report_file.write("=" * 100 + "\n")
        cargando(0.15, "Cargando")
        print(f"Reporte generado exitosamente en el archivo: {report_path}\n")
    except IOError as e:
        print(f"Error al generar el reporte: {e}\n")

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

        opcion = input("Seleccione una opcion: ").strip()
        
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
            cargando(0.25, "Saliendo del sistema de inventario")
            break
        else:
            print("Opción no valida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

#460
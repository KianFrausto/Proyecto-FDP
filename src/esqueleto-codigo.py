import os
import time
import datetime as dt
from sys import exit 

DIA_HOY = dt.date.today()
NOMBRE_REPORTE_PROHIBIDO = f"Reporte_Final-{DIA_HOY.day}-{DIA_HOY.month}-{DIA_HOY.year}.txt"
CANCEL_TOKEN = "cancelar"

filepath_carga = "" 
WORKING_FILEPATH = "" 

def normalizar(texto):
    """Convierte el texto a minúsculas y elimina espacios en blanco iniciales/finales."""
    return str(texto).lower().strip()

def cargando(tiempo=0.15, palabra="Cargando"):
    """Simula una animación de carga."""
    for i in range(3):
        for j in range(4):
            print(f"\r{palabra}" + "." * j + " " * (3 - j), end="", flush=True)
            time.sleep(tiempo)
    else:
        print("\n")

def try_int(mensaje=''):
    while True:    
        entrada = input(mensaje).strip()
        
        if normalizar(entrada) == CANCEL_TOKEN:
            print("\nOperación cancelada.")
            return None 

        try:
            escribe = int(entrada)
            if escribe < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo o escriba 'cancelar'.")
                continue
            return escribe
        except ValueError:
            print('\nEl número es inválido, escríbalo de nuevo o escriba "cancelar".\n')

def try_float(mensaje=''): 
    while True:
        entrada = input(mensaje).strip()

        if normalizar(entrada) == CANCEL_TOKEN:
            print("\nOperación cancelada.")
            return None 

        try:
            escribe = float(entrada)
            if escribe < 0:
                print("El costo no puede ser negativo. Intente de nuevo o escriba 'cancelar'.")
                continue
            return escribe
        except ValueError:
            print('\nEl número es inválido, escríbalo de nuevo o escriba "cancelar".\n')

def cargar_inventario(path):
    inventario = []
    
    try:
        with open(path, "r") as file:
            for linea in file:
                datos = [c.strip() for c in linea.split(",")]
                if len(datos) == 4 and all(datos):
                    inventario.append(datos)
    except FileNotFoundError:
        return []
    except IOError as e:
        print(f"Advertencia: Error al leer el archivo '{path}'. {e}")
        return []
        
    return inventario

def guardar_inventario(path, inventario):
    try:
        with open(path, "w") as file:
            for datos in inventario:
                file.write(",".join(datos) + "\n")
        return True
    except IOError as e:
        print(f"Error al escribir en el archivo: {path}. {e}")
        return False

def try_codigo(inventario):
    while True:
        codigo = input("\n¿Cual es el codigo del producto? (Escriba 'cancelar' para salir)\nCodigo a ingresar: ").strip()
        
        if normalizar(codigo) == CANCEL_TOKEN:
            print("\nOperación cancelada.")
            return None

        if not codigo:
            print("\nEl código no puede estar vacío. Inténtalo de nuevo.")
            continue

        encontrado = any(codigo == datos[0] for datos in inventario)
                
        if encontrado:
            print("\nEl código ya existe en el inventario\nEscribe un nuevo código o 'cancelar'.")
        else:
            return codigo

def try_nombre(inventario):
    while True:
        nombre = input("\n¿Cual es el nombre del producto? (Escriba 'cancelar' para salir)\nNombre a ingresar: ").strip()
        
        if normalizar(nombre) == CANCEL_TOKEN:
            print("\nOperación cancelada.")
            return None

        if not nombre:
            print("\nEl nombre no puede estar vacío. Inténtalo de nuevo.")
            continue
        
        nombre_normalizado = normalizar(nombre)
        
        encontrado = any(nombre_normalizado == normalizar(datos[1]) for datos in inventario)

        if encontrado:
            print("\nEste producto ya existe en el inventario.\nIntente otro nombre o escriba 'cancelar'.")
        else:    
            return nombre

def inicializar_rutas():
    global filepath_carga
    global WORKING_FILEPATH

    print(f"\n[Escriba '{CANCEL_TOKEN}' en cualquier momento para cancelar y salir.]")

    while True:
        try:    
            nom_archivo_input = input("Ingrese el nombre base del archivo para el inventario (ej: 'Inventario'): ").strip()
            
            if normalizar(nom_archivo_input) == CANCEL_TOKEN:
                return None
            
            if not nom_archivo_input:
                print("El nombre base del archivo no puede estar vacío. Intente de nuevo.")
                continue

            print("\nIngrese la fecha del archivo a cargar (deje en blanco para usar la fecha actual):")

            year_input = input("Año (YYYY) o 'cancelar': ").strip()
            if normalizar(year_input) == CANCEL_TOKEN: return None

            month_input = input("Mes (MM) o 'cancelar': ").strip()
            if normalizar(month_input) == CANCEL_TOKEN: return None

            day_input = input("Día (DD) o 'cancelar': ").strip()
            if normalizar(day_input) == CANCEL_TOKEN: return None

            if not (year_input and month_input and day_input):
                fecha_busqueda = DIA_HOY
            else:
                fecha_busqueda = dt.date(int(year_input), int(month_input), int(day_input))
            
            filepath_carga = f"{nom_archivo_input}-{fecha_busqueda.day}-{fecha_busqueda.month}-{fecha_busqueda.year}.txt"
            WORKING_FILEPATH = f"{nom_archivo_input}-{DIA_HOY.day}-{DIA_HOY.month}-{DIA_HOY.year}.txt"

            if WORKING_FILEPATH.lower() == NOMBRE_REPORTE_PROHIBIDO.lower():
                print(f"No puede usar: {nom_archivo_input} como nombre, ya que resultaría en el mismo nombre del archivo de reporte final de hoy ('{NOMBRE_REPORTE_PROHIBIDO}').")
                continue

            inventario_en_memoria = []

            if os.path.exists(filepath_carga):
                print(f"\nEl archivo a cargar: {filepath_carga} fue encontrado.")
                inventario_en_memoria = cargar_inventario(filepath_carga)
                print(f"Productos válidos cargados: {len(inventario_en_memoria)}")
            else:
                print(f"\nEl archivo a cargar: {filepath_carga} no existe. Se iniciará un nuevo inventario.")

            if filepath_carga != WORKING_FILEPATH:
                print(f"Todos los cambios de la sesión se guardarán en el archivo de trabajo de hoy: {WORKING_FILEPATH}.")
            
            if guardar_inventario(WORKING_FILEPATH, inventario_en_memoria):
                 print(f"Inventario inicializado y guardado en {WORKING_FILEPATH}.")
            else:
                print("Error crítico al inicializar el archivo de guardado. Saliendo.")
                return None 
            
            return inventario_en_memoria 
        
        except ValueError:
            print("\n¡Error en el formato de la fecha! Asegúrese de ingresar números válidos para año, mes y día, o escriba 'cancelar'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado durante la inicialización: {e}")
            return None

def agregar_producto():    
    cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
    inventario = cargar_inventario(WORKING_FILEPATH)
    
    print("\n"+ "="*5 + " Registro de Producto " + "="*5)

    codigo = try_codigo(inventario)
    if codigo is None: return

    nombre = try_nombre(inventario)
    if nombre is None: return

    cantidad = try_int("¿Cual será la cantidad? (o 'cancelar'): ")
    if cantidad is None: return

    costo = try_float("¿Cual será el costo individual del producto? (o 'cancelar')\nCosto: $")
    if costo is None: return

    nuevo_producto = [codigo, normalizar(nombre), str(cantidad), str(costo)]
    inventario.append(nuevo_producto)

    if guardar_inventario(WORKING_FILEPATH, inventario):
        cargando(0.15, "Actualizando inventario")
        print("Producto agregado correctamente.")
    else:
        cargando(0.15, "Actualizando inventario")
        print("Error al guardar el inventario después de agregar.")

def quitar_producto():    
    inventario = cargar_inventario(WORKING_FILEPATH)

    if not inventario:
        cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
        print("El inventario está vacío, no hay productos para eliminar.\n")
        return
    
    ver_inventario(inventario)
    
    cargando(0.15, f"Preparando eliminación...")
    codigo_a_borrar = input("Escribe el código del producto a borrar (o 'cancelar'): ").strip()
    
    if normalizar(codigo_a_borrar) == CANCEL_TOKEN:
        print("\nOperación cancelada.")
        return

    inventario_actualizado = [datos for datos in inventario if datos[0] != codigo_a_borrar]
    
    if len(inventario_actualizado) < len(inventario):
        producto_eliminado = next((datos for datos in inventario if datos[0] == codigo_a_borrar), None)

        if guardar_inventario(WORKING_FILEPATH, inventario_actualizado):
            nombre = producto_eliminado[1].title()
            cargando(0.15, "Actualizando inventario")
            print(f"\nEl producto '{nombre}' con código '{codigo_a_borrar}' ha sido eliminado con éxito.")
        else:
            cargando(0.15, "Actualizando inventario")
            print("Error al guardar el inventario después de eliminar.")
    else:
        cargando(0.15, "Cargando")
        print(f"\nNo se encontró el código '{codigo_a_borrar}' en el inventario.\n")

def actualizar_inventario():
    inventario = cargar_inventario(WORKING_FILEPATH)
    
    if not inventario:
        cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
        print("El inventario está vacío, no hay productos para actualizar.\n")
        return
        
    ver_inventario(inventario)
    
    cargando(0.15, "Validando opciones")
    print("\n=====================\n¿Qué desea actualizar? (o 'cancelar')")
    print("1. Actualizar cantidad.")
    print("2. Actualizar precio.")
    opcion = input("Seleccione una opción (1, 2, o 'cancelar'): ").strip()

    if normalizar(opcion) == CANCEL_TOKEN:
        print("\nOperación cancelada.")
        return

    if opcion not in ("1", "2"):
        print("\nOpción no válida. Regresando al menú principal.\n")
        return
    
    codigo_a_modificar = input("Escribe el código del producto a modificar (o 'cancelar'): ").strip()
    
    if normalizar(codigo_a_modificar) == CANCEL_TOKEN:
        print("\nOperación cancelada.")
        return

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
        campo_actualizado = ""
        valor_actualizado = None

        if opcion == "1":
            print(f"\nActualizando cantidad de: {nombre_producto} (Actual: {producto_modificado[2]})")
            nueva_cantidad = try_int("Nueva Cantidad (o 'cancelar'): ")
            if nueva_cantidad is None: return 
            nueva_linea_datos[2] = str(nueva_cantidad)
            campo_actualizado = "cantidad"
            valor_actualizado = nueva_cantidad
        
        elif opcion == "2":
            print(f"\nActualizando precio de: {nombre_producto} (Actual: ${producto_modificado[3]})")
            nuevo_precio = try_float("Nuevo Costo (o 'cancelar'): $")
            if nuevo_precio is None: return 
            nueva_linea_datos[3] = str(nuevo_precio)
            campo_actualizado = "precio"
            valor_actualizado = nuevo_precio

        inventario[indice] = nueva_linea_datos

        if guardar_inventario(WORKING_FILEPATH, inventario):
            cargando(0.15, "Actualizando inventario")
            print(f"\nProducto '{nombre_producto}' actualizado exitosamente.")
            print(f"El nuevo {campo_actualizado} es: {valor_actualizado}\n")
        else:
            cargando(0.15, "Actualizando inventario")
            print("Error al guardar el inventario. El inventario NO fue actualizado.\n")
    else:
        cargando(0.15, "Buscando")
        print(f"\nNo se encontró el código: {codigo_a_modificar} en el inventario.\n")

def ver_inventario(productos=None):    
    if productos is None:
        productos = cargar_inventario(WORKING_FILEPATH)

    if not productos:
        cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
        print("\nEl inventario está vacío.\n")
        return
    
    cargando(0.25, "Cargando inventario")
    print("=" * 100)
    print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Código", "Producto", "Cantidad", "Precio", "Total"))
    print("=" * 100)

    for datos in productos:
        try:
            codigo = datos[0]
            producto = datos[1].title()
            cantidad = int(datos[2])
            precio = float(datos[3])
            total = round(cantidad * precio, 2)

            print("{:^25} {:^25} {:^20} ${:^9.2f} ${:^11.2f}".format(codigo, producto, cantidad, precio, total))
            print("-" * 100)
        except (ValueError):
            continue

def buscar_producto():    
    productos = cargar_inventario(WORKING_FILEPATH)

    if not productos:
        cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
        print("\nEl inventario está vacío.\n")
        return
    
    cargando(0.25, "Buscando códigos")
    
    print("\n" + "="* 30)
    print("{:^30}".format("Códigos Disponibles"))
    print("="* 30)
    codigos = [datos[0] for datos in productos]
    print(', '.join(codigos))
    print("="* 30)

    codigo_a_buscar = input("¿Cual es el código a buscar? (o 'cancelar')\nCódigo: ").strip()

    if normalizar(codigo_a_buscar) == CANCEL_TOKEN:
        print("\nOperación cancelada.")
        return

    encontrado = False
    for datos in productos:
        if codigo_a_buscar == datos[0]:
            encontrado = True

            cargando(0.15, "Buscando código")
            print("=" * 100)
            print("{:^25} {:^25} {:^20} {:^10} {:^12}".format("Código", "Producto", "Cantidad", "Precio", "Total"))
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
        print(f"\nNo se encontró el código: {codigo_a_buscar} en el inventario.\n")

def calcular_total():    
    productos = cargar_inventario(WORKING_FILEPATH)

    if not productos:
        cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
        print("\nEl inventario está vacío.\n")
        return
    
    total_general = 0
    for datos in productos:
        try:
            cantidad = int(datos[2])
            precio = float(datos[3])
            total_general += cantidad * precio
        except ValueError:
            continue 
    
    cargando(0.25, "Calculando valores")
    print(f"{'='*100}\nEl valor total de los productos en el inventario es: ${total_general:.2f}\n{'='*100}\n")

def generar_reporte_final():    
    print("\n === Generando Reporte Final === ")

    productos_data = cargar_inventario(WORKING_FILEPATH)

    if not productos_data:
        cargando(0.15, f"Accediendo al archivo: {WORKING_FILEPATH}")
        print("El inventario está vacío. No hay datos para generar el reporte.\n")
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
            report_file.write(f"=== REPORTE FINAL DE INVENTARIO - FECHA: {DIA_HOY.strftime('%d-%m-%Y')} ===\n\n")
            report_file.write(f"Archivo de origen de datos: {WORKING_FILEPATH}\n")
            report_file.write(f"Número total de productos únicos: {len(productos_procesados)}\n")
            report_file.write(f"VALOR TOTAL DEL INVENTARIO: ${total_general:.2f}\n")
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
                report_file.write("-" * 100 + "\n")
                
        cargando(0.15, "Generando reporte")
        print(f"Reporte generado exitosamente en el archivo: {report_path}\n")
    except IOError as e:
        print(f"Error al generar el reporte: {e}\n")

def manejar_datos_invalidos():    
    lineas_completas = []
    try:
        with open(WORKING_FILEPATH, "r") as file:
            lineas_completas = file.readlines()
    except Exception as e:
        print(f"Error al leer el archivo para manejar datos inválidos: {e}")
        return

    if not lineas_completas:
        print("El inventario está vacío, no hay datos que manejar.")
        return

    productos_validos = []
    productos_invalidos_y_indices = []
    
    for i, linea in enumerate(lineas_completas):
        datos = [c.strip() for c in linea.strip().split(",")]
        
        if len(datos) == 4 and all(datos):
            productos_validos.append(datos)
        else:
            productos_invalidos_y_indices.append({
                "indice_original": i, 
                "linea_cruda": linea.strip(),
                "datos": datos
            })

    if not productos_invalidos_y_indices:
        print("No se detectaron líneas con formato inválido.")
        return

    print("\n" + "="*50)
    print("¡ADVERTENCIA! Se detectaron líneas con formato inválido:")
    print("El formato esperado es: Codigo,Nombre,Cantidad,Costo")
    print("="*50)

    for i, item in enumerate(productos_invalidos_y_indices):
        print(f"\n[{i+1}] Línea Inválida (Línea {item['indice_original'] + 1} en archivo):")
        print(f"  Contenido: {item['linea_cruda']}")
        print(f"  Datos parciales: {' | '.join(item['datos'])}")


    while True:
        print("\nSeleccione una acción (o 'cancelar'):")
        print("1. Intentar corregir el formato de una línea.")
        print("2. Eliminar TODAS las líneas inválidas.")
        print("3. Volver al menú (Mantener las líneas inválidas).")
        
        opcion = input("Opción: ").strip()

        if normalizar(opcion) == CANCEL_TOKEN:
            print("\nOperación cancelada.")
            return

        if opcion == '1':
            try:
                indice = try_int("Ingrese el número de la línea a corregir (ej. 1) o 'cancelar': ") - 1
                if indice is None: continue
                
                if 0 <= indice < len(productos_invalidos_y_indices):
                    item_a_corregir = productos_invalidos_y_indices[indice]
                    
                    print(f"\nCorrigiendo línea: {item_a_corregir['linea_cruda']}")
                    
                    nuevo_codigo = input("Nuevo Código (o 'cancelar'): ").strip()
                    if normalizar(nuevo_codigo) == CANCEL_TOKEN: continue
                    
                    nuevo_nombre = input("Nuevo Nombre (o 'cancelar'): ").strip()
                    if normalizar(nuevo_nombre) == CANCEL_TOKEN: continue
                    
                    nueva_cantidad = str(try_int("Nueva Cantidad (o 'cancelar'): "))
                    if nueva_cantidad == "None": continue 
                    
                    nuevo_costo = str(try_float("Nuevo Costo (o 'cancelar'): $"))
                    if nuevo_costo == "None": continue
                    
                    linea_corregida = [nuevo_codigo, normalizar(nuevo_nombre), nueva_cantidad, nuevo_costo]
                    
                    if not all(linea_corregida):
                         print("\nError: Una corrección resultó en campos vacíos. Intente de nuevo o elimine la línea.")
                         continue
                         
                    productos_validos.append(linea_corregida)
                    productos_invalidos_y_indices.pop(indice) 
                    
                    inventario_final = productos_validos + [
                        item['datos'] for item in productos_invalidos_y_indices
                    ]
                    
                    if guardar_inventario(WORKING_FILEPATH, inventario_final):
                        print("\nLínea corregida y guardada exitosamente.")
                        if not productos_invalidos_y_indices:
                            print("¡Todos los errores han sido corregidos!")
                            return True
                    else:
                        print("Error al guardar la corrección.")
                else:
                    print("Número de línea no válido.")
            except Exception as e:
                print(f"Error al corregir línea: {e}")
                
        elif opcion == '2':
            if guardar_inventario(WORKING_FILEPATH, productos_validos):
                print(f"¡{len(productos_invalidos_y_indices)} líneas inválidas eliminadas del archivo!")
                return True
            else:
                print("Error al guardar la eliminación de líneas.")
                
        elif opcion == '3':
            print("Se regresa al menú. Las líneas inválidas permanecen en el archivo.")
            return False
        
        else:
            print("Opción no válida.")

def menu():
    if inicializar_rutas() is None:
        cargando(0.25, "Saliendo del sistema de inventario")
        return
    
    while True:
        print("\n === Menú ===")
        print(f"Archivo de trabajo: {WORKING_FILEPATH}")
        print("1. Agregar producto a inventario.")
        print("2. Quitar producto de inventario.")
        print("3. Ver los productos registrados.")
        print("4. Buscar producto por código.")
        print("5. Calcular valor total del inventario.")
        print("6. Actualizar cantidad o precio de producto.")
        print("7. Generar reporte final.")
        print("8. **Manejar datos inválidos** (Corregir o Eliminar).")
        print("9. Salir.")

        opcion = input("Seleccione una opción: ").strip()
        
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
            manejar_datos_invalidos()
        elif opcion == "9":
            cargando(0.25, "Saliendo del sistema de inventario")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
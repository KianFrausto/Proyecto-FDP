# Proyecto-FDP

![Imagen2_ALT](https://github.com/KianFrausto/Proyecto-FDP/blob/2299525c5aa287c3a86f42e48757d7e374126775/docs/5968396.png)

# Integrantes
- Ian Enrique Frausto Cervantes (Senior)
- Leonardo Perez Molina (Junior)
- Nallely Maldonado Ramírez (Junior)
- Bryan Alexis Molina Loya (Mid)
- Oscar Gabriel Reyes Delgado (Mid)

# Contexto y Problema
## Escenario:
El escenario planteado para nuestro proyecto es dentro
de una empresa para la realización de un programa con el
fin de que facilitemos las actividades relacionadas con la
toma de un inventario, como facilitar los datos
ingresados dentro de una lista para el conocimiento de
los materiales disponibles, su cantidad actual, el costo de
cada uno y el presupuesto total de todos y cada uno de
ellos, con el fin de hacer todo de una manera fácil de
entender, concisa y práctica.
## Problemas a resolver:
Nuestras problemáticas a resolver son las siguientes:
- Captura de datos de manera fácil y optima para
registrarlos dentro de una lista para un conocimiento
de los mismos.
- Un costo total dentro de todos los materiales
listados para una cotización y control de los
mismos.
- Mostrar los datos capturados de forma clara para el
mantenimiento de los mismos en el caso de ingresar
más material a los ya existentes o una reducción de
ellos.

## Criterios de exito
- El programa debe permitir la captura de datos de manera sencilla y sin errores.
- La lista de inventario debe mostrarse de forma clara y organizada.
- El cálculo del costo total de los materiales debe ser preciso.
- El sistema debe ser fácil de usar para cualquier usuario sin necesidad de conocimientos avanzados de programación.
- El programa debe permitir actualizar, añadir o reducir materiales en el inventario sin afectar los registros previos.
# Reglas del negocio
## Reglas de identificación de productos (Unicidad)
- Código Único: El codigo de un producto no debe existir previamente en el inventario al integrar registrar uno nuevo. (try_codigo)
- Nombre Único (ignorando mayusculas): El nombre de un producto (sin importar mayúsculas/minúsculas o espacios iniciales/finales) no debe existir previamente en el inventario al registrar uno nuevo. (try_nombre(), normalizar())
## Reglas de Validacion de Datos de Entrada
- Cantidad No Negativa: La cantidad de cualquier producto no peude ser un número negativo (debe ser ≥0). (try_int())
- Costo No Negativo: El costo individual de un producto no peude ser un número negativo (debe ser ≥0). (try_float())
- Campos Requeridos (Código y Nombre): El código y el nombre de un producto no pueden estar vacios al ingresarse. (try_codigo(), try_nombre())
- Formato de inventario: Cada registro de un producto debe contener exactamente 4 campos (código, nombre, cantidad, costo). (cargar_inventario())
## Reglas de Nomeclatura y Restricciones de Archivos
- Formato de Archivo de Inventario: El nombre de un archivo de inventario de seguir el formato. "[nombre_input]-[día]-[mes]-[año].txt". (Lógica principal del while True)
- Restricción de Nombre de Archivo de Reporte: No se permite usar el nombre "Reporte Final" de hoy (Reporte Final-d-m-a.txt) como nombre base para un archivo de inventario. (Lógica principal del while True (uso de NOMBRE_REPORTE_PROHIBIDO))
- Normalización del Nombre de Archivo Prohibido: La restricción del nombre del archivo de reporte final aplica sin importar si el usuario usa mayúsculas o minúsculas (.lower()). (Lógica principal del while True)
## Reglas de Operación y Procesamiento
- Guardado de Datos: Los productos se guardan en el archivo con el nombre normalizado (minúsculas y sin espacios, excepto el codigo que no s normaliza). (agregar_productos()(usa normalizar()))
- Cálculo del Total: El valor total de un producto es el resultado de multiplicar la cantidad por el costo unitario (cantidad * precio). (ver_inventario(), calcular_total(), generar_reporte_final())
- Persistencia del Inventario: Las modificaciones (agregar, quitar, actualizar) siempre se aplican y guardan en el filepath_guardado (el archivo con la fecha de hoy), incluso si se cargó un archivo antiguo (filepath_cargar). (agregar_producto(), quitar_producto(), actualizar_inventario())
# Requerimientos Funcionales
## Requisitos funcionales del Sistema de Inventario
### Gestión de Archivos y Configuración Inicial
1. Carga/Selección de Archivo: El sistema debe permitir al usuario ingresar el nombre de un archivo de inventario y, opcionalmente, una fecha para buscar un archivo de inventario histórico.
2. Creación de Archivo: Si el archivo solicitado para cargar no existe, el sistema debe crear un nuevo archivo de inventario para guardar los cambios, utilizando el nombre de archivo base provisto por el usuario y la fecha actual.
3. Detección de Archivo Prohibido: El sistema debe impedir que el usuario use el nombre del reporte final del día actual (Reporte Final-d-m-a.txt) como el nombre base para el archivo de inventario.
4. Carga de Datos: El sistema debe poder leer y parsear los datos de un archivo de inventario (separados por comas) y cargarlos en la memoria para su procesamiento.
### Funcionalidades del CRUD (Crear, Leer, Actualizar, Borrar)
1. Agregar Producto: El sistema debe permitir al usuario ingresar un nuevo producto, solicitando su código, nombre, cantidad y costo unitario.
- Validación de Unicidad: Debe verificar que el código y el nombre del producto no existan ya en el inventario.
2. Quitar Producto: El sistema debe permitir al usuario eliminar un producto del inventario buscando su código único.
4. Ver Inventario: El sistema debe mostrar un listado completo de todos los productos en el inventario, incluyendo: Código, Producto, Cantidad, Precio Unitario y el Total de su valor (Cantidad × Precio).
5. Buscar Producto: El sistema debe permitir al usuario buscar y mostrar los detalles de un producto específico, identificándolo por su código. 
- Actualizar Producto: El sistema debe permitir modificar los datos de un producto existente.
### Procesamiento y Reportes
1. Cálculo del Valor Total: El sistema debe calcular y mostrar la suma del valor de todo el inventario (la sumatoria de Cantidad × Costo para todos los productos).
2. Generación de Reporte Final: El sistema debe ser capaz de generar un archivo de texto de reporte (Reporte Final-d-m-a.txt) que contenga:
- Número total de productos únicos.
- Valor total del inventario.
- Una tabla detallada con el Código, Nombre, Cantidad, Costo y Sub-Total por cada producto.
### Interacción con el Usuario
1. Menú de Opciones: El sistema debe presentar un menú con las opciones para acceder a cada una de las funcionalidades descritas.
2. Manejo de Errores en Entrada: El sistema debe manejar errores de ValueError (como ingresar texto donde se espera un número) y solicitar la reintroducción de datos.
3. Validación de Rangos: El sistema debe rechazar entradas inválidas como cantidades o costos negativos.
4. Retroalimentación: El sistema debe mostrar mensajes de carga y éxito (cargando()) para indicar al usuario que las operaciones se están llevando a cabo.
# Diseño de entradas y salidas
Diseño de entradas y salidas:
Entradas:
- Nombre del material
- Tipo que especifica el material
- Cantidad del material
- Costo del material
- Valores correctos de los materiales (Nombre,
cantidad y costo)
- Guardar los datos ingresados
- Opciones de cancelar el programa
Salidas:
- Listado de nombre, tipo de material, cantidad y costo
de cada uno
- Cotizar el costo total de todos los materiales
- Mostrar mensajes en caso de ingresar valores no
permitidos
- Volver a solicitar valores en caso de errores

# Diagrama de flujo

![Imagen_ALT](https://github.com/KianFrausto/Proyecto-FDP/blob/5fdb9eaf53f92f6752952d22de63def9588e3a54/docs/Inventario.png)

# Plan de trabajo
Semana 1:
- [✓] Planteamiento del problema a realizar. (Todos)
- [✓] Distribución de los roles. (Senior)
- [✓] Realización del GitHub (main) para uso del equipo.
(Senior)
- [✓] Realización de los commits dentro del repositorio de
GitHub (Todos)

Semana 2:
- [✓] Realización del pseudo-codigo para integración
completa del proyecto a realizar. (Senior)
- [✓] Actualización a una versión principal del código con
funciones completas. (Mids)
- [✓] Verificación del código base en busca de posibles
errores y optimización de entradas y salidas. (Juniors)
- [✓] Validación de las ramas creadas para su integración
dentro del código principal. (Senior)

Semana 3:
- [✓] Realización de actualizaciones dentro del programa
para futuras versiones. (Mids)
- [✓] Ajustar variables y validación de las funciones nuevas
del programa. (Juniors)
- [✓] Ajuste de ramas nuevas para validación de las
funciones dentro de la rama principal y validar un
funcionamiento correcto. (Senior)

Semana 4:
- [✓] Reajuste de nuevos comandos para parches dentro de
las versiones anteriores. (Mids)
- [✓] Simplificar funciones dentro del código para un
funcionamiento más optimo. (Junior)
- [✓] Integración para una versión final del código. (Senior)

Semana 5:
- [✓] Ultimas actualizaciones dentro del programa. (Mids)
- [✓] Revisión a detalle del código completo por posibles
errores en el código. (Juniors)
- [✓] Entrega del código en una fase completa lista para su
ejecución sin errores. (Senior)

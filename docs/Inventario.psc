Algoritmo InventarioMateriales
	Definir opcion, cantidad, costo, i, total Como Real
	Definir nombre, tipo Como Cadena
	Definir materiales Como Cadena
	Definir cantidades, costos Como Real
	Dimensionar nombres(100), tipos(100), cantidades(100), costos(100)
	i <- 0
	total <- 0
	Repetir
		Escribir '---- MENÚ ----'
		Escribir '1. Registrar material'
		Escribir '2. Mostrar lista de materiales'
		Escribir '3. Mostrar costo total'
		Escribir '4. Cancelar programa'
		Leer opcion
		Según opcion Hacer
			1:
				Repetir
					Escribir 'Ingrese nombre del material:'
					Leer nombre
					Si nombre='' Entonces
						Escribir 'Error: el nombre no puede estar vacío.'
					FinSi
				Hasta Que nombre<>''
				Repetir
					Escribir 'Ingrese tipo de material:'
					Leer tipo
					Si tipo='' Entonces
						Escribir 'Error: el tipo no puede estar vacío.'
					FinSi
				Hasta Que tipo<>''
				Repetir
					Escribir 'Ingrese cantidad del material:'
					Leer cantidad
					Si cantidad<=0 Entonces
						Escribir 'Error: la cantidad debe ser mayor a 0.'
					FinSi
				Hasta Que cantidad>0
				Repetir
					Escribir 'Ingrese costo unitario del material:'
					Leer costo
					Si costo<=0 Entonces
						Escribir 'Error: el costo debe ser mayor a 0.'
					FinSi
				Hasta Que costo>0
				nombres[i] <- nombre
				tipos[i] <- tipo
				cantidades[i] <- cantidad
				costos[i] <- costo
				i <- i+1
				Escribir 'Material registrado con éxito.'
			2:
				Si i=0 Entonces
					Escribir 'No hay materiales registrados.'
				SiNo
					Escribir '---- LISTA DE MATERIALES ----'
					Para j<-0 Hasta i-1 Con Paso 1 Hacer
						Escribir 'Material ', j+1, ': ', nombres[j], ' | Tipo: ', tipos[j], ' | Cantidad: ', cantidades[j], ' | Costo Unitario: ', costos[j]
					FinPara
				FinSi
			3:
				total <- 0
				Para j<-0 Hasta i-1 Con Paso 1 Hacer
					total <- total+(cantidades[j]*costos[j])
				FinPara
				Escribir 'El costo total de todos los materiales es: $', total
			4:
				Escribir 'Programa cancelado. ¡Hasta luego!'
			De Otro Modo:
				Escribir 'Opción no válida, intente de nuevo.'
		FinSegún
	Hasta Que opcion=4
FinAlgoritmo

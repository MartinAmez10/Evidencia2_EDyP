import csv
import sys
#import openpyxl
#No permite utilizar ese modulo

datos_grabar = dict()
datos_leer = dict()

datos = {}

try:

  with open("logs_libros.csv","r", newline="") as archivo:
      lector = csv.reader(archivo)
      next(lector)
      
      for identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion in lector:
          datos_leer[int(identificador)] = (titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion)
except FileNotFoundError:
    print("El archivo no se encontró, se procede a trabajar con un conjunto vacío\n\n")
except Exception:
    Excepcion = sys.exc_info()
    print(f"Ocurrió un problema del tipo: {Excepcion[0]}")
    print(f"Mensaje del error: {Excepcion[1]}")
else:
  print(datos_leer) #Remover esta prueba de carga de datos
  datos = datos_leer
  #for identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion in lector:
    #datos[identificador] = (titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion)

while True:
  print("Hola! selecciona una opcion que quieras realizar (escribe el numero):")
  print("[1]- Registrar nuevo ejemplar")
  print("[2]- Consultas y Reportes")
  print("[3]- Salir")
  op_main = int(input())
  
  if op_main == 1:
    # Registro de datos
    while True:
      identificador = max(datos, default=0)+1
      titulo = input("Dame el nombre del libro: \n").upper()
      autor = input(f"Dame el autor de {titulo}: \n").upper()
      genero = input(f"Cual es el genero de {titulo}: \n").upper()
      año_publicacion = input(f"En que año se publico {titulo}: \n").upper()
      ISBN = input(f"Cual es el ISBN de {titulo}: \n").upper()
      fecha_adquisicion = input(f"Cuando se adquirio {titulo}: \n").upper()
      datos[identificador] = [titulo,autor,genero,año_publicacion,ISBN,fecha_adquisicion]
      print("Datos cargados!")
      op_registro = input("Deseas agregar mas?(si es no clickea enter) \n")
      if op_registro.strip() == "":
        break
  elif op_main == 2:
    # Consultas y Reportes
    while True:
      print("Selecciona una opcion que quieras realizar (escribe el numero):")
      print("[1]- Consulta de titulo")
      print("[2]- Reportes")
      print("[3]- Regresar al menu principal")
      op_consulta = int(input())
      
      # Separamos por la opción seleccionada
      if op_consulta == 1:
        # Consulta de título o ISBN
        while True:
          print("De que forma deseas buscar el libro?(escribe el numero):")
          print("[1]- Por titulo")
          print("[2]- Por ISBN")
          print("[3]- Regresar al menu anterior")
          op_busqueda = int(input())
          if op_busqueda == 1:
            # Muestra el catálago de Libros (POR TÍTULO)
            for i in datos:
              print(datos[i][0])
            # Añadí esto para filtrar por título y mostrar información (Maybe lo módifico)
            titulo_buscar = input('Seleccione el título a mostrar: ').upper()
            for i in datos:
              if titulo_buscar == datos[i][0]:
                print(''*5, ' Datos del libro ', ''*5)
                print('\tTítulo: ', datos[i][0])
                print('\tAutor: ', datos[i][1])
                print('\tGénero: ', datos[i][2])
                print('\tAño de Publicación: ', datos[i][3])
                print('\tISBN: ', datos[i][4])
                print('\tFecha de Adquisición: ', datos[i][5])
                print('*'*27)
                break
          elif op_busqueda == 2:
            # Muestra el libro (POR ISBN)
            # 1h Para hacer esto dios mio, ya hace falta dormir
            isbn_buscar = input('Ingrese el ISBN: ')
            for i in datos:
              if isbn_buscar == datos[i][4]:
                print(''*5, ' Datos del libro ', ''*5)
                print('ISBN seleccionado: ', isbn_buscar)
                print('\tTítulo: ', datos[i][0])
                print('\tAutor: ', datos[i][1])
                print('\tGénero: ', datos[i][2])
                print('\tAño de Publicación: ', datos[i][3])
                print('\tFecha de Adquisición: ', datos[i][5])
                print('*'*27)
                break            
          elif op_busqueda == 3:
            break
      elif op_consulta == 2:
        # Reportes tabulados
        while True:
          print("Escoge una forma de filtrar los datos:")
          print("[1]- Por autor")
          print("[2]- Por genero")
          print("[3]- Por año de publicacion")
          print("[4]- Catálogo completo")
          print("[5]- Regresar al menu anterior")
          op_reporte = int(input())
          if op_reporte == 1:
            datos_grabar = dict()
            # Filtro por autor
            print('Seleccione entre los siguientes autores:')
            for j in datos:
              #print('Seleccione entre las siguientes opciones:')
              print(datos[j][1])
            filtro_autor = input("Dame el autor: \n").upper()
            print('TITULO', ' '*29, 'AUTOR', ' '*18, 'GÉNERO', ' '*8, 'AÑO', ' '*5, 'ISBN', ' '*8, 'ADQUIRIDO   ')
            for i in datos:
              if filtro_autor == datos[i][1]:
                print(f'{datos[i][0]:35} {datos[i][1]:25} {datos[i][2]:15} {datos[i][3]:8} {datos[i][4]:15} {datos[i][5]:12}')
                datos_grabar[i] = datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5]
                print('\n')

            # Exportación a formatos CSV o MsExcel
            print("Desea exportar los datos a algun formato de los siguientes?")
            print("[1]- CSV")
            print("[2]- MsExcel")
            print("[3]- Ninguno")
            op_exportar = int(input())

            # IF para filtrar el formato deseado
            # Exportación a CSV
            if op_exportar == 1:
              #for j in datos:
                #datos_grabar = datos
              archivo = open('logs_autor_' + filtro_autor.lower() + '.csv', 'w', newline='')
              grabador = csv.writer(archivo)
              grabador.writerow(('identificador', 'titulo', 'autor', 'genero', 'año_publicacion', 'ISBN', 'fecha_adquisicion'))
              print("Se exporto correctamente!")
              grabador.writerows([(identificador, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]) for identificador, datos in datos_grabar.items()])
              archivo.close()
              #'identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion'
              break
          
            # Exportación a MsExcel
            if op_exportar == 2:
              #libro = openpyxl.Workbook()
              #hoja = libro["Sheet"]
              #hoja.title = "primera"
              #hoja["A1"].value = "Identificador"
              #hoja["B1"].value = "Titulo"
              #hoja["C1"].value = "Autor"
              #hoja["D1"].value = "Genero"
              #hoja["E1"].value = "Año de publicacion"
              #hoja["F1"].value = "ISBN"
              #hoja["G1"].value = "Fecha adquisicion"

              #fila = 0
              #hoja["A2"].value = fila + 1
              #hoja["B2"].value = datos[identificador][0]
              #hoja["C2"].value = datos[identificador][1]
              #hoja["D2"].value = datos[identificador][2]
              #hoja["F2"].value = datos[identificador][3]
              #hoja["G2"].value = datos[identificador][4]
              #hoja["H2"].value = datos[identificador][5]

              #libro.save("reporte_libros.xlsx")
              print("Se exporto de manera correcta")
              break
          elif op_reporte == 2:
            datos_grabar = dict()
            # Filtro por género
            print('Seleccione entre los siguientes Géneros:')
            for j in datos:
              #print('Seleccione entre las siguientes opciones:')
              print(datos[j][2])
            
            filtro_genero = input("Dame el genero: \n").upper()
            print('TITULO', ' '*29, 'AUTOR', ' '*18, 'GÉNERO', ' '*8, 'AÑO', ' '*5, 'ISBN', ' '*8, 'ADQUIRIDO   ')
            for i in datos:
              if filtro_genero == datos[i][2]:
                print(f'{datos[i][0]:35} {datos[i][1]:25} {datos[i][2]:15} {datos[i][3]:8} {datos[i][4]:15} {datos[i][5]:12}')
                datos_grabar[i] = datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5]
                print('\n')

            # Exportación a formatos CSV o MsExcel
            print("Desea exportar los datos a algun formato de los siguientes?")
            print("[1]- CSV")
            print("[2]- MsExcel")
            print("[3]- Ninguno")
            op_exportar = int(input())

            # IF para filtrar el formato deseado
            # Exportación a CSV
            if op_exportar == 1:
              #for j in datos:
                #datos_grabar = datos
              archivo = open('logs_genero_' + filtro_genero.lower() + '.csv', 'w', newline='')
              grabador = csv.writer(archivo)
              grabador.writerow(('identificador', 'titulo', 'autor', 'genero', 'año_publicacion', 'ISBN', 'fecha_adquisicion'))
              print("Se exporto correctamente!")
              grabador.writerows([(identificador, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]) for identificador, datos in datos_grabar.items()])
              archivo.close()
              #'identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion'
              break
          
            # Exportación a MsExcel
            if op_exportar == 2:
              #libro = openpyxl.Workbook()
              #hoja = libro["Sheet"]
              #hoja.title = "primera"
              #hoja["A1"].value = "Identificador"
              #hoja["B1"].value = "Titulo"
              #hoja["C1"].value = "Autor"
              #hoja["D1"].value = "Genero"
              #hoja["E1"].value = "Año de publicacion"
              #hoja["F1"].value = "ISBN"
              #hoja["G1"].value = "Fecha adquisicion"

              #fila = 0
              #hoja["A2"].value = fila + 1
              #hoja["B2"].value = datos[identificador][0]
              #hoja["C2"].value = datos[identificador][1]
              #hoja["D2"].value = datos[identificador][2]
              #hoja["F2"].value = datos[identificador][3]
              #hoja["G2"].value = datos[identificador][4]
              #hoja["H2"].value = datos[identificador][5]

              #libro.save("reporte_libros.xlsx")
              print("Se exporto de manera correcta")
              break

          elif op_reporte == 3:
            # Filtrado por año
            datos_grabar = dict()
            print('Seleccione entre los siguientes Años de Publicacion:')
            for j in datos:
              #print('Seleccione entre las siguientes opciones:')
              print(datos[j][3])

            filtro_año = input("Dame el año de publicacion: \n").upper()
            print('TITULO', ' '*29, 'AUTOR', ' '*18, 'GÉNERO', ' '*8, 'AÑO', ' '*5, 'ISBN', ' '*8, 'ADQUIRIDO   ')
            for i in datos:
              if filtro_año == datos[i][3]:
                print(f'{datos[i][0]:35} {datos[i][1]:25} {datos[i][2]:15} {datos[i][3]:8} {datos[i][4]:15} {datos[i][5]:12}')
                datos_grabar[i] = datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5]
                print('\n')

            # Exportación a formatos CSV o MsExcel
            print("Desea exportar los datos a algun formato de los siguientes?")
            print("[1]- CSV")
            print("[2]- MsExcel")
            print("[3]- Ninguno")
            op_exportar = int(input())

            # IF para filtrar el formato deseado
            # Exportación a CSV
            if op_exportar == 1:
              #for j in datos:
                #datos_grabar = datos
              archivo = open('logs_fecha_publicado_' + filtro_año + '.csv', 'w', newline='')
              grabador = csv.writer(archivo)
              grabador.writerow(('identificador', 'titulo', 'autor', 'genero', 'año_publicacion', 'ISBN', 'fecha_adquisicion'))
              print("Se exporto correctamente!")
              grabador.writerows([(identificador, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]) for identificador, datos in datos_grabar.items()])
              archivo.close()
              #'identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion'
              break
          
            # Exportación a MsExcel
            if op_exportar == 2:
              #libro = openpyxl.Workbook()
              #hoja = libro["Sheet"]
              #hoja.title = "primera"
              #hoja["A1"].value = "Identificador"
              #hoja["B1"].value = "Titulo"
              #hoja["C1"].value = "Autor"
              #hoja["D1"].value = "Genero"
              #hoja["E1"].value = "Año de publicacion"
              #hoja["F1"].value = "ISBN"
              #hoja["G1"].value = "Fecha adquisicion"

              #fila = 0
              #hoja["A2"].value = fila + 1
              #hoja["B2"].value = datos[identificador][0]
              #hoja["C2"].value = datos[identificador][1]
              #hoja["D2"].value = datos[identificador][2]
              #hoja["F2"].value = datos[identificador][3]
              #hoja["G2"].value = datos[identificador][4]
              #hoja["H2"].value = datos[identificador][5]

              #libro.save("reporte_libros.xlsx")
              print("Se exporto de manera correcta")
              break

          elif op_reporte == 4:
            # Catálogo completo
            print("DATOS GUARDADOS:")
            print('TITULO', ' '*29, 'AUTOR', ' '*18, 'GÉNERO', ' '*8, 'AÑO', ' '*5, 'ISBN', ' '*8, 'ADQUIRIDO   ')
            print("*"*113)
            for i in datos: 
              print(f'{datos[i][0]:35} {datos[i][1]:25} {datos[i][2]:15} {datos[i][3]:8} {datos[i][4]:15} {datos[i][5]:12}')
            print("*"*113)

            # exportacion a formato CSV o a MsExcel
            print("Desea exportar los datos a algun formato de los siguientes?")
            print("[1]- CSV")
            print("[2]- MsExcel")
            print("[3]- Ninguno")
            op_exportar = int(input())

            # exportacion a CSV o MsExcel
            if op_exportar == 1:
              for j in datos:
                datos_grabar = datos
              archivo = open('logs_catalogo_completo.csv', 'w', newline='')
              grabador = csv.writer(archivo)
              grabador.writerow(('identificador', 'titulo', 'autor', 'genero', 'año_publicacion', 'ISBN', 'fecha_adquisicion'))
              print("Se exporto correctamente!")
              grabador.writerows([(identificador, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]) for identificador, datos in datos_grabar.items()])
              archivo.close()
              #'identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion'
              break
          
            # exportacion a MsExcel
            if op_exportar == 2:
              #libro = openpyxl.Workbook()
              #hoja = libro["Sheet"]
              #hoja.title = "primera"
              #hoja["A1"].value = "Identificador"
              #hoja["B1"].value = "Titulo"
              #hoja["C1"].value = "Autor"
              #hoja["D1"].value = "Genero"
              #hoja["E1"].value = "Año de publicacion"
              #hoja["F1"].value = "ISBN"
              #hoja["G1"].value = "Fecha adquisicion"

              #fila = 0
              #hoja["A2"].value = fila + 1
              #hoja["B2"].value = datos[identificador][0]
              #hoja["C2"].value = datos[identificador][1]
              #hoja["D2"].value = datos[identificador][2]
              #hoja["F2"].value = datos[identificador][3]
              #hoja["G2"].value = datos[identificador][4]
              #hoja["H2"].value = datos[identificador][5]

              #libro.save("reporte_libros.xlsx")
              print("Se exporto de manera correcta")
              break
          elif op_reporte == 5:
            # Regresa al menú anterior
            break
      elif op_consulta == 3:
        # Regresa al menú anterior
        print('Volviendo al menú principal . . .')
        break

  elif op_main == 3:
    # Sale del programa
    break

for j in datos:
  datos_grabar = datos
archivo = open('logs_libros.csv', 'w', newline='')

grabador = csv.writer(archivo)
grabador.writerow(('identificador', 'titulo', 'autor', 'genero', 'año_publicacion', 'ISBN', 'fecha_adquisicion'))
#'identificador, titulo, autor, genero, año_publicacion, ISBN, fecha_adquisicion'
grabador.writerows([(identificador, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]) for identificador, datos in datos_grabar.items()])
archivo.close()
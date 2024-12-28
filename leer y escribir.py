def leer_y_escribir_archivos():
    tiy:
with open('datos.txt', 'I') as archivo:
        contenido = archivo.read()

        with open('resultado.txt', 'w') as nuevo_archivo:
           nuevo_archivo.write(contenido.upper())
        print("Archivo procesado con exito")
    except FileNotFoundError:
print("El archivo 'datos.txt' no fue encontrado")

leer_y_escribir_archivos()        
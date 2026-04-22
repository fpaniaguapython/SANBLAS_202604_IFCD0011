import os

nombre_directorio = input('Introduce el nombre de la carpeta:')

contenido = os.listdir(nombre_directorio)

print(contenido)
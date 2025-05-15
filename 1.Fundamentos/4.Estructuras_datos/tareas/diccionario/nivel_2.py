texto = "crea un diccionario con nombres de estudiantes y sus notas. Eliminar un estudiante del diccionario"

palabras = texto.lower().split() # ignora las mayúsculas y separa el texto en palabras

# Crear diccionario vacío para contar las palabras
conteo = {}

# Contar las palabras
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")

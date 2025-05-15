estudiantes = {
        "Ana": 30,
        "Luis": 25,
        "Juan": 40
}
# Acceso al diccionario
print("\nLista de estudiantes y sus notas:")
print(estudiantes)

#Agregar nuevo estudiante
estudiantes["Lucia"] = 34
print("\nNuevo estudiante agregado: Lucia")
print(estudiantes)

# Modificar nota de un estudiante
estudiantes["Luis"] = 30
print("\nNota modificada: Luis")
print(estudiantes)

# Elimina un estudiante
del estudiantes["Juan"]
print("\nEstudiante eliminado: Juan")
print(estudiantes)

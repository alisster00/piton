'''
Diccionarios (dict)
- Definición: colección de pares. clave: valor
- Sintaxis = mi_diccionario = {"nombre": "Ana", "edad": 30}
- Características:
    - Claves únicas.
    - Acceso rápido a valores mediante claves.
    - Mutable

¿Qué es un diccionario (dict)?

Un diccionario es una colección de pares clave:valor.
Se usa para almacenar datos donde cada elemento tiene una clave única que apunta a un valor.

mi_diccionario = {"nombre": "Ana", "edad": 30}

Características de los diccionarios:
    - Claves únicas: No puede haber dos iguales.
    - Valores mutables: puedes cambiar el valor asociado a una clave.
    - Acceso rápido: busca por clave es muy eficiente.
    - No ordenado, pero mantiene orden inserción
'''

# CREAR DICCIONARIO
# Forma básica:
persona = {"nombre": "Carlos", "edad": 25}

# Usando dict()
persona = dict(nombre="Carlos", edad=25)

# Diccionario vacío
vacio = {}

# ACCESO Y MODIFICACIÓN
# Acceder a un valor

print(persona["nombre"]) # Carlos

# Modificar un valor
persona["edad"] = 26

# Agregar nueva clave:valor
persona["ciudad"] = "Madrid"

# METODOS UTILES
'''
keys()                  devuelve las claves
values()                devuelve los valores
items()                 devuelve pares (clave, valor)
get(clave, valor_def)   devuelve valor o valor_def si no existe
pop(clave)              elimina y devuelve el valor
update(otro_dict)       actualiza con pares de otro dict
clear()                 vacía el diccionario
'''

# Ejemplos:
print(persona.keys())   # dict_keys(['nombre', edad', 'ciudad'])
print(persona.get("país", "Desconocido")) # Desconocido

# RECORRER UN DICCIONARIO
# Por claves
for clave in persona:
    print(clave, persona[clave])

# Por claves y valores
for clave, valor in persona.items():
    print(clave, "->", valor)

# Eliminar elmeentos
del persona["ciudad"] # Elimina la clave 'ciudad'
persona.pop("edad")  # Elimina 'edad' y devuelve su valor

# EJEMPLO COMPLETO

# Crear diccionario
alumno = {"nombre": "Laura", "edad": 22, "carrera": "Ingeniería"}

# Acceder
print(alumno["nombre"])

# Modificar
alumno["edad"] = 23

# Agregar
alumno["universidad"] = "UPM"

# Recorrer
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

# Eliminar
alumno.pop("carrera")

print(alumno)

# Diccionarios anidados
# puedes tener diccionarios dentro de diccionarios (estructura tipo JSON)

usuario = {
        "user1": {"nombre": "Ana", "edad": 30},
        "user2": {"nombre": "Luis", "edad": 25}
}
print(usuarios["user1"] ["nombre"] # Ana

# Diccionario por compresión
# Forma rápida de crear diccionarios

cuadrados = {x: x**2 for x in range(5)}
print(cuadrados) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

'''
Ventajas:
- Acceso rápido a datos por clave
- Estructura flexible: puedes almacenar cualquier tipo de dato como valor.
- Ideal para representar datos estructuras (tipo JSON)

Desventajas:
- No permite claves mutables (claves deben ser inmutables como strings, números o tuplas)
- Uso de memoria un poco mayor que listas para datos simples.


BONUS: defaultdict y OrderedDict
Python tiene variantes especiales en el módulo collections:

- defaultdict: asigna valores por defecto automáticamente
- OrderdDict: garantiza orden incluso en versiones antiguas de Python
'''

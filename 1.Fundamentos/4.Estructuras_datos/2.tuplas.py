'''
Tuplas (tuple)
- Definición: colección ordenada pero inmutable
- Sintaxis: mi_tupla = (1, 2, 3)
- Características:
    - No se puede modificar después de crearla
    - Más eficiente en memoria que las listas
    - Se puede usar como clave en un diccionario
      (si todos sus elementos son inmutables).

Una tupla es una colección ordenada e inmutable en Python.
Es similar a una lista, pero una vez creada, no se puede modificar.

Características de las tuplas:
- Ordenadas: los elementos tienen un orden fijo.
- Inmutables: no puedes agregar, eliminar ni cambiar elementos después de crearla
- Permiten duplicados: como las listas, puedes tener elementos repetidos.
- Eficiencia: usan menos memoria y son más rápidas que las listas.

¿Por qué usar tuplas?
- Si necesitas una colección que no cambie (seguridad)
- Para usar como clave un diccionario (solo tuplas son válidas, no listas)
- Cuando quieres aprovechar su mayor rendimiento en lectura.
'''

# ¿Cómo crear una tupla?
# Tupla común:
mi_tupla = (10, 20, 30)

# Tupla con un solo elemento:
tupla = (5, ) # La coma es necesaria

# Convertir lista a tupla
lista = [1, 2, 3]
tupla = tuple(lista)

# Acceso a elementos:
# funciona igual que en listas:
print(mi_tupla[0]) # 10
print(mi_tupla[-1]) # 30

# Operación con tupla:
# concatenación:
t1 = (1, 2)
t2 = (2, 4)
t3 = t1 + t2 # (1, 2, 3, 4)

# Repetición
t = (1, 2)
t_repetida = t * 3 # (1, 2, 1, 2, 1, 2)

# Desempaquetado:
a, b, c = (10, 20, 30)
print(a) # 10

'''
Métodos disponibles

count(x)    Cuenta cuántas veces aparece x.
index(x)    Devuelve el índice de x
'''
mi_tupla = (1, 2, 2, 3)
print(mi_tupla.count(2)) # 2
print(mi_tupla.index(3)) # 3

# Ejemplo completo:

# crear tupla
coordenadas = (100, 200)

# acceso
x = coordenadas[0]
y = coordenadas[1]

# desempaquetado
a, b = coordenadas

# concatenación
nueva_tupla = coordenadas + (300, 400)

# métodos
print(nueva_tupla.count(100))
print(nueva_tupla.index(300))

'''
Ventajas:
    - Inmutabilidad: evita cambios accidentales.
    - Rendimiento: mejor uso de memoria y velocidad
    - Seguridad: ideales para todos constantes

Desventajas:
    - No puedes modificarlas sin crear una nueva
    - Tine menos métodos que las listas
'''

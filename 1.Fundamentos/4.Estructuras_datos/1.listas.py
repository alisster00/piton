'''
Listas (list)

- Definición: colección ordenada y mutable de elementos
              que permite guardar una secuencia de elementos.
- Sintaxis = mi_lista = [1, 2, 3, 4]
- Características:
    - Prmite duplicados
    - Se puede modificar (agregar, eliminar o cambiar elementos)
    - Se accede por índice (empieza en 0=

# Ejemplo:
mi_lista = [1, 2, 3, "hola", True]

Características de las listas:
- Ordenadas: los elementos tienen un orden fijo, y se puede acceder a ellos por índice.
- Mutables: se pueden modificar después de ser creadas (agregar. eliminar o cambiar elemento)
- Permiten duplicados: puedes tener elementos repetidos.
- Aceptan múltiples tipos: puedes mezclar enteros, cadenas, booleanos, etc.
'''

# OPERACIONES BASICAS

# Acceso a elementos:
mi_lista = [10, 20, 30, 40]
print(mi_lista[0]) # 10
print(mi_lista[-1]) # 40 (ÚLTIMO ELEMENTO)

# Modificar un elemento
mi_lista[1] = 25 # Ahora mi_lista es [10, 25, 30, 40]

'''
Métodos útiles de las listas:
append(x)       agrega x al final de la lista.
insert(i, x)    inserta x en la posición i
remove(x)       elimina la primera concurrencia de x
pop([i])        elimina y devuelve el elemento en posición
sort()          ordena la lista (en su lugar)
reverse()       invierte los elementos de la lista
index(x)        devuelve el indice de la primera posición
count(x)        cuenta cuántas veces aparece x
extend(iterable)agrega todos los elementos iterables
'''
# Ejemplo:
mi_lista = [1, 2, 3]
mi_lista.append(4)  # [1, 2, 3, 4]
mi_lista.remove(2)  # [1, 3, 4]
mi_lista.sort()     # [1, 3, 4]

# Slicing (sublistas)
# puede obtenerse partes de una lista usando slicing:
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[1:4]    # [20, 30, 40]

# Lista de comprensión (list comprehension)
# forma compacta y poderosa de crear listas
# lista de cuadrados
cuadrados = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]

# Ejemplo competo:

# crear lista
numeros = [1, 2, 3]

# Agregar elementos
numeros.append(4)
numeros.extend([5, 6])

# Acceder y modificar
print(numeros[0]) # 1
numeros[0] = 10

# Remover elementos
numeros.remove(2)
ultimo = numeros.pop()

# Slicing
print(numeros[1:3]) # [3, 4]

# List comprehension
pares = [x for x in numeros if x % 2 == 0]
print(pares)

'''
Ventajas
- Muy flexible
- Amplio soporte nativo
- Permite manipulación eficiente para la mayoría de casos generales.

Desventajas:
- Menos eficiente en grandes cantidaddes de datos
comparado con arrays de librerías como NumPy.
- Almacena referencias a objetos, lo que puede consumir más memoria.
'''

# pendientes:
# map, filter

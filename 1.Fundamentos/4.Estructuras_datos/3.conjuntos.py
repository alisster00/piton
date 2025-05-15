'''
Conjuntos (set)
- Definición: conlección no ordenada de elementos únicos.
- Sintaxis: mi_conjunto = {1, 2, 3}
- Características:
    - No permite duplicados.
    - Soporta operaciones matemáticas como unión, intersección y diferencia.
    - No se puede acceder por índice (porque no es ordenado).

Un conjunto es una colección no ordenada de elementos únicos. 
Es muy útil cuando quieres eliminar duplicados o hacer operaciones de tipo matemático 
como unión, intersección o diferencia.

Caracteríscticas de los conjuntos:
- No permiten duplicados: Cada elemento aparece solo una vez.
- No están ordenados: no puedes acceder a los elementos por índice.
- Mutable: puedes agregar y eliminar elementos.
- Aceptan múltiples tipos: pero los elements deben ser inmutables 
(por ejemplo, no puedes meter una lista dentro de un set).
'''

# COMO CREAR UN CONJUNTO:
# Con llaves {}
mi_conjunto = {1, 2, 3}

# Usando set():
mi_conjunto = set([1, 2, 2, 3]) # {1, 2, 3}

# Conjunto vacío (¡importante!):
vacio = set() # No uses {} porque eso crea un diccionario

# OPERACIONES BASICAS
# Agregar elementos
mi_conjunto.add(4)

# Eliminar elementos
mi_conjunto.remove(2) # Lanza error si no existe
mi_conjunto.discard(5) # No lanza error si no existe

# Limpiar y borrar
mi_conjunto.clear() # vacía el conjunto

# Operación             Símbolo / Método            Ejemplo
# Unión                 `                           o.union()`
# Intersección          & O .intersection()         a & b
# Diferencia            - o .diference()            a - b
# Diferencia simétrica  ^ o .symmetric_difference() a ^ b

# Ejemplo:
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # {1, 2, 3, 4, 5} (union) 
print(a & b) # {3} (interseccion)
print(a - b) # {1 ,2} (diferencia)
print(a ^ b) # {1, 2, 3, 4, 5} (diferencia simétrica)


# Eliminar duplicados usando un set
lista = [1, 2, 2, 3, 3, 3]
sin_duplicado = list(set(lista)) # [1, 2, 3]

'''
Métodos útiles de set

add(x)              agrega x al conjunto
remove(x)           eliina x; error si no existe
discard(x)          elimina x; no error si no existe
clear()             elimina todos los elementos
unio(otro_set)      devuelve la unión
intersection(o_set)     devuelve la intersección
difference(o_set)   devuelve la intersección
symetric_difference(otro_set)       devuelve la diferencia simétrica
'''

# Ejemplo completo:

# crear un conjunto
frutas = {"manzana", "pera", "naranja"}

# Agregar elemento
frutas.add("platano")

# Elimina elemento
frutas.discard("pera")

# Unión
otras_frutas = {"kiwi", "naranja"}
todas = frutas.union(otras_frutas)

print(todas)

'''
Ventajas
- Elimina duplicado automáticamente
- Operaciones matemáticas rápidas
- Más eficiente que las listas para comprobar si un elemento existe (in es muy rápido)

Desventajas
- No ordenado: no puedes acceder por índice
- No permite elementos mutables (nada como listas u otros sets dentro)
- Menos flexible que las listas o diccionarios para datos complejos

'''

# Bonus: frozenset
# si necesitas un conjunto inmutable, puedes usar un frozenset.
inmutable = frozenset([1, 2, 3])

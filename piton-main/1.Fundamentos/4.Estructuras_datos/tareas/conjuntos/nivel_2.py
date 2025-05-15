'''
2. Operaciones de conjuntos:
    - Crear dos sets con números y hallar la unión, intersección y diferencia.
    - Usar la diferencia simétrica para obtener elementos únicos en cada set.
'''

conjuno = {1, 2, 3}
conjudos = {1, 2, 4}

# intersección (imprime hasta el punto en que 'cambia')
intersec = conjuno.intersection(conjudos)
print(intersec)
print(conjuno & conjudos) # forma corta

# diferencia (imprime el número diferente)
diferencia = conjuno.difference(conjudos)
print(diferencia)
print(conjuno - conjudos) # forma larga

# unión (elimina repetidos)
otras_conj = conjudos
unir = conjuno.union(otras_conj)
print(unir)
print(conjuno | conjudos) # forma corta

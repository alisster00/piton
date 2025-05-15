# 4. Crear una lista con solo los múltiplos de 3 entre 1 y 50
#lista = [x*3 for x in range(1, 50)]
lista = [x for x in range(1, 50) if x % 3 == 0]

print(lista)

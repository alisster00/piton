# 2. Eliminar duplicados de una lista usando solo listas (sin usar set)

lista = [2, 3, 4, 3, 5, 7, 8, 2, 3, 8]

#listas = lista.count(7)

#print(listas)
for num in lista:
    repetidos = lista.count(num)
    if repetidos > 1:
        eliminar = lista.remove(num)
        print(lista)

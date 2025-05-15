'''
Crea un bucle que itere sobre una lista de palabras
y usa pass si la palabra es "Python" pero imprime el resto.
'''

lista = ["pajaro", "tijeras", "python", "bateria"]

for palabra in lista:
    if palabra == "python":
        pass
    else:
        print(palabra)

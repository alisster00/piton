# Son fundamentos para ejecutar bloques de código múltiples veces.

# Bucle while
# Ejecuta un bloque de código mientras la condición sea verdadera.

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Si no se actualiza la variable dentro del bucle, se genera un bucle infinito

# Bucle for
# Itera sobre una secuencia (lista, tuplas, cadenas, rangos, etc.)
# con range()
for i in range(5):
    print(i)    # imprime de 0 a 4

# iterando sobre una lista:
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# iterando sobre una cadena:
for letra in "Python":
    print(letra)

## Funciones útiles con for
# range(inicio, fin, paso):
for i in range(2, 10, 2): # de 2 a 8, de dos en dos
    print(i)

# enumerate(): para obtener índice y valor
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# zip(): para iterar sobre varias secuencias a la vez
nombre = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")


## Control de bucles
# break: termina el bucle
# continue: salta a la siguiente iteración
# pass: no hace nada (relleno)

for i in range(10):
    if i == 5:
        break # sale del bucle cuando i es 5
    if i % 2 == 0:
        continue # salta los números pares
    print(i)

# Bucles anidados (un bucle dentro de otro bucle)
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Cláusula else en bucles
# Poco conocida: el bloque else se ejecuta si el bucle termina sin un break

for i in range(5):
    if i == 7:
        break
else:
    print("Bucle completado sin interrupción")
# Aquí el else se ejecuta porque nunca se hizo break

#Pendiente: list comprehension

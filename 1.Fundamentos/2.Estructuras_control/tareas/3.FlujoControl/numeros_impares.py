'''
Usa un bucle para imprimir solo los números impares del 1 al 10.
Usa continue para saltar los pares.
'''
print("bucle for:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


print("bucle while:")

num = 1
while num < 11:
    if num % 2 == 0:
        print(num - 1)
    num += 1


'''
Haz un bucle que cuente de 10 a 0 y alllegar a 0 imprima "¡Despegue!".
'''
import time

print("Bucle for")
for i in range(10, -1, -1):
    print(i)
    if i == 0:
        print("¡Despegue!")

print("\nBucle while")
num = 10
while num >= 0:
    print(num)
    num -= 1
    if num < 0:
        print("¡Despegue!")

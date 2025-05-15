'''
Crea ua mini calculadora con funciones:
- Usa función para sumar
- Otra para restar
- Otra para multiplicar
- Otra para dividir (con manejo para no dividir por cero)

Y una función principal que, segun el operador que le pases (+, -, *, /),
llame a la función correcta.
'''

# Función que hace la suma
def sumar(a, b):
    return a + b

# Función que hace la resta
def restar(a, b):
    return a - b

# Función que hace la multiplicación
def multi(a, b):
    return a * b

# Función que hace la división (manejo para no dividir por cero)
def divi(a, b):
        return a / b

# Función que hace las operaciones (main)
def operacion():
    a = float(input("Inserta un número: "))
    b = float(input("Inserta otro número: "))
    c = str(input("Inserta un operador: "))

    if c == "+":
        print(sumar(a, b))

    elif c == "-":
        print(restar(a, b))

    elif c == "*":
        print(multi(a, b))
    
    elif c == "/":
        if b == 0:
            print("Error, no puedes dividir por 0")
        else:
            print(divi(a, b))
    else:
        print("Valor inválido")

operacion()

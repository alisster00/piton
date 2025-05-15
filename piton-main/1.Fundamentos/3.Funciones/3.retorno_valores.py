'''
Cuando una función retorna un valor, 
significa que la función 'devuelve' un resultado que puede ser usado después. 
Se usa la palabra clave return.
Si no se usa return, la función no devuelve nada
(devuelve None por defecto).
'''

# Ejemplo de retorno:
def sumar(a, b):
    return a + b # devuelve el resultado
resultado = sumar(3, 4)
print(resultado) # imprime 7

# - Aquí la función sumar devuelve la suma de a y b.
# - La variable resultado guarda ese valor retornado

# Diferencia entre print y return

def sin_retorno():
    print("Hola")

def con_retorno():
    return "Hola"

x = sin_retorno() # Esto imprime Hola pero x es None
y = con_retorno() # y ahora contiene "Hola"

print(x) # None
print(y) # Hola

# print() solo muestra algo en pantalla
# return devuelve un valor que puedes guardar, procesar o usar después

# Retornar múltiples valores
# permite retornar más de un valor, que llega como tupla
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(10, 5)
print(f"Suma: {s}, Resta: {r}")

# Retorna sin valor:
# solo si usas return sin nada, o no usas return, la función se vuelve None.
def nada():
    return
print(nada()) # imprime None

'''
¿Cuándo usar return?
- Cuando necesitas que tu función devuelva datos para ser usados más tarde.
- Es esencial en funciones que hacen cálculos, transforman datos o toman decisiones.
'''


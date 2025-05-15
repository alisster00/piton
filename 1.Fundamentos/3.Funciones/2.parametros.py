'''
Parámetros: es la 'variable' que aparece cuando defines la función.
Argumento: es el valor 'real' que pasas cuando llamas a la función.
'''

def saludar(nombre): # nombre es el parámetro
    print(f"Hola, {nombre}")
saludar("Carlos") # carlos es el argumento

# Tipos de parámetros:
# 1.Parámetros Posicionales:
# Son los más comunes. Se pasan en el mismo orden en que están definidos.

def sumar(a, b):
    return a + b
print(sumar(3, 5)) # 3 y 5 son argumentos posicionales

# 2. Parámetros con valor por defecto:
# Si no pasas un valor, se usa el que se ha definido por default
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")
saludar()           # Usa amigo
saludar("Laura")    # Usa Laura

# 3. Parámetros con nombre (keywords)
# Puedes especificar el nombre al llamar la función, no importa el orden

def presentar(nombre, edad):
    print(f"{nombre} tiene {edad}")
presentar(edad= 25, nombre="Luis")

# 4. Parámetros variables:
# *args: recibe muchos argumentos posicionales como una tupla.
# **kwargs: recibe muchos argumentos con nombre como un diccionario.

def sumar_todo(*args):
    return sum(args)
print(sumar_todo(1, 2, 3, 4))   # 10

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_info(nombre="Ana", edad=30)

'''
Resumen:
Posicional:         función(1, 2)
Por defecto:        def func(x=10)
Con nombre(kw):     funcion(y=5, x=2)
Múltiples(*args):   def func(*args)
Múltiples(**kwargs) def func(**kwargs)
'''

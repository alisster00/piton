# Definir una función:
def nombre_de_la_funcion(parametros):
    # bloque de código
    return resultado # opcional

# Ejemplo de función:
def saludar():
    print("Hola, ¿cómo estás?")

# llamar a la función
saludar()

# Función con parámetros:
def saludar_a(nombre):
    print(f"Hola, {nombre}!")
saludar_a("Ana")

# Función que devuelve un valor
def sumar(a, b):
    return a + b
resultado = sumar(3, 5)
print(resultado) # imprime 8

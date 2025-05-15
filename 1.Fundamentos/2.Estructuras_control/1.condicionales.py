# Estructuras condicionales
# Permiten ejecutar código solo si se cumple una condición.

# if: 
    #ejecuta un bloque si la condición es verdadera
x = 10
if x > 5:
    print("x es mayor que 5")

# if-else: 
    #permite comprobar múltiples condiciones
if x > 5:
    print("Mayor que 5")
else:
    print("5 o menor")

# if-elif-else:
    #captura cualquier caso que no haya cumplido condiciones anteriores
if x > 10:
    print("Mayor que 10")
elif x == 10:
    print("Es 10")
else:
    print("MEnor que 10")

# Operadores comunes en conducionales:
# comparación: ==, !=, <, >, <=, >=
# lógicos: and, or, not
# membresía: in, not, in

x = 5
y = 10

if x < 10 and y > 5:
    print("Ambas condicions son verdaderas")

if x == 5 or y == 5:
    print("Al menos una condición es verdadera")

if not x == 6:
    print("x no es 6.")

# Condicionales anidados:
# Puede ir un if dentro de otro if para comprobar condiciones más específicas

numero = 15
if numero > 10:
    if numero < 20:
        print("El número está entre 10 y 20")

# Condicionales en una sola línea (if ternario)
# (expresión condicional / operador ternario)
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# Evaluación de valores "truthy" y "falsy"
# Valores como 0, '' (cadena vacía),
# [] (lista vacía), {} (diccionario vacío),
# None se consideran falsos.
# Tdo lo demás se considera verdadero
nombre = ""
if nombre:
    print("Nombre ingresado")
else:
    print("No ingresaste tu nombre")

# Saldŕa: "no ingresaste tu nombre" porque "" es falso

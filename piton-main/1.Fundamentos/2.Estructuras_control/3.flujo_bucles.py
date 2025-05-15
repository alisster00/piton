# Permite modificar cómo se comporta un bucle mientras está en ejecución.
# las tres instrucciones más usadas son: break, continue y pass

# brea - Rompe el bucle
# Esta instrucción termina el bucle inmediatamente,
# sin importar si aún quedan iteraciones

for i in range(10):
    if i == 5:
        break   # sale del bucle cuando i es 6
    print(i)

# continue - Salta a la siguiente iteración
# Hace que un bucle pase directamente a la siguiente vuelta
# sin ejecutar el código restante en esa iteración

for i in range(5):
    if i == 2:
        continue # Salta la impresión cuando i es 2 (2 no se imprime)
    print(i)

# pass - No hacer nada
# pass es un relleno. No afecta el flujo,
# simplemente indica a Python "no hacer nada aquí".
# Es útil cuando necesitas estructura sintácticamente
# correcta pero aún no has escrito el código

for i in range(3):
    if i == 1:
        pass # aquí no hacemos nada especial
    print(i)
# pass no cambia nada en la ejecución. Solo es un "especio en blanco válido"


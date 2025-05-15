'''
Crea una función con un parámetro con valor por defecto,
por ejemplo, que salude diciendo "Hola, amigo" si no le pasas nombre.
'''

def saludo(usuario="amigo"):
    print(f"Hola, {usuario}")

saludo("Akari")
saludo()

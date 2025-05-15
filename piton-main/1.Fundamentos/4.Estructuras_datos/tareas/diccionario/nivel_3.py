'''
3. Diccionario anidado:
    - Crear un diccionario con usuarios y sus datos personales (como nombre, edad y dicudad).
    - Imprimir solo los nombres de todos los usuarios.
'''

personas = {
        "user1": {"nombre": "Elias", "edad": 22, "ciudad": "Tokyo"},
        "user2": {"nombre": "Sarah", "edad": 41, "ciudad": "Santiago"}
}

print(personas["user1"] ["nombre"])
print(personas["user2"] ["nombre"])


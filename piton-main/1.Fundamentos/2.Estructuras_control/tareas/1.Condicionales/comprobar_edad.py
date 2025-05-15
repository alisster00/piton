'''
Pide al usuario su edad y di ses menor de edad,
mayor de edad, o si justo tiene 18 años.
'''
usuario = int(input("\n¿Cuál es tu edad?\n"))

if usuario < 18:
    print("Eres menor de edad")
elif usuario == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")

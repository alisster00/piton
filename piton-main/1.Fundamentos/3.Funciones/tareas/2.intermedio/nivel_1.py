'''
Crea una función que reciba un número y retorne si es par o impar
'''

numero = int(input("Inserte un número: "))

# con print
def par_impar():
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
par_impar()

def impar_par(*args):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"

print(impar_par())

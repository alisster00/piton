'''
2. Clase Libro:
    - Atributos: titulo, autor, paginas, leido (booleano).
    - Método marcar_leido() que cambie el estado a True
'''

class Libro:
    def __init__(self, titulo, autor, paginas, leido):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.leido = leido

    def marcar_leido(self):
        usuario = str(input("Has leido este libro? (s/n) ")).lower()
        if usuario != "n":
            self.leido = True
            print(f"{self.titulo} de {self.autor}, el cual cuenta con {self.paginas}, ha sido leído: {self.leido}")
        else:
            print(f"{self.titulo} de {self.autor}, el cual cuenta con {self.paginas}, ha sido leído: {self.leido}")

libro = Libro("Don Quijote", "Miguel de Cervantes", 1424, False)

libro.marcar_leido()

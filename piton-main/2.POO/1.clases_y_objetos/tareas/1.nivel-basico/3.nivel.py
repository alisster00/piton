'''
Clase Rectángulo: recibe ancho y alto.
Agrega métodos:
    - area() que calcule el área
    - perimetro() que calcule el perimetro
'''

# alto = 12
# ancho = 18

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        print("El área del rectángulo es:", self.ancho * self.alto)

    def perimetro(self):
        print("El perímetro del rectángulo es:", (self.ancho + self.alto) *2)

area_rectangulo = Rectangulo(18, 12)
perimetro_rectangulo = Rectangulo(18, 12)

area_rectangulo.area()
perimetro_rectangulo.perimetro()



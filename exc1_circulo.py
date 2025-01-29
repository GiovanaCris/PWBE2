class Circulo:
    def __init__ (self, raio):
        self.raio = raio
        self.pi = 3.14

    def area(self):
        self.area = self.pi * self.raio ** 2
        print (f"A área é: {self.area:.2f}")

    def perimetro(self):
        self.perimetro = 2 * self.pi * self.raio
        print (f"O perímetro é: {self.perimetro:.2f}")

val_circulo = Circulo(10)

val_circulo.area()
val_circulo.perimetro()
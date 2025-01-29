class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
        
    def validacao(self):
        if (self.lado1 + self.lado2 > self.lado3) and (self.lado1 + self.lado3 > self.lado2) and (self.lado2 + self.lado3 > self.lado1):
            print("Triangulo válido!")
        else:
            print("Triangulo inválido!")
            
    def area(self):
        area_triangulo = (self.base * self.altura) / 2
        print(f"Área: {area_triangulo}")
        
triangulo = Triangulo(20, 20, 40, 30, 30)
triangulo.validacao()
triangulo.area()

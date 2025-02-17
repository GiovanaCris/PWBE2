class Retangulo:
    def  __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        self.area = self.largura * self.altura
        print (f"A área é {self.area}")
        
    def perimetro(self):
        self.perimetro = self.largura * 2 + self.altura * 2
        print (f"O perímetro é {self.perimetro}")
        
retangulo = Retangulo(50, 20)
retangulo.area()
retangulo.perimetro()


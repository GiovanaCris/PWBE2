class Funcionario:
    def __init__ (self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def dib(self):
        desc_imposto = self.salario / 30
        beneficio = 300
        salario_liquido = (self.salario - desc_imposto) + beneficio
        print (f"O salário líquido é R${salario_liquido:.2f}")

funcionario = Funcionario("Giovana", 1500 ,"Aprendiz")
funcionario.dib()
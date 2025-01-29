class Carro:
    def __init__(self, marca, modelo, vel_atual):
        self.marca = marca
        self.modelo = modelo
        self.vel_atual = vel_atual
        
    def acelerar(self):
        quant_acel = float(input("Digite a quantidade que deseja acelerar: "))
        calc_acel = self.vel_atual + quant_acel
        print (f"Velocidade atual: {calc_acel}")
            
    def frear(self):
        quant_frear = float(input("Digite a quantidade que deseja frear: "))
        calc_frear = self.vel_atual - quant_frear
        print (f"Velocidade atual: {calc_frear}")
            
    def manter(self):
        while True:
            manter = input("Deseja manter a velocidade? (s/n): ")
            if manter == "s":
                print (f"Velocidade: {self.vel_atual}")
            if manter == "n":
                print (f"Velocidade sem alteração!")
                break
    
carro = Carro("honda", "civic", 80)
carro.acelerar()
carro.frear()
carro.manter()
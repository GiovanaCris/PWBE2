class ContaBancaria:
    def __init__ (self, numero_conta, nome_titular):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = 100
    
    def deposito(self):
        desp = input("Deseja depositar? (s/n): ")
        if desp == "s":
            val_dep = float(input("Digite o valor que deseja depositar: "))
            self.saldo += val_dep
            print (f"Valor depositado com sucesso {self.saldo:.2f}!")

    def sacar(self):
        sac = input("Deseja sacar? (s/n): ")
        if sac == "s":
            val_sac = float(input("Digite o valor que deseja sacar: "))
            if val_sac > self.saldo:
                print ("Transação incompatível")

            else:
                self.saldo -= val_sac
                print (f"Valor sacado com sucesso {self.saldo:.2f}")

dados_banc = ContaBancaria("373829", "Maria")

dados_banc.deposito()
dados_banc.sacar()
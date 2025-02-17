class Banco:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cadastrar(self):
        print (f"Olá {self.nome}, necessito de alguns dados para a realização de seu cadastro")
        cpf_user = input("Digite seu CPF: ")
        rg_user = input("Digite seu RG: ")
        num_conta = 2763572
        print (num_conta)
        conf_conta = int(input("Digite o número da conta recebido: "))
        if num_conta == conf_conta:
            print ("Cadastro realizado com sucesso!")
        elif num_conta != conf_conta:
            print ("Número de confirmação diferente do número digitado, tente novamente!")
    
    def abrir_conta(self):
        num_conta = input("\nDigite o número da conta: ")
        criar_senha = input("Digite uma senha: ")
        confirm_senha = input("Confirme sua senha: ")
        if criar_senha == confirm_senha:
            print ("Conta aberta com sucesso! ")
        elif criar_senha != confirm_senha:
            print ("A senha criada é diferente da senha confirmada, tente novamente!")

    def saque(self):
        saldo = 500
        print (f"\nSeu saldo é {saldo}")
        val_saque = int(input("Digite o valor que deseja sacar: "))
        saq = saldo - val_saque
        if val_saque < saldo:
            print (f"Saque de {val_saque} realizado, seu saldo atual é {saq}")
        elif val_saque > saldo:
            print (f"Valor do saque superior ao saldo da conta, tente novamente!")

    def deposito(self):
        saldo = 300
        print (f"\nSeu saldo é {saldo}")
        val_dep = int(input("Digite o valor que deseja depositar: "))
        dep = saldo + val_dep
        print (f"Depósito realizado com sucesso! Saldo atual {dep}")
    
    def transferencia(self):
        saldo = 500
        cont_destino = input("\nDigite a conta de destino: ")
        val_transacao = int(input("Digite o valor da transação: "))
        if val_transacao <= saldo:
            print (f"Transação realizada com sucesso para {cont_destino}")
        elif val_transacao > saldo:
            print (f"Valor da transação maior que o saldo da conta, tente novamente!")

banco = Banco ("Maria", 19)
banco.cadastrar()
banco.abrir_conta()
banco.saque()
banco.deposito()
banco.transferencia()
class MáquinaDeVendas:
    def __init__(self):
        self.produtos = {}  
        self.precos = {}    
        self.estoque = {}  

    def cadastrar_produto(self):
        i = len(self.produtos) + 1
        print(">>>>> CADASTRAR PRODUTO <<<<<")
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))

        self.produtos[i] = nome
        self.precos[i] = preco
        self.estoque[i] = quantidade

        print(f"Produto {nome} cadastrado com sucesso!\n")

    def exibir_estoque(self):
        print(">>>>> ESTOQUE DISPONÍVEL <<<<<")
        for i in self.produtos:
            nome = self.produtos[i]
            preco = self.precos[i]
            quantidade = self.estoque[i]
            print(f"{i} - {nome} | Preço: R$ {preco:.2f} | Estoque: {quantidade}")
        print()

    def comprar_produto(self):
        self.exibir_estoque()
        escolha = int(input("Digite o número do produto que deseja comprar: "))

        if escolha not in self.produtos:
            print("Produto inválido.\n")
            return

        if self.estoque[escolha] <= 0:
            print("Produto fora de estoque.\n")
            return

        preco = self.precos[escolha]
        print(f"O produto escolhido foi: {self.produtos[escolha]} - R$ {preco:.2f}")
        dinheiro = float(input("Insira o valor (R$): "))

        if dinheiro < preco:
            print("Dinheiro insuficiente. Tente novamente\n")
            return

        troco = dinheiro - preco
        self.estoque[escolha] -= 1
        print(f"Compra realizada com sucesso! Troco: R$ {troco:.2f}\n")

maquina = MáquinaDeVendas()
print("\n>>>>>>>>Seja bem vindo ao buypy!<<<<<<<<<")
while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar produto")
    print("2 - Exibir estoque")
    print("3 - Comprar produto")
    print("4 - Sair")
    opcao = input("Digite a opção: ")

    if opcao == '1':
        maquina.cadastrar_produto()
    elif opcao == '2':
        maquina.exibir_estoque()
    elif opcao == '3':
        maquina.comprar_produto()
    elif opcao == '4':
        print("Te espero na próxima!!")
        break
    else:
        print("Opção inválida!\n")
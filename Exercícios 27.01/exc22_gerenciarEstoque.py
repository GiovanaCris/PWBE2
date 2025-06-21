class Produto:
    def __init__(self, nome, preco_compra, preco_venda, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def comprar(self, qtd):
        self.quantidade += qtd

    def vender(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            print(f"✅ Venda de {qtd} unidades realizada.")
        else:
            print("❌ Estoque insuficiente.")

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self):
        nome = input("Nome: ")
        compra = float(input("Preço de compra: "))
        venda = float(input("Preço de venda: "))
        qtd = int(input("Quantidade inicial: "))
        self.produtos.append(Produto(nome, compra, venda, qtd))
        print("✅ Produto adicionado.")

    def listar_produtos(self):
        print("\n📋 Produtos no estoque:")
        for p in self.produtos:
            print(f"{p.nome} | Estoque: {p.quantidade} | Compra: R${p.preco_compra:.2f} | Venda: R${p.preco_venda:.2f}")

    def comprar_produto(self):
        nome = input("Nome do produto: ")
        for p in self.produtos:
            if p.nome == nome:
                qtd = int(input("Quantidade comprada: "))
                p.comprar(qtd)
                print("✅ Compra registrada.")
                return
        print("❌ Produto não encontrado.")

    def vender_produto(self):
        nome = input("Nome do produto: ")
        for p in self.produtos:
            if p.nome == nome:
                qtd = int(input("Quantidade vendida: "))
                p.vender(qtd)
                return
        print("❌ Produto não encontrado.")

estoque = Estoque()
print("\n>>>>>>Seja bem vindo ao GerenciAqui<<<<<<<")
while True:
    print("\n2O que deseja realizar?")
    print("1 - Cadastrar produto")
    print("2 - Comprar produto (aumentar estoque)")
    print("3 - Vender produto (reduzir estoque)")
    print("4 - Ver produtos")
    print("5 - Sair")

    opc = input("Escolha: ")

    if opc == "1":
        estoque.adicionar_produto()
    elif opc == "2":
        estoque.comprar_produto()
    elif opc == "3":
        estoque.vender_produto()
    elif opc == "4":
        estoque.listar_produtos()
    elif opc == "5":
        print("Te espero na próxima 👋")
        break
    else:
        print("❌ Opção inválida.")
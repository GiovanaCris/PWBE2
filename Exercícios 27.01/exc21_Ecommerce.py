class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.total = 0

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))
        self.total += produto.preco * quantidade

    def aplicar_desconto(self, porcentagem):
        self.total -= self.total * (porcentagem / 100)

    def calcular_frete(self, km):
        frete = 5 + 0.5 * km
        self.total += frete
        print(f"Frete: R$ {frete:.2f}")

    def finalizar(self):
        self.cliente.historico.append(self)
        print(f"\n🧾 Pedido finalizado - Total: R$ {self.total:.2f}")

    def mostrar_itens(self):
        for p, q in self.itens:
            print(f"{q}x {p.nome} (R$ {p.preco:.2f})")
        print(f"Total atual: R$ {self.total:.2f}")

class SistemaEcommerce:
    def __init__(self):
        self.produtos = []
        self.clientes = []

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        categoria = input("Categoria: ")
        self.produtos.append(Produto(nome, preco, categoria))
        print("✅ Produto cadastrado.")

    def cadastrar_cliente(self):
        nome = input("Nome do cliente: ")
        cliente = Cliente(nome)
        self.clientes.append(cliente)
        print("✅ Cliente cadastrado.")

    def encontrar_cliente(self, nome):
        for c in self.clientes:
            if c.nome == nome:
                return c
        return None

    def encontrar_produto(self, nome):
        for p in self.produtos:
            if p.nome == nome:
                return p
        return None

    def recomendar(self, cliente):
        categorias = {}
        for pedido in cliente.historico:
            for produto, _ in pedido.itens:
                categorias[produto.categoria] = categorias.get(produto.categoria, 0) + 1

        if categorias:
            preferida = max(categorias, key=categorias.get)
            sugestoes = [p.nome for p in self.produtos if p.categoria == preferida]
            print(f"🎯 Recomendação ({preferida}): {', '.join(sugestoes)}")
        else:
            print("Nenhuma recomendação disponível.")

sistema = SistemaEcommerce()

while True:
    print("\n>>>>>>> Bem vendo ao PyCommerce <<<<<<<")
    print("1 - Cadastrar produto")
    print("2 - Cadastrar cliente")
    print("3 - Fazer pedido")
    print("4 - Ver recomendações")
    print("5 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        sistema.cadastrar_produto()

    elif opc == "2":
        sistema.cadastrar_cliente()

    elif opc == "3":
        nome_cliente = input("Nome do cliente: ")
        cliente = sistema.encontrar_cliente(nome_cliente)
        if not cliente:
            print("Cliente não encontrado.")
            continue

        pedido = Pedido(cliente)

        while True:
            print("\nProdutos disponíveis:")
            for p in sistema.produtos:
                print(f"- {p.nome} | R${p.preco:.2f} | {p.categoria}")

            nome_prod = input("Digite o nome do produto (ou 'fim' pra encerrar): ")
            if nome_prod.lower() == "fim":
                break

            prod = sistema.encontrar_produto(nome_prod)
            if prod:
                qtd = int(input("Quantidade: "))
                pedido.adicionar_item(prod, qtd)
            else:
                print("Produto não encontrado.")

        pedido.mostrar_itens()

        desc = float(input("Desconto (%): "))
        pedido.aplicar_desconto(desc)

        frete_km = float(input("Distância para entrega (km): "))
        pedido.calcular_frete(frete_km)

        pedido.finalizar()

    elif opc == "4":
        nome = input("Nome do cliente: ")
        cliente = sistema.encontrar_cliente(nome)
        if cliente:
            sistema.recomendar(cliente)
        else:
            print("Cliente não encontrado.")

    elif opc == "5":
        print("Que pena que já vai :/ Até mais! 🛒")
        break

    else:
        print("Opção inválida.")

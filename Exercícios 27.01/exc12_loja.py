class LojaVirtual:
    def __init__(self):
        self.produto = {}
        self.precos = {}

    def cadastrar_produto(self):
        #Adiciona produtos na biblioteca vazia
        i = len(self.produto) + 1
        print ("\nPara cadastrar produtos: ")

        nome_prod = input("Digite o nome do produto: ")
        #Adicona o nome do produto na lista de nomes
        self.produto[i] = nome_prod

        val_prod = int (input("Digite o valor do produto: "))
        #Adiciona o valor na lista de valor dos produtos
        self.precos[i] = val_prod
        print ("Produto adicionado com sucesso.\n")

    def excluir_produtos(self, indice_excluir):
            indice_excluir = indice_excluir
            if indice_excluir in self.produto:
                del self.produto[indice_excluir]
                #Deleta o produto da lista
                del self.precos[indice_excluir]
                #Deleta o preço da lita
                print (f"O produto {indice_excluir} foi excluído com sucesso!\n")
            elif indice_excluir not in self.produto:
                print ("Produto não encontrado. Por favor tente novamente!\n")
        

    def carrinho(self): 
        desconto = 10
        #Printa o índice, nome e preço do produto
        for i, nome_prod in self.produto.items():
            print(f"\nIndice: {i} \n Produto: {nome_prod} \n Valor: {self.precos[i]}")
        escolha = int(input("\nDigite o índice do produto que deseja: "))

        if escolha in self.produto:
            preco = float(self.precos[escolha])
            valor_total = preco - desconto
            print(f"Produto: {self.produto[escolha]} \nPreço: {self.precos[escolha]} \nDesconto: {desconto} \nValor total: {valor_total}\n")

        elif escolha not in self.produto:
            print("O índice informado não existe.")
            
loja = LojaVirtual()

while True:
    escolha = int(input("\nQual sua função? \n 1 - Adm \n 2 - Cliente\n"))
    if escolha == 1:
        codigo = 12345 #Código para o adm digitar
        cod_user = int(input("\nDigite o número do código informado em seu telefone: "))

        #Realiza essas determinadas funções se o código do adm estiver correto
        if cod_user == codigo:
            acao = input("\nDigite o que deseja fazer: \n 1- EXCLUIR PRODUTO \n 2- CADASTRAR PRODUTO\n")
            if acao == "2":
                loja.cadastrar_produto()
            elif acao == "1":
                loja.excluir_produtos(indice_excluir = int(input("\nDigite o indice do produto á ser excluído: ")))
            elif cod_user != codigo:
                print("Código incorreto, tente novamente!\n")

        elif cod_user != codigo:
            print("O código digitado está errado. Tente novamente!\n")
            break

    elif escolha == 2:
        loja.carrinho()

    else:
        print ("Opção não encontrada. Tente novamente!\n")
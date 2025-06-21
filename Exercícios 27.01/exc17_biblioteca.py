class Biblioteca:
    def __init__(self):
        self.livros = {}  

    def cadastrar(self):
        nome = input("Nome do livro: ")
        if nome not in self.livros:
            self.livros[nome] = True
            print("Livro cadastrado!")
        else:
            print("Livro já cadastrado.")

    def emprestar(self):
        nome = input("Livro para emprestar: ")
        if nome in self.livros:
            if self.livros[nome]:
                self.livros[nome] = False
                print("Livro emprestado!")
            else:
                print("Livro já está emprestado.")
        else:
            print("Livro não encontrado.")

    def devolver(self):
        nome = input("Livro para devolver: ")
        if nome in self.livros:
            if not self.livros[nome]:
                self.livros[nome] = True
                print("Livro devolvido!")
            else:
                print("Livro já está disponível.")
        else:
            print("Livro não encontrado.")

    def verificar(self):
        nome = input("Livro para verificar: ")
        if nome in self.livros:
            if self.livros[nome]:
                print("Livro disponível.")
            else:
                print("Livro emprestado.")
        else:
            print("Livro não cadastrado.")

b = Biblioteca()
print("Seja bem vindo á biblioteca da Gigi 🦋")
while True:
    print("\nO que deseja realizar?")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Verificar livro")
    print("5 - Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
        b.cadastrar()
    elif escolha == "2":
        b.emprestar()
    elif escolha == "3":
        b.devolver()
    elif escolha == "4":
        b.verificar()
    elif escolha == "5":
        print("Te espero nas próximas aventuras!")
        break
    else:
        print("Opção inválida.")
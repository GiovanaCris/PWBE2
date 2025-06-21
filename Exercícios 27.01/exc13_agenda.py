class Agenda:
    def __init__(self):
        self.nome = {}     
        self.telefone = {} 

    def adicionar(self):
        i = len(self.nome) + 1
        print(">>>>>>>>>> ADICIONAR CONTATO <<<<<<<<<<")

        nome = input("Digite o nome da pessoa: ")
        self.nome[i] = nome

        numero = input("Digite o número de telefone: ") 
        self.telefone[i] = numero

        print("Contato adicionado com sucesso!")

    def editar(self, editar_contato):
        if editar_contato == 1:
            nome_procurado = input("Digite o nome do contato que deseja editar: ")
            for i, nome in self.nome.items():
                if nome == nome_procurado:
                    novo_nome = input("Digite o novo nome do contato: ")
                    self.nome[i] = novo_nome
                    print(f"Contato atualizado com sucesso: {nome_procurado} -> {novo_nome}")
                    return
            print("Contato não encontrado.")

        elif editar_contato == 2:
            numero_procurado = input("Digite o número do contato que deseja editar: ")
            for i, numero in self.telefone.items():
                if numero == numero_procurado:
                    novo_numero = input("Digite o novo número do contato: ")
                    self.telefone[i] = novo_numero
                    print(f"Telefone atualizado com sucesso: {numero_procurado} -> {novo_numero}")
                    return
            print("Telefone não encontrado.")

        elif editar_contato == 3:
            return

    def remover(self):
        nome_procurado = input("Digite o nome do contato que deseja remover: ")
        for i, nome in list(self.nome.items()):
            if nome == nome_procurado:
                del self.nome[i]
                del self.telefone[i]
                print(f"Contato {nome_procurado} removido com sucesso!")
                return
        print("Contato não encontrado!")

    def buscar(self):
        nome_buscar = input("Digite o nome do contato que deseja encontrar: ")
        for i, nome in self.nome.items():
            if nome == nome_buscar:
                print("Contato encontrado:")
                print("Nome:", nome)
                print("Telefone:", self.telefone[i])
                return
        print("Contato não encontrado.")

agenda = Agenda()

while True:
    escolha = int(input("\nO que deseja realizar? \n1- Adicionar \n2- Editar \n3- Remover \n4- Buscar contato\n5- Sair\n"))

    if escolha == 1:
        agenda.adicionar()

    elif escolha == 2:
        agenda.editar(editar_contato=int(input("\nO que deseja editar? \n1- Nome \n2- Telefone \n3- Cancelar\n")))

    elif escolha == 3:
        agenda.remover()

    elif escolha == 4:
        agenda.buscar()

    elif escolha == 5:
        print("Te espero na próxima 💫")
        break

    else:
        print("Opção inválida!")
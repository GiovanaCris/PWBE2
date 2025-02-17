class Agenda:
    def __init__(self):
        self.nome = {}
        self.telefone = {}

    def adicionar (self):
        i = len(self.nome) + 1
        print (">>>>>>>>>ADICIONAR CONTATOS<<<<<<<<")

        nome = input("Digite o nome da pessoa: ")
        self.nome[i] = nome

        numero = int(input("Digite o número de telefone: "))
        self.telefone[i] = numero

        print ("Contato adicionado com sucesso!")

    def editar (self, editar_contato):
        editar_contato = editar_contato
        if editar_contato == 1:
            i = input("Digite o nome do contato: ")

            if i in self.nome.values():
                novo_nome = input("Digite o novo nome do contato: ")
                self.nome[i] = novo_nome
                print (f"Contato {i} atualizado com sucesso para {novo_nome}! ")
            
        elif editar_contato == 2:
            numero = input("Digite o número do contato: ")
            if numero in self.telefone.values():
                novo_numero = input("Digite o novo número do contato: ")
                self.telefone[i] = novo_numero
                print (f"Contato {i} atualizado com sucesso para {novo_numero}! ")

        elif editar_contato == 3:
            return
        
    def remover (self):
        nome = input("Digite o nome do contato: ")

        if nome in self.nome.values():
            del self.nome[nome]
            print (f"Contato {nome} removido com êxito! ")

        elif nome not in self.nome.values():
            print ("Contato não encontrado! ")

    def buscar (self):
        nome_buscar = input("Digite o nome do contato que deseja encontrar: ")
        if nome_buscar in self.nome[nome_buscar]:
            print (self.nome)
            print (self.telefone[nome_buscar])

agenda = Agenda()

while True:
    escolha = int(input("\nO que deseja realizar? \n1- Adicionar \n2- Editar \n3- Remover \n4- Buscar contato\n"))
    if escolha == 1:
        agenda.adicionar()

    elif escolha == 2:
        agenda.editar(editar_contato=int(input("\nO que deseja editar \n1- Nome \n2- Telefone \n3- Não editar\n")))

    elif escolha == 3:
        agenda.remover()
        
    elif escolha == 4:
        agenda.buscar()
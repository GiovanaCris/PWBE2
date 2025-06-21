class RedeSocial:
    def __init__(self):
        self.usuarios = {}

    def cadastrar(self):
        nome = input("Digite seu nome: ")
        if nome not in self.usuarios:
            self.usuarios[nome] = {"amigos": [], "posts": []}
            print("Usuário cadastrado!")
        else:
            print("Esse nome já foi usado.")

    def adicionar_amigo(self):
        u1 = input("Quem vai adicionar o amigo? ")
        u2 = input("Nome do amigo: ")
        if u1 in self.usuarios and u2 in self.usuarios:
            if u2 not in self.usuarios[u1]["amigos"]:
                self.usuarios[u1]["amigos"].append(u2)
                self.usuarios[u2]["amigos"].append(u1)
                print("Amizade feita!")
            else:
                print("Já são amigos.")
        else:
            print("Um dos nomes não existe.")

    def postar(self):
        nome = input("Quem vai postar? ")
        if nome in self.usuarios:
            msg = input("Digite a mensagem: ")
            self.usuarios[nome]["posts"].append({"texto": msg, "comentarios": []})
            print("Post feito!")
        else:
            print("Usuário não existe.")

    def comentar(self):
        autor = input("Quem vai comentar? ")
        if autor not in self.usuarios:
            print("Usuário não existe.")
            return

        posts_disponiveis = []
        for usuario, dados in self.usuarios.items():
            for i, post in enumerate(dados["posts"]):
                print(f"{len(posts_disponiveis)} - {usuario}: {post['texto']}")
                posts_disponiveis.append((usuario, i)) 

        dono = input("De quem é o post? ")
        num = int(input("Digite o número do post para comentar: "))

        if 0 <= num < len(posts_disponiveis):
            dono, indice_post = posts_disponiveis[num]
            texto = input("Comentário: ")
            self.usuarios[dono]["posts"][indice_post]["comentarios"].append(f"{autor}: {texto}")
            print("Comentário adicionado!")
        else:
            print("Número inválido.")


        if dono in self.usuarios and 0 <= num < len(self.usuarios[dono]["posts"]):
            txt = input("Comentário: ")
            self.usuarios[dono]["posts"][num]["comentarios"].append(f"{autor}: {txt}")
            print("Comentado com sucesso!")
        else:
            print("Post inválido.")

    def buscar(self):
        nome = input("Digite o nome do usuário: ")
        if nome in self.usuarios:
            print("Amigos:", self.usuarios[nome]["amigos"])
            print("Posts:")
            for post in self.usuarios[nome]["posts"]:
                print(" -", post["texto"])
                for c in post["comentarios"]:
                    print("   💬", c)
        else:
            print("Usuário não encontrado.")

rede = RedeSocial()

print(">>>>>>>Bem vindo ao Ginsta<<<<<<")
while True:
    print("\nO que deseja realizar?")
    print("1 - Cadastrar")
    print("2 - Adicionar amigo")
    print("3 - Postar")
    print("4 - Comentar")
    print("5 - Buscar usuário")
    print("6 - Sair")
    op = input("Escolha: ")

    if op == "1":
        rede.cadastrar()
    elif op == "2":
        rede.adicionar_amigo()
    elif op == "3":
        rede.postar()
    elif op == "4":
        rede.comentar()
    elif op == "5":
        rede.buscar()
    elif op == "6":
        print("Que pena que já vai :/")
        break
    else:
        print("Opção inválida.")
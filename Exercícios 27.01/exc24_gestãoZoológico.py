print(">>>>>>Seja bem vindo ao PyZoo!! 🦁<<<<<<\n")
class Habitat:
    def __init__(self, tipo, temperatura, umidade):
        self.tipo = tipo
        self.temperatura = temperatura
        self.umidade = umidade

class Animal:
    def __init__(self, nome, especie, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta
        self.habitat = habitat
        self.saude = "Boa"
        self.localizacao = habitat.tipo

    def mover_para(self, novo_habitat):
        print(f"{self.nome} foi movido de {self.habitat.tipo} para {novo_habitat.tipo}")
        self.habitat = novo_habitat
        self.localizacao = novo_habitat.tipo

    def atualizar_saude(self, status):
        self.saude = status
        print(f"Saúde de {self.nome} atualizada para: {self.saude}")

class Alimentacao:
    def __init__(self, animal, comida, horario, quantidade):
        self.animal = animal
        self.comida = comida
        self.horario = horario
        self.quantidade = quantidade

    def registrar(self):
        print(f"{self.animal.nome} foi alimentado com {self.quantidade}g de {self.comida} às {self.horario}")

class Veterinario:
    def __init__(self, nome):
        self.nome = nome
        self.animais_responsaveis = []

    def adicionar_animal(self, animal):
        self.animais_responsaveis.append(animal)

    def verificar_animais(self):
        print(f"\n👨‍⚕️ Veterinário {self.nome} - Animais sob cuidado:")
        for animal in self.animais_responsaveis:
            print(f"- {animal.nome} ({animal.especie}) - Saúde: {animal.saude}")

class Funcionario:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

    def exibir(self):
        print(f"{self.nome} - Função: {self.funcao}")

# Habitats
savana = Habitat("Savana", "Quente", "Seca")
aquario = Habitat("Aquário", "Fria", "Alta")

# Animais
leao = Animal("Simba", "Leão", "Carnívoro", savana)
peixe = Animal("Nemo", "Peixe-palhaço", "Onívoro", aquario)

# Alimentação
refeicao1 = Alimentacao(leao, "Carne", "10h", 500)
refeicao2 = Alimentacao(peixe, "Ração", "12h", 50)

refeicao1.registrar()
refeicao2.registrar()

# Veterinário
vet = Veterinario("Dra. Paula")
vet.adicionar_animal(leao)
vet.adicionar_animal(peixe)
vet.verificar_animais()

# Atualizar saúde e mover animal
leao.atualizar_saude("Machucado")
leao.mover_para(aquario)

# Funcionário
func = Funcionario("João", "Cuidador")
func.exibir()

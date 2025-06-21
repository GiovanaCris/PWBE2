import random

class Personagem:
    def __init__(self, nome, saude, forca, defesa):
        self.nome = nome
        self.saude = saude
        self.saude_max = saude
        self.forca = forca
        self.defesa = defesa
        self.nivel = 1
        self.xp = 0
        self.pocoes = 3

    def atacar(self, inimigo):
        dano = max(0, self.forca - inimigo.defesa + random.randint(-2, 2))
        inimigo.saude -= dano
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")

    def habilidade_especial(self, inimigo):
        dano = (self.forca * 2) - inimigo.defesa
        inimigo.saude -= dano
        print(f"{self.nome} usou habilidade especial! Dano: {dano}")

    def usar_pocao(self):
        if self.pocoes > 0:
            cura = 20
            self.saude = min(self.saude + cura, self.saude_max)
            self.pocoes -= 1
            print(f"{self.nome} usou uma poção e recuperou {cura} de vida! ({self.pocoes} restantes)")
        else:
            print("⚠️ Sem poções disponíveis!")

    def ganhar_xp(self, valor):
        self.xp += valor
        print(f"{self.nome} ganhou {valor} XP!")
        if self.xp >= 50:
            self.evoluir()

    def evoluir(self):
        self.nivel += 1
        self.xp = 0
        self.forca += 3
        self.defesa += 2
        self.saude_max += 10
        self.saude = self.saude_max
        print(f"🎉 {self.nome} subiu para o nível {self.nivel}!")

    def esta_vivo(self):
        return self.saude > 0

    def status(self):
        print(f"\n{self.nome} | Vida: {self.saude}/{self.saude_max} | Nível: {self.nivel} | XP: {self.xp} | Poções: {self.pocoes}")


heroi = Personagem("Gi", saude=100, forca=15, defesa=5)
inimigo = Personagem("Orc", saude=80, forca=10, defesa=3)

print("⚔️ Início do combate!")

while heroi.esta_vivo() and inimigo.esta_vivo():
    heroi.status()
    inimigo.status()

    print("\nEscolha uma ação:")
    print("1 - Atacar")
    print("2 - Habilidade especial")
    print("3 - Usar poção")

    acao = input("> ")

    if acao == "1":
        heroi.atacar(inimigo)
    elif acao == "2":
        heroi.habilidade_especial(inimigo)
    elif acao == "3":
        heroi.usar_pocao()
    else:
        print("❌ Ação inválida.")
        continue

    if inimigo.esta_vivo():
        inimigo.atacar(heroi)

if heroi.esta_vivo():
    print("\n🏆 Você venceu o combate!")
    heroi.ganhar_xp(50)
else:
    print("\n💀 Você foi derrotado...")

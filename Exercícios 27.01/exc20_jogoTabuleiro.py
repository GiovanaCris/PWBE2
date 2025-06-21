class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [["." for _ in range(4)] for _ in range(4)]
        self.pecas = {
            "P": (3, 0),  # Peão na posição (3,0)
            "T": (0, 0)   # Torre na posição (0,0)
        }
        self.atualizar_tabuleiro()

    def atualizar_tabuleiro(self):
        self.tabuleiro = [["." for _ in range(4)] for _ in range(4)]
        for nome, pos in self.pecas.items():
            l, c = pos
            self.tabuleiro[l][c] = nome

    def mostrar(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))

    def mover(self, nome, nova_linha, nova_coluna):
        if nome not in self.pecas:
            print("Peça não existe.")
            return

        linha_atual, coluna_atual = self.pecas[nome]

        if nome == "P":  # Peão: só anda 1 pra cima
            if nova_linha == linha_atual - 1 and nova_coluna == coluna_atual:
                self.pecas[nome] = (nova_linha, nova_coluna)
                print("Peão movido!")
            else:
                print("Movimento inválido para o Peão.")
        elif nome == "T":  # Torre: anda em linha reta
            if nova_linha == linha_atual or nova_coluna == coluna_atual:
                self.pecas[nome] = (nova_linha, nova_coluna)
                print("Torre movida!")
            else:
                print("Movimento inválido para a Torre.")

        self.atualizar_tabuleiro()

jogo = Tabuleiro()
print("Seja bem vindo ao tabuleiro da Gigi💜")
while True:
    jogo.mostrar()
    peca = input("Qual peça quer mover? (P ou T): ").upper()
    linha = int(input("Nova linha (0 a 3): "))
    coluna = int(input("Nova coluna (0 a 3): "))
    jogo.mover(peca, linha, coluna)

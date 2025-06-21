import random
from colorama import Fore, Style, init
init(autoreset=True)  # Inicializa colorama e reseta automaticamente

class JogoCartas:
    def __init__(self):
        self.cartas_azul = ["0 AZUL", "1 AZUL", "2 AZUL", "3 AZUL", "4 AZUL", "5 AZUL", "6 AZUL", "7 AZUL", "8 AZUL", "9 AZUL", "+2 AZUL", "BLOQUEIO AZUL", "REVERSE AZUL"]
        self.cartas_amarela = ["0 AMARELO", "1 AMARELO", "2 AMARELO", "3 AMARELO", "4 AMARELO", "5 AMARELO", "6 AMARELO", "7 AMARELO", "8 AMARELO", "9 AMARELO", "+2 AMARELO", "BLOQUEIO AMARELO", "REVERSE AMARELO"]
        self.cartas_verde = ["0 VERDE", "1 VERDE", "2 VERDE", "3 VERDE", "4 VERDE", "5 VERDE", "6 VERDE", "7 VERDE", "8 VERDE", "9 VERDE", "+2 VERDE", "BLOQUEIO VERDE", "REVERSE VERDE"]
        self.cartas_vermelha = ["0 VERMELHO", "1 VERMELHO", "2 VERMELHO", "3 VERMELHO", "4 VERMELHO", "5 VERMELHO", "6 VERMELHO", "7 VERMELHO", "8 VERMELHO", "9 VERMELHO", "+2 VERMELHO", "BLOQUEIO VERMELHO", "REVERSE VERMELHO"]
        self.cartas_especiais = ["+4 PRETO", "ESCOLHA COR"]

        self.todas_cartas = self.cartas_azul + self.cartas_amarela + self.cartas_verde + self.cartas_vermelha + self.cartas_especiais

    def embaralhar(self):
        random.shuffle(self.todas_cartas)

    def carta_valida(self, carta_jogada, carta_mesa):
        cor_jogada = carta_jogada.split()[-1]
        valor_jogado = carta_jogada.split()[0]

        cor_mesa = carta_mesa.split()[-1]
        valor_mesa = carta_mesa.split()[0]

        return cor_jogada == cor_mesa or valor_jogado == valor_mesa or "PRETO" in carta_jogada or "ESCOLHA" in carta_jogada

    def jogadas(self):
        self.embaralhar()

        jogador1 = input("Qual é o nome do jogador 1? ")
        cartas1 = self.todas_cartas[:5]

        jogador2 = input("Qual é o nome do jogador 2? ")
        cartas2 = self.todas_cartas[5:10]

        carta_na_mesa = self.todas_cartas[10]
        baralho_restante = self.todas_cartas[11:]

        print(f"\n>>> Carta inicial na mesa: {carta_na_mesa}")

        vez = 1
        while True:
            if vez % 2 != 0:
                jogador_atual = jogador1
                cartas_atual = cartas1
            else:
                jogador_atual = jogador2
                cartas_atual = cartas2

            print(f"\nÉ a vez de {jogador_atual}")
            print(f"Suas cartas: {cartas_atual}")
            print(f"Carta na mesa: {carta_na_mesa}")
            jogada = input("Digite a carta que deseja jogar, 'comprar' para pegar 1 carta ou 'passar': ").strip().upper()

            if jogada == "PASSAR":
                print(f"{jogador_atual} passou a vez.")
            elif jogada == "COMPRAR":
                if baralho_restante:
                    nova_carta = baralho_restante.pop(0)
                    cartas_atual.append(nova_carta)
                    print(f"{jogador_atual} comprou uma carta: {nova_carta}")
                else:
                    print("⚠️ O baralho acabou! Não há mais cartas para comprar.")
            elif jogada in cartas_atual:
                if self.carta_valida(jogada, carta_na_mesa):
                    cartas_atual.remove(jogada)
                    carta_na_mesa = jogada
                    print(f"{jogador_atual} jogou: {jogada}")
                else:
                    print("Essa carta não pode ser jogada. Perdeu a vez.")
            else:
                print("Entrada inválida. Tente novamente.")
                continue  # repete a vez

            if len(cartas_atual) == 0:
                print(f"\n🎉 Parabéns {jogador_atual}, você venceu o jogo!")
                break

            vez += 1

jogocartas = JogoCartas()
print(
    f"🎮 Bem-vindo ao PyUno!\n"
    f"Passe o celular para o próximo jogador após jogar.\n"
    f"{Fore.RED}Olhar as cartas do adversário é proibido, tô de olho einn 👀{Style.RESET_ALL}"
)
jogocartas.jogadas()
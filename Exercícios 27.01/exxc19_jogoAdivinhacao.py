import random
from colorama import Fore, Style, init
init(autoreset=True)  

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)

    def jogar(self):
        print(f"🎲 Bem-vindo ao GiSort!\n{Fore.MAGENTA}Aqui seu maior aliado é a sorte!{Style.RESET_ALL}")
        tentativas = 0

        while True:
            palpite = int(input("\nDigite seu palpite (1 a 100): "))
            tentativas += 1

            if palpite < self.numero_secreto:
                print("🔽 Muito baixo. Tente um número maior.")
            elif palpite > self.numero_secreto:
                print("🔼 Muito alto. Tente um número menor.")
            else:
                print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
                break

jogo = JogoAdivinhacao()
jogo.jogar()

import calendar #Biblioteca para formato de calendário
from datetime import datetime

class Calendario:
    def __init__(self):
        # Lista de feriados do PyCalender
        self.feriados = {
            "01/01": "Ano Novo",
            "07/09": "Independência do Brasil",
            "12/10": "Nossa Senhora Aparecida",
            "25/12": "Natal"
        }

    def exibir_mes(self):
        ano = int(input("Digite o ano: "))
        mes = int(input("Digite o mês (1 a 12): "))
        print("\n" + calendar.month(ano, mes))

    def verificar_feriado(self):
        data = input("Digite a data (dd/mm): ")
        if data in self.feriados:
            print(f"🎉 {data} é feriado: {self.feriados[data]}")
        else:
            print(f"{data} não é um feriado cadastrado no PyCalendar.")

    def diferenca_dias(self):
        d1 = input("Digite a primeira data (dd/mm/aaaa): ")
        d2 = input("Digite a segunda data (dd/mm/aaaa): ")

        try:
            data1 = datetime.strptime(d1, "%d/%m/%Y")
            data2 = datetime.strptime(d2, "%d/%m/%Y")
            diff = abs((data2 - data1).days)
            print(f"A diferença é de {diff} dias.")
        except ValueError:
            print("⚠️ Formato de data inválido.")

cal = Calendario()

print("Bem vindooo ao PyCalendar!📅")
while True:
    print("\nO que deseja realizar?")
    print("1 - Exibir mês")
    print("2 - Verificar feriado")
    print("3 - Diferença entre datas")
    print("4 - Sair")
    op = input("Escolha: ")

    if op == "1":
        cal.exibir_mes()
    elif op == "2":
        cal.verificar_feriado()
    elif op == "3":
        cal.diferenca_dias()
    elif op == "4":
        print("Bye bye usuárioo")
        break
    else:
        print("Opção inválida.")
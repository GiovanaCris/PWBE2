from datetime import datetime

class Evento:
    def __init__(self, nome, tipo, data, hora, local, descricao):
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.hora = hora
        self.local = local
        self.descricao = descricao
        self.tarefas = []
        self.fornecedores = []
        self.pagamentos = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.append(pagamento)

    def exibir_resumo(self):
        print(f"\n📅 Evento: {self.nome} ({self.tipo})")
        print(f"📍 Data: {self.data} às {self.hora} | Local: {self.local}")
        print(f"ℹ️ Descrição: {self.descricao}")
        print(f"✅ Tarefas: {len(self.tarefas)} | 🧾 Fornecedores: {len(self.fornecedores)} | 💵 Pagamentos: {len(self.pagamentos)}")

class Tarefa:
    def __init__(self, nome, responsavel, prazo):
        self.nome = nome
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def verificar_atraso(self):
        if self.status == "Pendente":
            prazo_data = datetime.strptime(self.prazo, "%d/%m/%Y")
            if prazo_data < datetime.today():
                self.status = "Atrasada"

class Fornecedor:
    def __init__(self, nome, servico):
        self.nome = nome
        self.servico = servico

class Pagamento:
    def __init__(self, valor_total, vencimento, descricao):
        self.valor_total = valor_total
        self.vencimento = vencimento
        self.descricao = descricao
        self.pago = False

    def registrar_pagamento(self):
        self.pago = True


eventos = []

def listar_eventos():
    if not eventos:
        print("⚠️ Nenhum evento cadastrado.")
        return
    for i, evento in enumerate(eventos):
        print(f"\n[{i}] {evento.nome} - {evento.tipo}")
        evento.exibir_resumo()

def selecionar_evento():
    if not eventos:
        print("⚠️ Nenhum evento disponível.")
        return None
    listar_eventos()
    try:
        idx = int(input("Digite o número do evento: "))
        if 0 <= idx < len(eventos):
            return idx
        else:
            print("❌ Índice inválido.")
            return None
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
        return None

def criar_evento():
    print("\n--- Criar novo evento ---")
    nome = input("Nome do evento: ")
    tipo = input("Tipo do evento (Casamento, Festa, Corporativo): ")
    data = input("Data (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    local = input("Local: ")
    descricao = input("Descrição: ")
    e = Evento(nome, tipo, data, hora, local, descricao)
    eventos.append(e)
    print("✅ Evento criado com sucesso!")

def adicionar_tarefa():
    idx = selecionar_evento()
    if idx is None:
        return
    nome = input("Nome da tarefa: ")
    responsavel = input("Responsável: ")
    prazo = input("Prazo (DD/MM/AAAA): ")
    t = Tarefa(nome, responsavel, prazo)
    eventos[idx].adicionar_tarefa(t)
    print("📝 Tarefa adicionada.")

def adicionar_fornecedor():
    idx = selecionar_evento()
    if idx is None:
        return
    nome = input("Nome do fornecedor: ")
    servico = input("Serviço prestado: ")
    f = Fornecedor(nome, servico)
    eventos[idx].adicionar_fornecedor(f)
    print("🤝 Fornecedor associado.")

def adicionar_pagamento():
    idx = selecionar_evento()
    if idx is None:
        return
    try:
        valor = float(input("Valor do pagamento: R$ "))
    except ValueError:
        print("❌ Valor inválido.")
        return
    vencimento = input("Data de vencimento (DD/MM/AAAA): ")
    descricao = input("Descrição do pagamento: ")
    p = Pagamento(valor, vencimento, descricao)
    eventos[idx].adicionar_pagamento(p)
    print("💵 Pagamento registrado.")

def marcar_tarefa_concluida():
    idx = selecionar_evento()
    if idx is None:
        return
    if not eventos[idx].tarefas:
        print("⚠️ Nenhuma tarefa para este evento.")
        return
    print("\nTarefas:")
    for i, t in enumerate(eventos[idx].tarefas):
        print(f"[{i}] {t.nome} - Status: {t.status}")
    try:
        idt = int(input("Qual tarefa deseja concluir? "))
        if 0 <= idt < len(eventos[idx].tarefas):
            eventos[idx].tarefas[idt].concluir()
            print("✅ Tarefa marcada como concluída.")
        else:
            print("❌ Índice de tarefa inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

def marcar_pagamento_pago():
    idx = selecionar_evento()
    if idx is None:
        return
    if not eventos[idx].pagamentos:
        print("⚠️ Nenhum pagamento para este evento.")
        return
    print("\nPagamentos:")
    for i, p in enumerate(eventos[idx].pagamentos):
        status = "Pago" if p.pago else "Pendente"
        print(f"[{i}] {p.descricao} - R${p.valor_total} - {status}")
    try:
        idp = int(input("Qual pagamento deseja marcar como pago? "))
        if 0 <= idp < len(eventos[idx].pagamentos):
            eventos[idx].pagamentos[idp].registrar_pagamento()
            print("✅ Pagamento confirmado.")
        else:
            print("❌ Índice de pagamento inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

# Menu principal
print("Seja bem-vindo ao GitarefasPy")
while True:
    print("\nO que deseja realizar?")
    print("1 - Criar evento")
    print("2 - Ver eventos")
    print("3 - Adicionar tarefa")
    print("4 - Adicionar fornecedor")
    print("5 - Adicionar pagamento")
    print("6 - Concluir tarefa")
    print("7 - Confirmar pagamento")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_evento()
    elif opcao == "2":
        listar_eventos()
    elif opcao == "3":
        adicionar_tarefa()
    elif opcao == "4":
        adicionar_fornecedor()
    elif opcao == "5":
        adicionar_pagamento()
    elif opcao == "6":
        marcar_tarefa_concluida()
    elif opcao == "7":
        marcar_pagamento_pago()
    elif opcao == "8":
        print("Bye bye te espero na próxima usuáriooo 👋")
        break
    else:
        print("❌ Opção inválida.")
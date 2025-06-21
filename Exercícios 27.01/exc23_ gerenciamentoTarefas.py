class Tarefa:
    def __init__(self, titulo, categoria, prioridade, vencimento):
        self.titulo = titulo
        self.categoria = categoria
        self.prioridade = prioridade
        self.vencimento = vencimento
        self.status = "Pendente"

    def mostrar(self):
        print(f"\n📌 {self.titulo}")
        print(f"Categoria: {self.categoria}")
        print(f"Prioridade: {self.prioridade}")
        print(f"Vencimento: {self.vencimento}")
        print(f"Status: {self.status}")

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def criar_tarefa(self):
        titulo = input("Título da tarefa: ")
        categoria = input("Categoria: ")
        prioridade = input("Prioridade (Alta, Média, Baixa): ")
        vencimento = input("Data de vencimento (DD/MM/AAAA): ")
        self.tarefas.append(Tarefa(titulo, categoria, prioridade, vencimento))
        print("✅ Tarefa criada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("🚫 Nenhuma tarefa cadastrada.")
            return
        for i, tarefa in enumerate(self.tarefas):
            print(f"\nTarefa {i+1}:")
            tarefa.mostrar()

    def editar_tarefa(self):
        self.listar_tarefas()
        i = int(input("Digite o número da tarefa que deseja editar: ")) - 1
        if 0 <= i < len(self.tarefas):
            t = self.tarefas[i]
            print("Deixe vazio se não quiser alterar:")
            novo_titulo = input("Novo título: ")
            nova_categoria = input("Nova categoria: ")
            nova_prioridade = input("Nova prioridade: ")
            novo_vencimento = input("Nova data de vencimento: ")
            novo_status = input("Novo status (Pendente, Em andamento, Concluída): ")

            if novo_titulo: t.titulo = novo_titulo
            if nova_categoria: t.categoria = nova_categoria
            if nova_prioridade: t.prioridade = nova_prioridade
            if novo_vencimento: t.vencimento = novo_vencimento
            if novo_status: t.status = novo_status
            print("✅ Tarefa atualizada.")
        else:
            print("❌ Número inválido.")

    def excluir_tarefa(self):
        self.listar_tarefas()
        i = int(input("Número da tarefa para excluir: ")) - 1
        if 0 <= i < len(self.tarefas):
            del self.tarefas[i]
            print("🗑️ Tarefa excluída.")
        else:
            print("❌ Número inválido.")

    def filtrar(self):
        print("\n1 - Filtrar por status\n2 - Filtrar por prioridade")
        opc = input("Escolha: ")
        if opc == "1":
            status = input("Digite o status (Pendente, Em andamento, Concluída): ")
            for t in self.tarefas:
                if t.status.lower() == status.lower():
                    t.mostrar()
        elif opc == "2":
            prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
            for t in self.tarefas:
                if t.prioridade.lower() == prioridade.lower():
                    t.mostrar()
        else:
            print("❌ Opção inválida.")

sistema = GerenciadorDeTarefas()
print(">>>>>Seja bem vindo ao PyGeren<<<<<")
while True:
    print("\nO que deseja realizar?")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Filtrar tarefas")
    print("6 - Sair")

    opc = input("Escolha: ")

    if opc == "1":
        sistema.criar_tarefa()
    elif opc == "2":
        sistema.listar_tarefas()
    elif opc == "3":
        sistema.editar_tarefa()
    elif opc == "4":
        sistema.excluir_tarefa()
    elif opc == "5":
        sistema.filtrar()
    elif opc == "6":
        print("Lhe espero na próximaa")
        break
    else:
        print("❌ Opção inválida.")
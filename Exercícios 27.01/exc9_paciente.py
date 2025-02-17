while True:
    class Paciente:
            def __init__(self, nome, idade, historico):
                self.nome = nome
                self.idade = idade
                self.historico = historico
                self.adc_consulta = 0
                
            def adicionar(self):
                decisao = input(f"{self.nome} Deseja adicionar uma consulta ao seu histórico?(s/n) ")
                if decisao == "s":
                    print ("Consulta adicionada com sucesso! ")
                    self.adc_consulta += 1
                elif decisao == "n":
                    print ("Consulta não agendada!")
                    
            def consultas(self):
                self.historico += self.adc_consulta
                self.adc_consulta = 0
                print (f"Consultas realizadas: {self.historico}")
            
    paciente = Paciente("Maria", "40", 1)
    paciente.adicionar()
    paciente.consultas()
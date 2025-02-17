class Aluno:
    def __init__ (self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def media(self):
        n1 = float(input("Me passe uma nota: "))    
        n2 = float(input("Me passe uma nota: "))    
        n3 = float(input("Me passe uma nota: "))
        media = (n1 + n2 + n3) / 3 
        if media >= 6:
            print(f"{self.nome}, média {media} Foi aprovado")
        elif media < 6:
            print (f"{self.nome}, média {media} Reprovado")
            
media_al = Aluno("Nicolas", "13564")
media_al.media()
               
        
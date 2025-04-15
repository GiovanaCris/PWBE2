while True: 
    class Livro:
        def __init__(self, titulo, autor, paginas):
            self.titulo = titulo
            self.autor = autor
            self.paginas = paginas
            
        def emprestar(self):
            emprest = input("\nDeseja emprestar o livro? (s/n) ")
            if emprest == "s":
                nome_empres = input("Digite o nome da pessoa que irá receber o livro: ")
                print (f"Livro emprestado com sucesso para {nome_empres}!")
                
            elif emprest == "n":
                print ("Livro não emprestado!")
            
        def devolver(self):
            devol = input("\nDeseja devolver o livro? (s/n) ")
            if devol == "s":
                nome_dev = input("Digite o nome do livro para realizar a devolução: ")
                print (f"{nome_dev}, foi devolvido com sucesso!")
                
            elif devol == "n":
                print ("Devolução não concretizada!")
            
        def disponivel(self):
            nome_livro = input("\nDigite o nome do livro que deseja: ")
            if nome_livro == self.titulo:
                print ("Livro disponível! ")
            else:
                print ("Livro indisponível!")
                
    livro = Livro(titulo = input("\nDigite o nome do livro: "), autor = input("Digite o autor: "), paginas = int(input("Digite a quantidade de páginas: ")))
    livro.emprestar()
    livro.devolver()
    livro.disponivel()
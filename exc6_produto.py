class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def prod_estoque(self):
        val_estoque = self.estoque + self.preco
        print (f"O valor total em estoque do {self.nome} que custa {self.preco} reais é {val_estoque}")
        
produto = Produto("Arroz", 20, 10)
produto.prod_estoque()
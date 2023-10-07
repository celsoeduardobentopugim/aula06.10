class livro:
    def __init__(self, titulo, autor, ano_publicaçao):
        self.titulo=titulo
        self.autor=autor 
        self.ano_publicaçao = ano_publicaçao

    def descricao (self):
        print(f" titulo: {self.titulo} o autor {self.autor} ano de publicação: {self.ano_publicaçao}")

        
livro1= livro("terror","celso eduardo","2023")

print(livro1.titulo)
print(livro1.autor)
print(livro1.ano_publicaçao)

livro1.descricao()







class estudante:
    def __init__(self,nome, idade):
        self.nome=nome
        self.idade=idade


    def apresentar(self):
        print(f"nome é {self.nome} e idade é {self.idade}")


aluno= estudante("celso eduardo",22)

print(aluno.nome)
print(aluno.idade)


aluno.apresentar()
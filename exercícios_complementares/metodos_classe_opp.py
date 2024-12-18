class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Sua profissão é {self.profissao}!'
    
pessoa = Pessoa('Gustavo', 37, 'Dev')
print(pessoa)

pessoa.aniversario()
print(pessoa)

print(pessoa.saudacao)
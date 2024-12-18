# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

carro = Carro('GLC', 'Azul Escuro', 2023)
print(carro)

# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
# Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, unidades, dono):
        self.nome = nome
        self.categoria = categoria
        self.status = False
        self.unidades = unidades
        self.dono = dono

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status} | {self.unidades} | {self.dono}'
    
restaurante = Restaurante('Luigia', 'Italiano', 4, 'Giuseppe')
print(restaurante)

# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
# e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

restaurante2 = Restaurante('Taypa', 'Peruano', 1, 'Pedro')
print(restaurante2)

# 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
# seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

print(restaurante2)

# 5 - Crie uma classe chamada Cliente e pense em 4 atributos.
# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, cpf, endereco, fidelidade):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.fidelidade= fidelidade

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.endereco} | {self.fidelidade}'

cliente_1 = Cliente(
    nome="João Silva",
    cpf="123.456.789-00",
    endereco="Rua das Flores, 123 - São Paulo, SP",
    fidelidade=1200
)

cliente_2 = Cliente(
    nome="Maria Oliveira",
    cpf="987.654.321-11",
    endereco="Avenida Brasil, 456 - Rio de Janeiro, RJ",
    fidelidade=850
)

cliente_3 = Cliente(
    nome="Carlos Santos",
    cpf="456.789.123-22",
    endereco="Praça da Liberdade, 789 - Belo Horizonte, MG",
    fidelidade=200
)

print(cliente_1)
print(cliente_2)
print(cliente_3)
# 1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os
# parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular da conta: {self.titular} | Saldo da conta: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls):
        cls._ativo = True
        print(f'{cls._ativo}')

# 2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna
# uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

conta_1 = ContaBancaria('Gustavo', 200)
conta_2 = ContaBancaria('Bartô', 100)

print(conta_1)
print(conta_2)

# 3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define
# o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

conta_3 = ContaBancaria('Mari', 300)
print(conta_3)
conta_3.ativar_conta()

# 4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação
# de atributos. Utilize propriedades, se necessário.

class PythonicContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
# 5 - Crie uma instância da classe e imprima o valor da propriedade titular.

conta_4 = PythonicContaBancaria('Gustavo', 400)
print(conta_4.titular)

# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    clientes = []

    def __init__(self, titular, conta, agencia, saldo, endereco):
        self._titular = titular
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo
        self._endereco = endereco
        ClienteBanco.clientes.append(self)

    @classmethod
    def listar_contas(cls):
        for cliente in cls.clientes:
            print(f'{cliente._titular} | {cliente._conta} | {cliente._agencia}')
        
cliente1 = ClienteBanco("Ana Beatriz Costa", "12345-6", "001", 1500.75, "Rua dos Pinheiros, 45 - São Paulo, SP")
cliente2 = ClienteBanco("Carlos Eduardo Alves", "67890-2", "002", 3250.40, "Avenida Paulista, 1000 - São Paulo, SP")
cliente3 = ClienteBanco("Fernanda Oliveira", "54321-9", "003", 870.15, "Praça da República, 78 - Rio de Janeiro, RJ")


# 7 - Crie um método de classe para a conta ClienteBanco.

ClienteBanco.listar_contas()


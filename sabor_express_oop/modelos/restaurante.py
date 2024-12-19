from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = [] # a ideia é não manipular as informações de avaliação assim que a classe Restaurantes for instanciada
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status}'
    
    @classmethod
    def listar_restaurantes(cls): # indica que é um método da classe. não precisa acessar atributo
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.status}')

    @property
    def status(self):
        return 'Ativado' if self._status else 'Desativado'
    
    def alternar_status(self): # método para os objetos
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return f'Não avaliado'
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtde_notas = len(self._avaliacao)
        media = round(soma_notas / qtde_notas, 1)
        return media


# função dir() - atributos, métodos, tudo relacionado a classes
# função vars() - visualizar um dicionário dos atributos e métodos relacionados ao objeto instanciado da classe

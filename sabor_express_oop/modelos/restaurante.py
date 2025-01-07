from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = [] # a ideia é não manipular as informações de avaliação assim que a classe Restaurantes for instanciada
        self._cardapio = []
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

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): # valida se o item a ser adicionado é uma instância de ItemCardapio, ou seja, não importa qual item, desde que ele seja uma instância
            self._cardapio.append(item)

    @property # o valor desse método que é uma property será usado apenas para leitura e não manipulação, por isso a escolha de property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'): # verifica se o atributo está presente no item. se sim, imprime o item com o atributo definido no parâmetro
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}\n'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}\n'
                print(mensagem_bebida)

# função dir() - atributos, métodos, tudo relacionado a classes
# função vars() - visualizar um dicionário dos atributos e métodos relacionados ao objeto instanciado da classe

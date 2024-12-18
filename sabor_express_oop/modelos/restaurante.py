class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status}'
    
    @classmethod
    def listar_restaurantes(cls): # indica que é um método da classe. não precisa acessar atributo
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.status}')

    @property
    def status(self):
        return 'Ativado' if self._status else 'Desativado'
    
    def alternar_status(self): # método para os objetos
        self._status = not self._status


# função dir() - atributos, métodos, tudo relacionado a classes
# função vars() - visualizar um dicionário dos atributos e métodos relacionados ao objeto instanciado da classe

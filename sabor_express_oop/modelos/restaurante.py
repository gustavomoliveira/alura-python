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

restaurante_praca = Restaurante('Praça', 'Gourmet')
#print(restaurante_praca)
#print(dir(restaurante_praca)) # função dir() - atributos, métodos, tudo relacionado a classes
#print(vars(restaurante_praca)) # função vars() - visualizar um dicionário dos atributos e métodos relacionados ao objeto instanciado da classe

restaurante_praca.alternar_status()

restaurante_pizza_express = Restaurante('Pizza Express', 'Italiano')
#print(vars(restaurante_pizza_express))

#print(restaurante_pizza_express) # o print agora usa o método __str__
#print(restaurante_praca)



Restaurante.listar_restaurantes()

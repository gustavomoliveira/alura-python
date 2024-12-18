# 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

class Restaurante:
    def __init__(self, nome, categoria, status):
        self.nome = nome
        self.categoria = categoria
        self.status = status

restaurante_praca = Restaurante('Praça', 'Italiana', True)
print(restaurante_praca.categoria)

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

print(restaurante_praca.nome)

# 3 - Verifique o valor inicial do atributo ativo para a instância
# restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

mensagem = 'Ativo' if restaurante_praca.status == True else 'Desativado'
print(mensagem)

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

#categoria = Restaurante.categoria # sem a estrutura de construtor montada

# 5 - Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = Restaurante('Pizza Place', 'Fast Food', False)
print(restaurante_pizza)

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

print(restaurante_pizza.categoria)

# 8 - Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.status = True
print(restaurante_pizza.status)

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'Nome: {restaurante_pizza.nome}, Categoria: {restaurante_pizza.categoria}')
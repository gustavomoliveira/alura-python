# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome': 'Gustavo', 'idade': 37, 'cidade': 'Genebra'}

print(pessoa)

""" 2 -  Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário. """

pessoa['idade'] = 36
print(pessoa['idade'])

pessoa['profissão'] = 'Engenheiro de Software'
print(pessoa)

pessoa.pop('idade')
print(pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

quadrados_numeros = {
    '1': 1,
    '2': 4,
    '3': 9,
    '4': 16,
    '5': 25
}

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

print(quadrados_numeros['4'])

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = 'Essa é a frase de teste para o programa em Python que conta palavras em uma frase'
palavras = frase.split()
palavras_dic = {}

for palavra in palavras:
    palavras_dic[palavra] = palavras_dic.get(palavra, 0) + 1

print(palavras_dic)
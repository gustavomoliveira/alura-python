# 7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto.
# Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

# 9 - Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

from carro import Carro
from moto import Moto

carro_1 = Carro('Mercedes Benz', 'GLC', 4)
carro_2 = Carro('BMW', 'X5', 4)
carro_3 = Carro('Mercedes Benz', 'G Class AMG 63', 4)
moto_1 = Moto('Honda', '1000r', 'Esportiva')
moto_2 = Moto('BMW', 'R1300 Gs', 'Esportiva')
moto_3 = Moto('BMW', 'Roadster', 'Esportiva')

def main():
    print(carro_1)
    print(carro_2)
    print(carro_3)
    print(moto_1)
    print(moto_2)
    print(moto_3)

if __name__ == '__main__':
    main() 
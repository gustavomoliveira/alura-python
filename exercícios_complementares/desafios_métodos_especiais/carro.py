from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        return f'{self._marca.ljust(15)} | {self._modelo.ljust(15)} | {self.cor.ljust(15)}'

    def ligar(self):
        print(f'O carro {self._modelo} está ligado.')
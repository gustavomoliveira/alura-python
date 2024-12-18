from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonês')

restaurante_mexicano.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
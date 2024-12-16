import os

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            return opcao
        except ValueError:
            print('\nERRO: Digite um número inteiro entre 1 e 4.')

def validar_categoria(msg):
    while True:
        try:
            categoria = input(msg)
            if all(caracter.isalpha() or caracter.isspace() for caracter in categoria):
                return categoria
        except ValueError:
            print('ERRO: Digite uma categoria válida.')

def exibir_subtitulo(msg):
    os.system('clear')
    linha = '=' * len(msg)
    print(linha)
    print(msg)
    print(linha)
    print()
        
def menu():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
''')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Status')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('App finalizado')

def cadastrar_restaurante(restaurantes):
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ').title()
    categoria = validar_categoria('Digite a categoria do restaurante: ').title()
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!')
    return restaurantes

def listar_restaurantes(restaurantes):
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do Restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | Status')
    for i, restaurante in enumerate(restaurantes, start=1):
        status = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'\n{i} - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {status}')

def alternar_estado(restaurantes):
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ').title().strip()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'{nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'{nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

def app():
    restaurantes = []
    while True:
        menu()
        opcao = validar_opcao('\nEscolha uma opção do menu (1 - 4): ')

        match opcao:
            case 1:
                restaurantes = cadastrar_restaurante(restaurantes)
            case 2:
                listar_restaurantes(restaurantes)
            case 3:
                alternar_estado(restaurantes)
            case 4:
                finalizar_app()
                break
            case _:
                print('Digite uma opção válida.')
app()

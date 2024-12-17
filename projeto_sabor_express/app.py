import os

def validar_opcao(msg):
    """ Valida que a opção digitada pelo usuário seja um número inteiro entre 1 e 4
    
    Input:
    - texto: str - A opção escolhida pelo usuário

    Output:
    - número: int - A opção convertida pala número inteiro e validada 
    """
    while True:
        try:
            opcao = int(input(msg))
            return opcao
        except ValueError:
            print('\nERRO: Digite um número inteiro entre 1 e 4.')

def validar_categoria(msg):
    """ Valida que a categoria digitada pelo usuário contenha apenas letras e espaços
    
    Input:
    - texto: str - A categoria digitada pelo usuário

    Output:
    - texto: str - A categoria validada
    """
    while True:
        try:
            categoria = input(msg)
            if all(caracter.isalpha() or caracter.isspace() for caracter in categoria):
                return categoria
        except ValueError:
            print('ERRO: Digite uma categoria válida.')

def exibir_subtitulo(msg):
    """ Exibe um subtítulo estilizado
    
    Inputs:
    - texto: str - O texto do subtítulo
    """
    os.system('clear')
    linha = '=' * len(msg)
    print(linha)
    print(msg)
    print(linha)
    print()
        
def menu():
    """ Exibe o menu e suas opções """
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
    """ Exibe mensagem de encerramento do programa  """
    exibir_subtitulo('App finalizado')

def cadastrar_restaurante(restaurantes):
    """ Cadastra novos restaurantes na lista
    
    Inputs:
    - list: str - A lista com todos os restaurantes

    Outputs:
    - Exibe mensagem de sucesso para o cadastro de um novo restaurante
    - list: str - Retorna a lista de restaurantes atualizada
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ').title()
    categoria = validar_categoria('Digite a categoria do restaurante: ').title()
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!')
    return restaurantes

def listar_restaurantes(restaurantes):
    """ Lista os restaurantes cadastrados

    Inputs:
    - list: str - A lista com todos os restaurantes

    Outputs:
    - Exibe a lista de restaurantes cadastrados
    """
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do Restaurante'.ljust(24)} | {'Categoria'.ljust(20)} | Status')
    for i, restaurante in enumerate(restaurantes, start=1):
        status = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'\n{i} - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {status}')

def alternar_estado(restaurantes):
    """ Alterna o status ativado/desativado de um restaurante 
    
    Inputs:
    - list: str - A lista com todos os restaurantes

    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    """
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
    """ Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    """
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

from desafios_classes_metodos import Livro

# 6 - No arquivo biblioteca.py, empreste o livro chamando o método
# emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro_1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro_2 = Livro("1984", "George Orwell", 1949)
livro_3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro_4 = Livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925)
livro_5 = Livro("Orgulho e Preconceito", "Jane Austen", 1813)
livro_6 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro_7 = Livro("A Revolução dos Bichos", "George Orwell", 1945)
livro_8 = Livro("A Sociedade do Anel", "J.R.R. Tolkien", 1954)

livro_8.emprestar()
print(livro_8._disponivel)

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade
# para obter a lista de livros disponíveis publicados em um ano específico.

for livro in Livro.verificar_disponibilidade(1954):
    print(livro)

# 8 - Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py,
# instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
# Título, autor, ano de publicação, gênio e número de páginas
livros = []
for i in range(3):
    print(f'\n----- Livro {i+1}-----')

    livro = {}
    
    livro['título'] = input('Nome do livro:')
    livro['autor'] = input('Nome do autor:')
    livro['ano'] = int(input('Ano do livro:'))
    livro['genero'] = input('Gênero do livro:')
    livro['paginas'] = int(input('Quantas páginas do livro:'))

    livros.append(livro)
    print('Livro cadastrado !')

# Mostrando
print('\n--- Livros a partir de 2020 ---')    
for l in livros:
    if l['ano'] >= 2020:
        #print(l)
        print(f"Nome do livro: {l['título']}")
        print(f"Ano do livro: {l['ano']}")


Pessoas_v = {}

pessoa = {}
pessoa['Nome'] = 'João'
pessoa['Idade'] = 25
pessoa['Cidade'] = 'Niterói'
print(pessoa)

# Acessando uma chave
print(pessoa['Cidade'])

# Alterando o valor
pessoa['Idade'] = 26
print(pessoa)

# Chave Nova
pessoa['Profissão'] = 'Programador'
print(pessoa)

# Deletando a chave
del pessoa['Cidade']
print(pessoa)


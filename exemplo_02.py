List_produtos = ['Notebook','Mouse','Teclado','Monitor']

for p in List_produtos:
    print(p)

List_produtos[0] = 'PC'
print(f'Alterar o primeiro elemnto {List_produtos}')

List_produtos.append('WebCam')
print(f'Produto Adicionado {List_produtos}')

List_produtos.remove('Monitor')
print(f'Produto Removido {List_produtos}')

List_produtos.pop()
print(f'Remove o último {List_produtos}')

del List_produtos[0]
print(f'Remove pela posição {List_produtos}')

#print(List_produtos)

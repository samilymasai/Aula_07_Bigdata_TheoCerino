vendas = []

for i in range(3):
    valor = float(input('Informe a venda: '))
    vendas.append(valor)

print(f'Venda registrado {vendas}')

#

for v in vendas:
    if v >= 1000:
       print(f'venda de R${v} - meta atingida')
    elif v >= 700 and v < 1000:
       print(f'Venda de R${v} - próximo da meta')
    else:
        print(f"Venda de R${v} - abaixo da meta") 
          
for o in vendas:
    print(o)

# Meta 1.000 pr venda ; apromx. 700 devem ser por valores abaixo, se indentifiquem como abaixo desempenho.
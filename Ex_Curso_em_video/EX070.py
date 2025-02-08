# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
soma = qtdd_mil = cont = menor = 0
barato = ' '
print('-'*40)
print('          LOJAS SUPER A.D.R.S          ')
print('-'*40)
while True:
    prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    soma += preco
    if preco > 1000:
        qtdd_mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
    if continuar == 'N':
        break
print('-------FIM DO PROGRAMA-------')
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {qtdd_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
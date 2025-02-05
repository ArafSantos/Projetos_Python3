# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao 
# usuário se ele quer ou não continuar a digitar valores.
n = cont = soma = maior = menor = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n     
    continuar = input('Quer continuar [S / N]').upper()
    while continuar not in ['S', 'N']:
        continuar = input('Resposta inválida. Quer continuar [S / N]? ').upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')    
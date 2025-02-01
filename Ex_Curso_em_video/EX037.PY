# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
base = int(input('Qual será a base de conversão? \n[1] para binário \n[2] para octal \n[3] para hexadecimal \nSua opção: '))
if base == 1:
    base, conversao, resultado = 1, 'binário', bin(num)[2:]
    
elif base == 2:
    base, conversao, resultado = 2, 'octal', oct(num)[2:]
    
elif base == 3:
    base, conversao, resultado = 3, 'hexadecimal', hex(num)[2:]
    
else:
    print('Você digitou {}. Os valores aceitos são: 1, 2 ou 3.'.format(num))
print('Número digitado: {} \nConversão para {}: {}'.format(num, conversao, resultado))
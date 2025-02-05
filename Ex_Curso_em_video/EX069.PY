# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
maior_18 = homens = mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip() [0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    continuar = ' '    
    print('-'*20)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip() [0]
    if continuar == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
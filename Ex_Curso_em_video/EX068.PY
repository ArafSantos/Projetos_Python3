# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vitorias = 0
while True:
    cpu = randint(0, 10)
    user = int(input('Diga um valor: '))
    soma = cpu + user
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I] ')).strip().upper() [0]
    print(f'Você jogou {user} e o computador {cpu}. Total de {soma}')    
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!!!')
            vitorias += 1
        else:
            print('Você perdeu!!!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!!!')
            vitorias += 1
        else:
            print('Você perdeu!!!')
            break
print(f'GAME OVER! Você venceu {vitorias} vezes')      
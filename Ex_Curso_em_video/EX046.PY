# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Se preparem para a contagem!!!!')
print('Contagem regressiva!!!')
for r in range(10, -1, -1):
    print(r)
    sleep(1)
print('Feliz Ano Novo!!!!!!!!')

# passo for (1,10)
#   pegar maçã
# trocar a estrutura do laço
# fica enquanto não chegar na maçã - WHILE
# enquanto não chegar na maçã
#   passo
# pega
# while not maçã:
#   passo
# pega
# enquanto não maçã: I    WHILE NOT MAÇÃ:
#   se chão          I       IF CHÃO:
#        passo       I           PASSO
#    se espaço       I       IF ESPAÇO:
#        pula        I           PULA
#    se moeda        I       IF MOEDA:
#        pega        I           PEGA
# pega               I   PEGA
#----------------------------------------------------
'''for c in range(1,10):
    print(c)
print('Fim') # eu sei o limite
n = 1
while n != 0: # flag ponto de parada. condição de parada.
    n = int(input('Digite um valor: '))
print('Fim')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N] ')).upper()
print('Fim')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} numeros impares')
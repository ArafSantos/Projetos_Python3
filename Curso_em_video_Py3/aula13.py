# Nessa aula, vamos começar nossos estudos com os laços
# e vamos fazer primeiro o “for”, que é
# uma estrutura versátil e simples de entender.Por exemplo:
# for c in range(0, 4):
# print(c)
# print(‘Acabou’)
# for c in range(0, 7, 2)# contagem pulando de 2 em 2
# for c in range(6, 0, -1): #contagem regressiva
#     print(c)
# print('FIM')
# n = int(input('digite um numero: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM')
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')
# for in c range (0, 3):
#   n = int(input('Digite um valor: '))
# print('FIM') # ira solicitar para digitar um valor input 3x
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatorio de todos os valores foi {s}')
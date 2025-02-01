nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {} '.format(nome))
print('Prazer em te conhecer {:20} '.format(nome)) # aparecer em 20 caracteres
print('Prazer em te conhecer {:>20} '.format(nome)) # alinhamento a direita
print('Prazer em te conhecer {:<20} '.format(nome)) # alinhamento a esquerda
print('Prazer em te conhecer {:^20} '.format(nome)) # centralizado em 20 espeços
print('Prazer em te conhecer {:=^20} '.format(nome)) # nome centralizado em 20 espaços com = ao lado
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência'.format(di, e))
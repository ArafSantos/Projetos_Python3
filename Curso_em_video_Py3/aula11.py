# PADRÃO ANSI
# /033[style;text;back m
# /033[0;33;44m
# stile codigos =
# 0 none
# 1 bold
# 4 underline
# 7 negative
# TEXT
# 30 branco
# 31 vermelho
# 32 verde
# 33 amarelo
# 34 azul
# 35 majenta
# 36 ciano
# 37 cinza
# BACK
# 40
# 41 vermelho
# 42 verde
# 43 amarelo
# 44 azul
# 45 majenta
# 46 ciano
# 47 cinza
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[7;30m

#PRATICA
# nome = 'Araf'
# cores = {'limpa':'\033[m', }
# print('Ola muito prazem em te conhecer {}{}{}'.format('\033[m', nome, '\033[m'))
idade = int(input('Quantos anos vc tem? '))
n = 19 // 2
n1 = 19%2
print(' {} e {}'.format(n, n1))
from math import sqrt
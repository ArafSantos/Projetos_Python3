# Fatiamento
# frase [9]
# frase [9:13]
# frese [9:21]
# frase [9:21:2] de 9 ate 21 pulando de 2 em 2
# frase [:5] omitindo o inicio ele começa do caracter 0
# frase [15:] do 15 ate o final
# frase [9::3] vai começar no 9 e ir ate o final pulando de 3 em 3
# ANALISE
# len = contar caracter
# count('o') = quantas vezes o 'o' apareceu na frase
# frase.count('o', 0, 13)
# frase.find('deo') = vai te mostrar o momento que começou posição 11
# frase.find('android') = valor menos -1 = android não existe na str
# 'curso' in frase = True
# TRANSFORMAÇÂO
# frase.replace('python, 'android') = vai substituir por android onde tiver python
# frase.upper() = para cima - maiuscula
# frase.lower() = para baixo - minusculo
# frase.capitalize() = so o primeiro caracter fica em maiuscula
# frase.title() = ele analisa e transforma as primeiraas letras de cada palavra em maiuscula
# frase.strip() = vai remover todos os espaços inuteis da string inicio e fim
# frase.Rstrip() = vai remover somente os ultimos espaços RIGHT direita
# frase.Lsprit() = vai remover somente os ultimos espaços LEFT esquerda
# DIVISÃO
# frase.split() = divisão em seus espaços refaz os indices, o split vai dividir uma string em lista
# JUNÇÃO
# '-'.join(frase) = uma unica string. no lugar dos espaços entrara a -
frase = 'Curso em Video Python'
dividido = frase.split()
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso'in frase)
print(frase.find('Curso'))
print(frase.lower().find('video'))
print(frase.split())
print(dividido[2][3])
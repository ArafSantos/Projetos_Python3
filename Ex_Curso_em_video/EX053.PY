# Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).strip().upper().split()
unir = ''.join(frase)
inverter = ''
for letra in range(len(unir) -1, -1, -1):
    inverter += unir[letra]
print('O inverso de {} é {}.'.format(unir, inverter))
if unir == inverter:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
# primitivo e todas as informações possíveis sobre ele.
texto = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(texto))
print('Só tem espaços? ', texto.isspace())
print('É um numero? ', texto.isnumeric())
print('É Alfabético? ', texto.isalpha())
print('É Alfanumerico? ', texto.isalnum())
print('Está em maiusculas? ', texto.isupper())
print('Está em minusculas? ', texto.islower())
print('Está capitalizada? ', texto.istitle())
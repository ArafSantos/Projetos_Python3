# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um valor: '))
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5
print(f'O dobro de {num} vale {dobro}')
print(f'O triplo de {num} vale {triplo}')
print(f'A raiz quadadra de {num} é igual a {raiz:.2f}')
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.
medida = float(input('Digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
hec = medida / 100
dec = medida / 10
decim = medida * 10
print(f'A media de {medida}m corresponde a ')
print(f'{km}km')
print(f'{hec}hm')
print(f'{dec}dam')
print(f'{decim}dm')
print(f'{cm}cm')
print(f'{mm}mm')

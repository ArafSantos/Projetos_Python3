# Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.
temp = float(input('Digite a temperatura em °C: '))
fah = temp * 9/5 + 32
print(f'A temperatura de {temp}°C corresponde a {fah}°F!')
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso;  Entre 18,5 e 25: Peso Ideal
# IMC entre 25,0 e 29,9 Kg/m2: sobrepeso;
# IMC entre 30,0 e 34,9 Kg/m2: obesidade grau I;
# IMC entre 35,0 e 39,9 Kg/m2: obesidade grau II;
# IMC maior do que 40,0 Kg/m2: obesidade grau III
print('Cálculo de IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Olá, o seu peso é {}Kg e a sua altura é {}m. O valor do seu IMC é de {:.1f}Kg/m².'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está com sobrepeso. Sugiro que procure um profissional para verificar a sua saúde.')
elif imc < 25:
    print('Tenho uma ótima notícia, você está no peso ideal.')
elif imc < 29.9:
    print('Você está com sobrepeso. Sugiro que procure um profissional')
elif imc < 34.9:
    print('O valor do seu IMC é o correspondente a obesidade grau I.')
elif imc < 39.9:
    print('O valor do seu IMC é o correspondente a obesidade grau II.')
elif imc < 40.0:
    print('O valor do seu IMC é o correspondente a obesidade grau I.')
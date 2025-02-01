# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salario do Funcionario? R$'))
ajuste = salario + (15 / 100 * salario)
print(f'Um funcionario que ganhava R${salario}, com ajuste de 15% passa a receber R${ajuste:.2f}')
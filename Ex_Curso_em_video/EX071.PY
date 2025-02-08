# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado 
# (número inteiro) e o programa vai informar quantas cédulas 
# de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print('        BANCO A.D.R.S    ')  # Exibe o nome do banco
print('='*30)

while True:  # Loop infinito para permitir múltiplos saques
    saque = int(input('Qual o valor que deseja sacar: R$'))  # Solicita o valor a ser sacado ao usuário

    cedula_50 = saque // 50  # Calcula quantas cédulas de R$50 cabem no valor solicitado
    resto = saque % 50  # Calcula o resto que não cabe nas cédulas de R$50
    print(f'Cédulas de R$50: {cedula_50}')  # Exibe a quantidade de cédulas de R$50

    cedula_20 = resto // 20  # Calcula quantas cédulas de R$20 cabem no valor restante
    resto = resto % 20  # Atualiza o resto após subtrair as cédulas de R$20
    print(f'Cédulas de R$20: {cedula_20}')  # Exibe a quantidade de cédulas de R$20

    cedula_10 = resto // 10  # Calcula quantas cédulas de R$10 cabem no valor restante
    resto = resto % 10  # Atualiza o resto após subtrair as cédulas de R$10
    print(f'Cédulas de R$10: {cedula_10}')  # Exibe a quantidade de cédulas de R$10

    cedula_1 = resto // 1  # O que sobrar é dado em cédulas de R$1
    print(f'Cédulas de R$1: {cedula_1}')  # Exibe a quantidade de cédulas de R$1

    continuar = input('Deseja realizar outro saque? (S/N): ').strip().upper()  # Pergunta ao usuário se deseja fazer outro saque
    if continuar != 'S':  # Se a resposta não for 'S', o programa sai do loop
        break  # Sai do loop

print('Volte sempre ao banco A.D.R.S! Tenha um bom dia!')  # Mensagem final quando o loop é encerrado



# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
# palpites foram necessários para vencer.
from time import sleep 
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar\n'
      '[ 2 ] multiplicar\n'
      '[ 3 ] maior\n'
      '[ 4 ] novos numeros\n'
      '[ 5 ] sair do programa\n')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} é igual a {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'{n1} x {n2} é igual a {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        elif n1 == n2 or n2 == n1:
            print(f'{n1} e {n2} tem o mesmo valor!')
    elif opcao == 4:
        str(input('Primeiro valor: '))
        str(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando.....')
        sleep(3)
    else:
        print('Opção Inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
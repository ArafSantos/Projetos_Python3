# carro.siga()
# carro.esquerda()
# carro.siga()
# carro.direita()
# carro.siga()
# carro.direita()
# carro.siga()
# carro.esquerda()
# carro.siga()
# carro.pare()
# estrutura de sequancia
# estrutura condição
# if carro.esquerda():
#   bloco True
# else:
#   bloco False
# tempo = int(input('Quantos anos tem seu carro? '))
# if tempo <=3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('--FIM--')

# tempo = int(input('Quantos anos tem seu carro? '))
# print('Carro novo'if tempo <=3 else'Carro velho')
# print('--FIM--')
# nome = str(input('Qual o seu nome: '))
# if nome == 'Araf':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
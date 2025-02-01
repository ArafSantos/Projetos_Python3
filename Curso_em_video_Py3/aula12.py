# Estruturas de Controle
# Condições Aninhadas
#   IF, ELIF E ELSE
# Um if pode ter varios elif, pode não ter um else, mas um elif sempre precisa de um if
nome = str(input('Qual é o seu nome? '))
if nome == 'Araf':
    print('Que nome bonito')
elif nome == 'Maria' or nome == 'Dulce' or nome == 'Lucky':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Julia':
    print('Belo nome feminino')
else: # Else é opcional
    print('Seu nome é bem normal')
print(f'Tenha um otimo dia,{nome}!')
# ------------- ESTRUTURA CONDICIONAL ANINHADA ----------------



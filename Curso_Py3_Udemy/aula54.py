"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os  # Importa o módulo para limpar o terminal

# Criando uma lista vazia para armazenar os itens
lista = []

# Loop principal do programa
while True:
    # Exibe o menu de opções
    print('\n📌 Lista de Compras')
    print('[i]nserir  [a]pagar  [l]istar  [s]air')
    opcao = input('Escolha uma opção: ').strip().lower()  # Remove espaços e converte para minúsculas

    # Opção de inserir um item na lista
    if opcao == 'i':
        os.system('cls')  # Limpa o terminal (Windows). Use 'clear' para Linux/macOS
        valor = input('Digite o item para adicionar: ').strip()  # Remove espaços extras
        
        if valor:  # Verifica se o valor não está vazio
            lista.append(valor)  # Adiciona o item à lista
            print(f'✅ {valor} foi adicionado à lista.')
        else:
            print('⚠️ O item não pode ser vazio.')  # Mensagem de erro caso o usuário não digite nada

    # Opção de apagar um item da lista pelo índice
    elif opcao == 'a':
        os.system('cls')  # Limpa o terminal
        
        if lista:  # Verifica se a lista não está vazia antes de tentar apagar
            print('🗑 Lista Atual:')
            for i, item in enumerate(lista):  # Exibe os itens com seus índices
                print(f'[{i}] {item}')
            
            indice_str = input('Digite o índice do item para remover: ').strip()

            try:
                indice = int(indice_str)  # Converte a entrada para inteiro
                removido = lista.pop(indice)  # Remove o item pelo índice
                print(f'❌ {removido} foi removido.')
            except ValueError:
                print('⚠️ Digite um número válido.')  # Caso o usuário não digite um número
            except IndexError:
                print('⚠️ Índice inexistente.')  # Caso o índice esteja fora do tamanho da lista
        else:
            print('⚠️ A lista está vazia, nada para remover.')

    # Opção de listar todos os itens da lista
    elif opcao == 'l':
        os.system('cls')  # Limpa o terminal
        
        if lista:  # Verifica se há itens na lista
            print('📋 Sua lista de compras:')
            for i, item in enumerate(lista):  # Exibe os itens com seus índices
                print(f'[{i}] {item}')
        else:
            print('⚠️ Sua lista está vazia.')

    # Opção de sair do programa
    elif opcao == 's':
        print('👋 Saindo do programa...')
        break  # Sai do loop e encerra o programa

    # Caso o usuário digite uma opção inválida
    else:
        print('⚠️ Opção inválida. Escolha [i], [a], [l] ou [s].')

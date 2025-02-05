'''
O que é o while?
O while (que significa "enquanto" em inglês) é uma estrutura de repetição
em Python que permite executar um bloco de código várias vezes enquanto uma condição for verdadeira.
Como funciona?
A sintaxe básica do while é:
while condição:
    # bloco de código
O while verifica se a condição é verdadeira.
Se for verdadeira, o bloco de código dentro do while é executado.
Depois de executar o bloco, o Python volta a verificar a condição. Se ainda
for verdadeira, o bloco de código é executado novamente.
Esse processo se repete até que a condição se torne falsa, momento em que o while
para de executar o código.
Exemplo simples:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
Explicação:
contador = 0: Iniciamos a variável contador com 0.
while contador < 5:: A condição do while é que o valor de contador seja menor que 5.
print(contador): Dentro do bloco do while, imprimimos o valor de contador.
contador += 1: Em seguida, incrementamos o valor de contador em 1.
O que acontece na execução:
Primeira vez: contador é 0, então 0 é impresso. Depois, o contador vira 1.
Segunda vez: contador é 1, então 1 é impresso. Depois, o contador vira 2.
Terceira vez: contador é 2, então 2 é impresso. Depois, o contador vira 3.
Quarta vez: contador é 3, então 3 é impresso. Depois, o contador vira 4.
Quinta vez: contador é 4, então 4 é impresso. Depois, o contador vira 5.
Fim: Quando contador chega a 5, a condição contador < 5 não é
mais verdadeira, então o while é interrompido.
Quando usar o while?
O while é útil quando você não sabe quantas vezes vai precisar repetir um bloco de código,
mas tem uma condição que vai fazer com que ele pare.
Exemplos de quando usar while:
Quando você precisa de um loop infinito, mas com uma condição de parada (exemplo:
jogo que vai até o jogador vencer ou perder).
Quando você precisa repetir um processo até que o usuário forneça um valor válido
(como validar uma senha ou uma entrada de dados).
Quando o número de repetições depende de algum cálculo que só será
conhecido enquanto o código está sendo executado.
Importante:
Se você não atualizar a variável que é usada na condição, o while
pode entrar em um loop infinito, ou seja, o código ficará repetindo para sempre sem parar.
Por exemplo:
contador = 0
while contador < 5:
    print(contador)
Esse código vai imprimir sempre 0 porque o valor de contador nunca vai mudar,
e a condição contador < 5 nunca se tornará falsa. O Python entraria em um loop infinito.


1. Usando while True:
O while True cria um loop que só será interrompido quando uma condição de saída for
atingida, geralmente dentro do próprio loop. Esse tipo de loop é útil quando você
não sabe de antemão quantas vezes o loop precisa ser executado, mas sabe que ele deve
continuar até uma condição ser atendida (por exemplo, quando o usuário digitar algo específico).

Exemplo 1: Repetir até o usuário digitar "sair" Aqui, o loop vai continuar pedindo
a entrada do usuário até ele digitar "sair".

while True:
    comando = input("Digite 'sair' para parar: ").lower()
    if comando == "sair":
        print("Você saiu do programa.")
        break  # Quebra o loop quando o usuário digitar 'sair'
    else:
        print(f"Você digitou: {comando}")
2. Usando while com condição específica:
Esse tipo de loop continua executando enquanto a condição especificada for verdadeira.
É uma forma mais controlada de interromper o loop baseado em alguma variável ou condição.

Exemplo 2: Continuar até a lista estar vazia: Se tivermos uma lista de tarefas,
e queremos continuar processando até que a lista esteja vazia, podemos usar um
while com a condição while lista (que vai verificar se a lista não está vazia).


tarefas = ["Estudar", "Comprar comida", "Limpar a casa"]

while tarefas:
    tarefa = tarefas.pop(0)  # Retira a primeira tarefa da lista
    print(f"Fazendo: {tarefa}")

print("Todas as tarefas foram feitas!")
Como funciona:

Enquanto a lista tarefas não estiver vazia (while tarefas), ele vai retirar (pop) e mostrar as tarefas.
Quando a lista estiver vazia, o while para, e o programa imprime "Todas as tarefas foram feitas!"
3. Usando while com not:
Você também pode usar while not para continuar o loop enquanto uma condição for falsa.
 Isso é útil quando você quer esperar até que algo se torne verdadeiro.

Exemplo 3: Pedir uma entrada válida do usuário Aqui, o programa vai continuar pedindo
para o usuário digitar um número positivo até que ele forneça uma entrada válida.

numero = -1
while numero < 0:  # Vai continuar enquanto o número for negativo
    numero = int(input("Digite um número positivo: "))

print(f"Você digitou o número {numero}.")
Como funciona:

O loop vai continuar até que o usuário digite um número positivo.
Quando o número for maior ou igual a 0, a condição numero < 0 será falsa, e o loop vai parar.
4. Usando while com is not:
O is not é um operador de identidade, e é útil para comparar objetos,
como listas ou strings, para garantir que não são o mesmo objeto.

Exemplo 4: Continuar até uma lista ser diferente de um valor específico
Aqui, vamos continuar processando até a lista ser diferente de um valor específico.

lista = [1, 2, 3, 4, 5]

while lista is not None:  # Enquanto a lista não for None
    item = lista.pop(0)  # Retira o primeiro item da lista
    print(f"Processando o item: {item}")

    # Se a lista estiver vazia, podemos atribuir None para parar o loop
    if not lista:
        lista = None  # Alteramos a lista para None para sair do loop

print("Lista vazia, programa finalizado.")
Como funciona:

O loop continua enquanto a lista não for None.
Quando a lista estiver vazia, ela é definida como None, interrompendo o loop.
Resumo:
while True: Útil quando você não sabe o número de iterações e precisa de uma
condição de saída interna (break).
while com condição simples: Usado para loops baseados em uma condição verdadeira,
como uma lista não vazia ou um número que atenda a certos critérios.
while not: Ideal para quando você deseja que o loop continue até que uma condição
se torne verdadeira (ou falsa), como uma entrada do usuário.
while is not: Usado para comparar a identidade de objetos, geralmente utilizado
quando queremos garantir que algo não seja um valor específico como None.
Esses exemplos devem te ajudar a entender melhor o uso do while em diferentes
cenários! Se ainda tiver alguma dúvida, posso ajudar mais.
'''
while True:
    nome = input('Digite seu nome (ou "sair" para parar): ').lower()
    if nome == 'sair':
        break  # Sai do loop
    print(f'Olá, {nome}!')
print('Programa encerrado!')

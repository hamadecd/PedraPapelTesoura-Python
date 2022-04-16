import random

# variáveis para controlar a pontuação do jogo
pontuacao_Jogador = 0
pontuacao_Computador = 0

while True:
    pass
    # Array que contém as 3 opções do jogo
    computador = ('pedra', 'papel', 'tesoura')

    # recebe o valor digitado pelo jogador
    jogador = input('Digite Pedra, Papel, Tesoura\n').lower()

    # agora computador recebe somente um valor aleatório, escolhido dentre seu conjunto de valores
    computador = random.choice(computador)

    # nome de variável em Python normalmente se usa o caractere underline para separar as palavras (nome disso é Snake_Case, temos o CamelCase entre otros
    # mas por boas práticas de desenvolvimento o mais comum é utilizar o snake_case)
    informa_Resultado = ''

    if jogador == computador:
        informa_Resultado = 'Deu empate'
    elif (jogador == 'pedra'):
        if computador == 'tesoura' :
            informa_Resultado = 'Você Venceu'
            pontuacao_Jogador = pontuacao_Jogador + 1
        elif computador == 'papel' :
            informa_Resultado = 'Você Perdeu'
            pontuacao_Computador = pontuacao_Computador + 1
    elif (jogador == 'papel'):
        if computador == 'pedra' :
            informa_Resultado = 'Você Venceu'
            pontuacao_Jogador = pontuacao_Jogador + 1
        elif computador == 'tesoura' :
            informa_Resultado = 'Você Perdeu'
            pontuacao_Computador = pontuacao_Computador + 1
    elif (jogador == 'tesoura'):
        if computador == 'papel' :
            informa_Resultado = 'Você Venceu'
            pontuacao_Jogador = pontuacao_Jogador + 1
        elif computador == 'pedra' :
            informa_Resultado = 'Você Perdeu'
            pontuacao_Computador = pontuacao_Computador + 1
    else:
        informa_Resultado = 'Não foi informada uma palavra válida'

    # Antes de exibir o resultado, o jogo mostra cada opção os jogadores escolheram
    print('Jogador escolheu: ' + jogador + ' \nComputador escolheu: ' + computador)

    print('\nPontos do jogador: {}'.format(pontuacao_Jogador) + '\nPontos do computador: {}'.format(pontuacao_Computador) + '\n' + informa_Resultado)

    #lembrar sempre de ter um código limpo e de fácil entendimento. Evitar de deixar sem espaçamento entre as linhas.

    #variável para repetir o game
    repetir = input("\nJogar Novamente? (s/n)").lower()

    #condição para repetir o game
    if repetir != 's':
        break

if pontuacao_Jogador > pontuacao_Computador:
    print('O vencedor é jogador com o total de {}'.format(pontuacao_Jogador) + ' vitória(s)')
elif pontuacao_Computador > pontuacao_Jogador:
    print('O vencedor é computador com o total de {}'.format(pontuacao_Computador) + ' vitória(s)')
else:
    print('O jogo terminou empatado!')
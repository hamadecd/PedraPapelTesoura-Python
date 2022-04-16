# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
# variável que contém as 3 opções do jogo
computador = ('pedra', 'papel', 'tesoura')
# recebe o valor digitado pelo jogador
jogador = input('Digite Pedra, Papel, Tesoura\n')
# agora computador recebe somente um valor aleatório, escolhido dentre seu conjunto de valores
computador = random.choice(computador)
# nome de variável em Python normalmente se usa o caractere underline para separar as palavras
informa_Resultado = ''

if jogador == computador:
    informa_Resultado = 'Você Empatou'
elif (jogador == 'pedra'):
    if computador == 'tesoura' :
        informa_Resultado = 'Você Venceu'
    elif computador == 'papel' :
        informa_Resultado = 'Você Perdeu'
elif (jogador == 'papel'):
    if computador == 'pedra' :
        informa_Resultado = 'Você Venceu'
    elif computador == 'tesoura' :
        informa_Resultado = 'Você Perdeu'
elif (jogador == 'tesoura'):
    if computador == 'papel' :
        informa_Resultado = 'Você Venceu'
    elif computador == 'pedra' :
        informa_Resultado = 'Você Perdeu'
else:
    informa_Resultado = 'Não foi informada uma palavra válida'
# Antes de exibir o resultado, o jogo mostra cada opção os jogadores escolheram
print('Jogador escolheu: ' + jogador + ' \nComputador escolheu: ' + computador)

print(informa_Resultado)
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
computador = ("pedra", "papel", "tesoura")
valor = input("Digite Pedra, Papel, Tesoura\n")
computador = random.choice(computador)
f = ""

if valor == computador:
    f = "Você Empatou"
elif (valor == "pedra"):
    if computador == "tesoura" :
        f = "Você Venceu"
    elif computador == "papel" :
        f = "Você Perdeu"
elif (valor == "papel"):
    if computador == "pedra" :
        f = "Você Venceu"
    elif computador == "tesoura" :
        f = "Você Perdeu"
elif (valor == "tesoura"):
    if computador == "papel" :
        f = "Você Venceu"
    elif computador == "pedra" :
        f = "Você Perdeu"
else:
    f = "Palavra não encontrada"

print("Jogador escolheu: " + valor + " \nComputador escolheu: "+computador)

print(f)
#Jogo pedra, papel e tesoura

import random

lista =('Pedra', 'Papel', 'Tesoura')
resultado = random.choice(lista)
print('Escolha: Pedra, Papel ou Tesoura')
jogador = str(input('Informe a sua jogada:')).strip()
print('A máquina escolheu: {}'.format(resultado))
if resultado == jogador:
    print('Empate, ninguém ganhou.')

elif resultado == 'Papel' and jogador == 'Pedra':
    print('A máquina venceu.')
elif resultado == 'Tesoura' and jogador == 'Papel':
    print('A máquina venceu.')
elif resultado == 'Pedra' and jogador =='Tesoura':
    print('A máquina venceu.')
else:
    print('Você ganhou.') 


    #Poderia ter usado numeros ao invés de caractere. Exemplo: "[0]Papel" no lugar de "Papel"
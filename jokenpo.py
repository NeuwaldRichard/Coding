'''
Jogo pedra, papel e tesoura!
'''
#Lista de Bugs#
# 1 - Pensar em solucao para nao sair numeros iguais sem usar loop, ou quando for igual colocar que empatou.
# 2 - Solucao para caso digite numeros sem ser 1, 2 ou 3, ou colocar uma mensagem dizendo que o numero escolhido nao e valido.
import random
from time import sleep

print(6*'*~._.~''*')
print('                  Jokenpo')
print(6*'*~._.~''*')
print('\n')
print('Tente me vencer! :D')
print('\n')
print('''Sua vez, jogador! 
[1] - Pedra
[2] - Papel
[3] - Tesoura
''')
player1 = int(input('Digite o numero correspondente a sua escolha: '))
print('')
print('  JOOO')
sleep(1)
print('      KENNN')
sleep(1)
print('           POOO')
sleep(1)
print('')

player2 = random.randint(1 , 3) 

if player1 == 1:
    print('Voce escolheu PEDRA!')
elif player1 == 2:
    print('Voce escolheu PAPEL!')
else:
    print('Voce escolheu TESOURA!')

if player2 == 1:
    print('Eu escolhi PEDRA!')
elif player2 == 2:
    print('Eu escolhi PAPEL!')
else: 
    print('Eu escolhi TESOURA!')
print('')
sleep(1)
if player1 == 1 and player2 == 3:
    print('Parabens, Voce Ganhou!')
elif player1 == 2 and player2 == 1:
    print('Parabens, Voce Ganhou!')
elif player1 == 3 and player2 == 2:
    print('Parabens, Voce Ganhou!')
else:
    print('Que pena, Voce Perdeu.')
print('')
print('Pressione enter para sair do jogo.')
input()
'''Estava estudando condicoes e me deparei com um exercicio envolvendo triangulos extremamente nostalgico, me lembrei
da minha epoca de estudante de ensino fundamental de exercicios de matematica...
Entao aqui uma ideia de como fazer uma calculador para aplicar a formula de bhaskara!
math.pow() por algum motivo que ainda nao sei dependendo do numero que coloco ele da um bug, '''
## lista de bugs que tive ##
#1- erro quando delta era negativo ( acrescentado variavel de quando valor de delta for negativo, nao existe raizes ) 
#2- erro no math.pow() (por algum motivo que nao descobri ainda, dependendo do numero digitado para variavel 'b' da 
#erro na linha de codigo referente ao math.pow(), troquei para operador simples ** para fazer elevado ao quadrado 
#e funcionou

import math
from time import sleep

print(10*'=-=')
print('Equacao 2º Grau bhaskara.')
print(10*'=-=')
print('')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b ** 2) -4 * a * c

print(f'Delta e igual a: {delta:.2f}')
if delta < 0:
    print('Como o resultado de delta foi um numero negativo, nao ha raizes para ele!')
else:
    print('Agora vamos determinar as raizes da equacao!..')
    sleep(2)
    x1 = (-(b) + math.sqrt(delta))/ (2 * a)
    x2 = (-(b) - math.sqrt(delta))/ (2 * a)
    print(f'O valor de x1 e: {x1:.2f}')
    print(f'O valor de x2 e: {x2:.2f}')
print('')
print('Aperte Enter para sair do programa.')
input()

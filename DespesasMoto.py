'''
Uma ideia que tive quando comecei a fazer entregas de moto para conseguir verificar exatamente o quanto vc esta gastando
para prestar um servico de entrega no caso. Isso somente e possivel quando conseguimos tomar nota de todos os gastos
que temos para prestar um determinado servico.
'''
## Lista de Bugs ##
#1º quando e apertado enter somente e nao digitado o valor ( nao corrigido ainda ) tentar algo com condicao if
#2º corrigido erro quando digitado valor zero, adicionando a condicional if valor == 0, porem agora se vc digitar o dividendo
#ele vai dar o valor dele mesmo ao invez de dar zero


print(15*'=-=')
print('CALCULADORA DE DESPESAS VEICULO')
print(15*'=-=')
print('\n')

print('Preencha com valores atualizados os quais voce pagou ou orcou recentemente!')
print('')
combustivel = float(input('Qual o valor do combustivel que voce utiliza? R$ '))
autonomia = float(input('Quantos Km/l de autonomia seu veiculo faz? '))

oleo = float(input('Qual o custo para fazer a troca de oleo do seu veiculo? R$ '))
troca_de_oleo = float(input ('A cada quantos Km percorridos voce troca o oleo? '))

revisao = float(input('Se voce faz revisao qual o valor da revisao? Se nao digite 0: R$ '))
autonomia_revisao = float(input('Quatos Km voce rodou ate esta revisao em especifico? '))


freio = float(input('Qual valor gasto na troca das pastilhas de freio? R$ '))
troca_freio = float(input('Quantos Km voce rodou ate a troca das pastilhas de freio? '))

pneu = float(input('Qual o valor gasto no jogo de pneus? R$ '))
troca_pneu = float(input('Quantos Km voce rodou ate a troca dos pneus? '))
print('')
km = float(input('Diga quantos Km rodou no ultimo mes que vou fazer uma previsao rapida: '))
print('')

if autonomia == 0:
    autonomia = 1
if troca_de_oleo == 0:
    troca_de_oleo = 1
if autonomia_revisao == 0:
    autonomia_revisao = 1
if troca_freio == 0:
    troca_freio = 1
if troca_pneu == 0:
    troca_pneu = 1


consumo = (combustivel / autonomia)
autonomia_oleo = (oleo/troca_de_oleo)
revisao = (revisao/autonomia_revisao)
autonomia_freio = (freio/troca_freio)
autonomia_pneu = (pneu/troca_pneu)

despesa_total = consumo + autonomia_oleo + revisao + autonomia_freio + autonomia_pneu
despesa_mes = despesa_total * km

print(f'''Segue entao sua lista de despesas abaixo:
Combustivel                 {consumo:.2f}
Troca de Oleo               {autonomia_oleo:.2f}
Revisao                     {revisao:.2f}
Troca de Pastilha de Freios {autonomia_freio:.2f}
Troca dos pneus             {autonomia_pneu:.2f}
''')
print('')
print(f'Voce rodou {km}Km este mes, e sua despesa foi de R$ {despesa_mes:.2f}! ')
print('')            
print(f'Seu consumo eh de R$ {despesa_total:.2f} por Km rodado.')
print('')
print('Pressione enter para finalizar o programa.')
input()


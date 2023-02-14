primeiro = int(input('primeiro termo: '))
posição = int(input('posição do termo que quer descobri: '))
razao = int(input('razão: '))
t = 1
while t <= posição:
    an = primeiro + (t - 1)* razao
    print(an,end=' ')
    t = t + 1 # somando 1 na varial ' t ' ate igualar ao valor do termo ,afim de cancelar a repetiçao .alcançando assim ,o valor false na condiçao .
print('Fim')
print('=-'* (posição + 10))

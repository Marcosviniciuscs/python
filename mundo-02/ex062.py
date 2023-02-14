print('{:=^19}'.format(' Gerador de PA '))
primeiro = int(input('primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
mais = 1
posiçao = 10
while mais != 0:
    posiçao = posiçao + mais
    while cont < posiçao:
        an = primeiro + (cont - 1) * razão
        cont = cont + 1
        print(an,end=' ')
    print('Pausa')
    mais = int(input('Quer ler mais algum termo? '))
print('foram lidos um total de {} termos'.format(cont - 1))

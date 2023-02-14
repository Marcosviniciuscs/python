from time import sleep
def lin():
    print("=" * 50)


def contador(inicio, fim , passo):
    if inicio > fim:
        if passo[0] in "-": #negativo
            comeco = inicio
            ultimo = fim-1
        else: #positivo
            comeco = fim
            ultimo = inicio+1
    if inicio < fim:
        if passo[0] in "-": #negativo
            comeco = fim
            ultimo = inicio-1
        else: #positivo
            comeco = inicio
            ultimo = fim+1
    pas = int(passo)
    if pas == 0:
        pas = 1
    for e in range(comeco, ultimo, pas):
        print(e, end=' ')
        sleep(0.3)
    print()


#programa principal
lin()
print('Contagem de 1 até 10:')
for c in range(1, 11, 1):
    print(c, end=' ')
    sleep(0.3)
print()
lin()
print('Contagem de 10 ate 0:')
for d in range(10, -1, -2):
    print(d, end=' ')
    sleep(0.3)
print()
lin()
i = int(input('Início: '))
f = int(input('Fim: '))
p = str(input('Passo: '))
print('Contagem Personalizada:')
contador(i, f, p)

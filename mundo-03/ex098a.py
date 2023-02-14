from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} e {p}')
    if i < f:#crescente
        if p < 0:#passo negativo
            for e in range(f, i, p):
                print(e, end=" ")
                sleep(0.3)
            print()
        if p > 0:#passo positivo
            for c in range(i, f+1, p):
                print(c, end=" ")
                sleep(0.3)
            print()
    if i > f:#decrescente
        if p < 0:# passo descrescente
            for n in range(i, f-1, p):
                print(n, end=" ")
                sleep(0.3)
            print()
        if p > 0:
            for n in range(i, f-1, -p):
                print(n, end=" ")
                sleep(0.3)
            print()


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de fazer uma contagem: ')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)

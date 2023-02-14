lista = []
# cria 5 input atraves do laço 'for' para adiciona-los na lista,atraves do método 'append'(acrescentar)
for c in range(0,5):
    lista.append(int(input(f'Digite um número para posição {c}: ')))
print(f'voce digitou os valores: {lista}')
#descobrir o maior e o menor valor
maior = 0
menor = 0
for pos, num in enumerate(lista):
    if pos == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
#usado para comparar os valores descorbertos (maior e menor) com intuito de descobrir as posições.
listaposicaomai = []
listaposicaomen = []
for i, v in enumerate(lista):
    if v == maior:
        listaposicaomai.append(i)
    elif v == menor:
        listaposicaomen.append(i)
print(f'o maior numero digitado foi {maior} e se encontra na posição: {listaposicaomai}')
print(f'o menor numero digitado foi {menor} e se encontra na posição: {listaposicaomen}')

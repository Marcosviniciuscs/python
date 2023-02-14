print('='*25)
print('{:>20}'.format('LoJa do Marcão'))
print('='*25)
soma = totmil = 0
menor = 0
contl = 0
probarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('preço: R$ '))
    soma = soma + preço
    contl = contl + 1 #saber quando é o primeiro produto ou segundo...
    if preço >= 1000:
        totmil = totmil + 1
    if contl == 1:
        menor = preço
        probarato = produto
    elif preço < menor:#ou seja ,tenho menor preço e o nome ,porque esta dentro do laço no momento.
        menor = preço
        probarato = produto
    resp = ' '
    while resp not in 'SN': #enquanto a informação da variavel 'resp' nao for 'S ou n' ,o laço vai repetir (validação de dados)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^35}'.format('Fim do programa'))
print(f'O cliente gastou um total de R$ {soma}')
print(f'o cliente adquiriu {totmil} produtos que custam mais de R$1000')
print(f'o produto mais barato é o(a) {probarato} e custa R${menor}')
print('/'*30)

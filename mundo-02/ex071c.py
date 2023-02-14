print('='*25)
print('{:^25}'.format('GIFSTORE'))
print('='*25)
total = contmil = contlaço = 0
probarato = ' '
menor = 0
while True:
    print('=-'*18)
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    opção = ' '
    total = total + preço
    contlaço += 1 #saber o primeiro momento do laço ou o segundo ...
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preço >= 1000:
        contmil = contmil + 1
    if contlaço == 1 or preço < menor:
        menor = preço
        probarato = nome
    if opção == 'N':
        break
print('{:=^30}'.format('Fim Do Programa'))
print(f'o total gasto na compra foi R$ {total}.')
print(f'o cliente adquiriu {contmil} produto(s) que custam mais de R$1000 .')
print(f'o {probarato} é o produto  mais barato e custa R${menor} .')
print('*-'*18)

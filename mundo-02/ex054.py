from datetime import date
data = date.today().year
contmaior = 0
contmenor = 0
for c in range(1,8):
    nasc = int(input('{}ª data de nascimento: '.format(c)))
    idade = data - nasc
    print('{} anos.'.format(idade))
    if idade < 18:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor + 1
print('\n{} pessoas nao atingiram a maioridade.'.format(contmaior))
print('{} ja sao maiores de idades.'.format(contmenor))

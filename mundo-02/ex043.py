print('OBS:o peso deve estar em KG e a altura em Metros')
peso = float(input('quanto você pesa? '))
altura = float(input('qual e a sua altura: '))
imc = peso / altura**2
print('o seu IMC : {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('voce esta com o Peso normal')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print('cuidade!voce esta em Obesidade')
else:
    print('cuidado!voce esta em Obesidade Mórbida')



peso = float(input('quanto você pesa? '))
alt = float(input('qual é a sua altura? '))
imc = peso / alt**2
print('\no seu IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('peso normal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

salário = float(input('quanto e o salário do funcionário? '))
if salário >= 1250:
    calculo = salário + (salário * 10) / 100
    print('o funcionário recebeu um aumento de 10 %,entao o salário passou a ser R${:.2f} .'.format(calculo))
else:
    calculo = salário + (salário * 15) / 100
    print('o funcionário recebeu um aumento de 15%,então o salario passou a ser R${:.2f} .'.format(calculo))

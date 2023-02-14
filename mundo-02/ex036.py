casa = float(input('qual e o valor da casa? '))
salario = float(input('salário do comprador? '))
anos = float(input('Em quantos anos voce quer pagar a casa? '))
#30% referente ao valor do salario do cliente
mínimo = (salario * 30) / 100
#representa os meses(ou parcelas)
meses = anos *12
prestação = casa / meses
if prestação <= mínimo:
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('EMPRESTIMO NEGADO!')
print('o cliente pagará {} parcelas no valor de R${:.2f} ,durante {} anos'.format(meses, prestação, anos))


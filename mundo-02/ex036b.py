from datetime import date
cores = {'red':'\033[1;31m','limpa':'\033[m'}
casa = int(input('qual e o valor da casa?  '))
salario = float(input('salário do comprador? '))
anos = int(input('quantos anos para pagar a casa?  '))
prestação = casa / (anos * 12) #<-meses
porcentagem = salario * 30 / 100
if prestação <= porcentagem:
    data = date.today().year
    print('\033[1;33mEmpréstimo concedido!\n\033[1;34mO valor da prestação será de R${:.2f}'
          ' mensais,que sera concluida em {}'.format(prestação,data + anos))
else:
    print('{}Empréstimo negado!{}'.format(cores['red'],cores['limpa']))


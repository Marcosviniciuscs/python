carro = float(input('qual e a velocidade do carro?KM '))
if carro > 80:
    m = (carro - 80) * 7
    print('velocidade acima do permitido!\nvoce foi multado em R${:.2f} reais'.format(m))
print('TENHA UM BOM DIA!DIRIJA COM SEGURANÇA.')

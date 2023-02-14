lista = ('Zero','Um','Dois','Três','Quatro','Cinco',
         'Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Trêze','Quatorze','Quinze',
         'Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input('qual número voce deseja mostrar? [entre 0 e 20] '))
    if num >= 0 and num <= 20:
        print(f'voce digitou o número {lista[num]}')
        opção = str(input('Quer continuar? [S/N] ')).upper()
        while opção not in 'SN':
            opção = str(input('Quer continuar? ')).upper()
        if opção == 'N':
            print('programa finalizado.')
            break

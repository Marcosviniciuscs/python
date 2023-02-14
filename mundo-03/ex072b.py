lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'Dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze',
         'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num <= 20 and num >= 0:
        break
print(f'você digitou o número {lista[num]}')
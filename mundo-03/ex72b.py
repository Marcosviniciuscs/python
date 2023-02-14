tupla = ('zero', 'um', 'dois', 'três', 'quatro','cinco',
         'seis','sete','oito','nove','dez',
         'onze','doze','treze','quatorze','quinze',
         'dezesseis', 'dezesete','dezoito','dezenove','vinte')
while True:
    num = int(input('informe um número de 0 até 20: '))
    while num < 0 or num > 20:
        if num == 999:
            break
        num = int(input('tente novamente! digite um número: '))
    if num == 999:
        break
    print(tupla[num])


print('\033[4;31m{:=^36}\033[m'.format(' conversor de temperatura '))
cel = int(input('\033[4;36mqual e a temperatura em graus?  \033[m'))
conv = cel / 5 * 9 + 32
print('{}a temperatura de {}ºC correspode a {:.2f}ºF'.format('\033[4;31m',cel , conv))



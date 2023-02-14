nome = str(input('qual e o seu nome completo: ')).strip()
print('seu nome em letras maiusculas e {}'.format(nome.upper()))
print('seu nome em letras minúsculas e {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
val = nome.split()
print('o seu primeiro nome é {} e possui {} letras '.format(val[0].capitalize(),len(val[0])))



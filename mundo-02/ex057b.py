sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos.tente novamente: [M/F] ')).strip().upper()[0]
print('sexo {} registrado com sucesso.'.format(sexo))
# sempre que for diferente, ele continua repetindo porque atende a logica.caso:ex:'m = m ',nao atende a logica ,prossegue saindo do loop
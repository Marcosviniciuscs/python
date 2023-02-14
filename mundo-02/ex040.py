n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
print('\033[1;34ma media das suas notas e igual a {}\033[m'.format(media))
if media < 5:
    print('\033[1;31mo aluno está REPROVADO\033[m')
elif media >= 5 and media < 7:
    print('\033[1;33mo aluno está em RECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[1;32mo aluno está APROVADO\033[m')

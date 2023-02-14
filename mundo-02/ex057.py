s = str(input('informe o seu sexo: ')).upper().strip()
while s != 'M' and s != 'F': # usando o 'and' o programa vai entender que as duas condiçoes terão que ser satisfeitas.
        s = str(input('valor errado.Digite novamente o seu sexo: ')).upper().strip()
print('fim')
# caso tivesse usado o 'or' ,o while consegue satisfazer uma condição e a outra não.pois há uma comparação ,
# mesmo usando o 'm ou F ' uma será verdadeiro e a outra falsa, então... entre no loop.

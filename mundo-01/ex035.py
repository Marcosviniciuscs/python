med1 = float(input('informe o primeiro lado: '))
med2 = float(input('informe o segundo lado: '))
med3 = float(input('informe o terceiro lado: '))
#maior número
if med1 > med2 and med1 > med3:
    maior = med1
if med2 > med1 and med2 > med3:
    maior = med2
if med3 > med2 and med3 > med1:
    maior = med3
print(maior)
#número médio
if med1 > med2:
    media = med1
if med2 > med1:
    media = med2
else:
    media = med3
print(media)
#menor numero
if med1 < med2 and med1 < med3:
    menor = med1
if med2 < med1 and med2 < med3:
    menor = med2
if med3 < med1 and med3 < med2:
    menor = med3
print(menor)
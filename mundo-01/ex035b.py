s1 = float(input('informe o primeiro segmento: '))
s2 = float(input('informe o segundo segmento: '))
s3 = float(input('informe o terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('os segmentos acima podem FORMAR um trinagulo!')
else:
    print('os segmentos acima não podem FORMAM triangulos! ')
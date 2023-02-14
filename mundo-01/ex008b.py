print('{:=^20}'.format(' conversor '.upper()))
medida = float(input('informe medida em Metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dec = medida * 10
cm = medida * 100
mm = medida * 1000
print('Metros para kilometro = {}\nMetros para hectômetro {}\nMetros para decâmetro {}\nMetros {}\nMetro para decimetro {}'
      '\nMetro para centímetro {}\nMetro para milimitro {}'.format(km,hm,dam,medida,dec,cm,mm))

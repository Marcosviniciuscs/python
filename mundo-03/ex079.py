while True:
    q = float(input('nota do usuario:  '))
    ef = 2.5
    ef = ef + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    print(ef)


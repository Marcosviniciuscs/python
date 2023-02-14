from time import sleep

def maior(*num):
    mai = 0
    print('=-'*30)
    print("De acordo com os números apresentados:")
    for pos, n in enumerate(num):
        print(n, end=" ")
        sleep(0.3)
        if pos == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f'=> Foram informados {len(num)} valores.')
    print(f'Dentre todos esses números, o maior é: {mai}')
    sleep(0.2)


maior(5,0,2,6,50)
maior(2,5,80,9)
maior(1,2,3,4,5,6,2,8)
maior(20,30,15)
maior(5,8,9,1)
maior()

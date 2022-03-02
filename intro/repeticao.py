numero = int(input("Digite um numero: "))

for num in range(1, numero + 1):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print('numero {} é primo'.format(num))

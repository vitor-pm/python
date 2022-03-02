num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))
num3 = int(input("Entre com o terceiro numero: "))
resto1 = num1 % 2
resto2 = num2 % 2
resto3 = num3 % 2

if resto1 == 0 or resto2 == 0 or resto3 == 0:
    print('Foi digitado um numero par')
else:
    print('Não foi digitado numero par')

if num1 > num2 and num1 > num3:
    print('O maior numero é {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior numero é {}'.format(num2))
else:
    print('O maior numero é {}'.format(num3))

print('fim')

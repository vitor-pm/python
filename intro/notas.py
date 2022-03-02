a = int(input("Entre com a primeira nota: "))
while a > 10:
    print('Nota Invalidada. Entre com uma nota até 10.')
    a = int(input("Entre com a primeira nota: "))

b = int(input("Entre com a segunda nota: "))
while b > 10:
    print('Nota Invalidada. Entre com uma nota até 10.')
    b = int(input("Entre com a segunda nota: "))
c = int(input("Entre com a terceira nota: "))
while c > 10:
    print('Nota Invalidada. Entre com uma nota até 10.')
    c = int(input("Entre com a terceira nota: "))
d = int(input("Entre com a quarta nota: "))
while d > 10:
    print('Nota Invalidada. Entre com uma nota até 10.')
    d = int(input("Entre com a quarta nota: "))

media = (a + b + c + d) / 4

print('media: {}'.format(media))

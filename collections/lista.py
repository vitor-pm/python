lista = [7, 8, 2, 5]
lista_animal = ['cachorro', 'gato', 'elefante']

for x in lista:
    print(x)

print('Soma: {soma}, Menor Valor: {menor}, Maior Valor: {maior}'
      .format(soma=sum(lista), menor=min(lista), maior=max(lista)))

for x in lista_animal:
    print(x)

animal = input('Digite um animal: ')

if animal in lista_animal:
    print('Existe {} na lista'.format(animal))
else:
    print('Não existe {} na lista, sera adicionado'.format(animal))
    lista_animal.append(animal)

for x in lista_animal:
    print(x)

# Remove e retorna o ultimo valor ou o item do index informado
ultimo = lista_animal.pop()
print(ultimo)

# Organizando a lista
lista.sort()
print(lista)

# Convertendo a lista para tupla (objetos da tupla nao podem ser alterados)
lista_animal = tuple(lista_animal)
print(lista_animal)

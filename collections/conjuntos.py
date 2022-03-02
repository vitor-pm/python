conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2)
print('Uniao Conjuntos um e dois {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Interseccao conjunto um e dois {}'.format(conjunto_interseccao))
conjunto_dif1 = conjunto.difference(conjunto2)
conjunto_dif2 = conjunto2.difference(conjunto)
print('Diferença entre um e dois {} '.format(conjunto_dif1))
print('Diferença entre dois e um {} '.format(conjunto_dif2))
conjunto_difsimetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simetrica {} '.format(conjunto_difsimetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('Conjunto A é um subconjunto de B: {}'.format(conjunto_subset))
print('Conjunto B é um superconjunto de A: {}'.format(conjunto_superset))

# convertendo lista para conjunto(conjunto nao tem duplicidade)
lista_animal = ['cachorro', 'gato', 'elefante', 'cachorro']
conjunto_animal = set(lista_animal)
print(conjunto_animal)

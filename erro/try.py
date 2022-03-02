try:
    num = int(input('Digite um numero: '))
    divisao = 10 / num
    lista = [5,4]
    print(lista[1])
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except IndexError:
    print('Indice não encontrato')
except Exception as ex:
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa se não houver nenhum erro')
finally:
    print('Sempre executa')
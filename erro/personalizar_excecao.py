class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message = message

while True:
    try:
        nota = int(input('Digite uma nota de 0 a 10: '))
        if nota > 10:
            raise InputError('Nota maior que 10')
        elif nota < 0:
            raise InputError('Nota menor que 0')
        break
    except ValueError:
        print('Digite apenas numeros')
    except InputError as ex:
        print(ex)

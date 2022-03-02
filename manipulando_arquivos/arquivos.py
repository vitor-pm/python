def escrever_arvivo():
    arquivo = open('texto.txt', 'w')
    arquivo.write('Primeira linha')
    arquivo.close()

def atualizar_arvivo():
    arquivo = open('texto.txt', 'a')
    arquivo.write('\nSegunda linha')

def ler_arvivo():
    arquivo = open('texto.txt', 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrever_arvivo()
    atualizar_arvivo()
    ler_arvivo()
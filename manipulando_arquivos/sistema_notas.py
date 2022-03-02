alunos = ['vitor,4,5,6,7','julio,7,1,2,9','maria,8,5,7,2']

def inserir_aluno():
    aluno = input('Qual o nome do aluno:')
    notas = input('Digite as notas')
    alunos.append(aluno + "," + notas)

def gravar_aluno(lista):
    arquivo = open('alunos.txt','w')
    for x in alunos:
        arquivo.write('\n' + x)

def medias():
    arquivo = open('alunos.txt','r')
    alunos_notas = arquivo.read()
    alunos_notas = alunos_notas.split('\n')
    alunos_notas.pop(0)
    media = lambda notas: sum([int(i) for i in notas]) / 4
    for aluno in alunos_notas:
        notas = aluno.split(',')
        print('Aluno = ' + notas.pop(0))
        print(notas)
        print('Media = ' + str(media(notas)))

if __name__ == '__main__':
    gravar_aluno(alunos)
    medias()
from datetime import date, time,datetime

def trabalhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))

def trabalhando_time():
    data_atual = time(15,55,27)
    print(data_atual)

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%c'))
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Doming')
    print(tupla[data_atual.weekday()])

if __name__ == '__main__':
    trabalhando_date()
    trabalhando_time()
    trabalhando_datetime()
#вариант 19
#организовать вывод номеров рейса, отправляющихся из заданного пунтка отправления
#и вывести список номеров рейсов у которых время в пути более 10 часов


class Avia:
    def __init__(self, num, departure, destination, time):
        self.num = num
        self.departure = departure
        self.destination = destination
        self.time = time
    
    def dep(self, per):
        if self.departure == per:
            print('Рейс под номером #'+self.num+" отправляется из "+per)
    def over_time(self):
        if self.time > 10:
            print('Рейс под номером #'+self.num+" летит "+str(self.time)+' часов, что более чем 10 часов')

per = input('Введите пункт отправления на русском: ')
tickets = [Avia('1', 'Москва', 'Нью-Йорк', 9.9), 
           Avia('2', 'Огайо', 'Панама', 1.7), 
           Avia('3', 'Нью-Йорк', 'Нью-Джерси', 12),
           Avia('4', 'Нью-Йорк', 'Виктория', 38)
]

#функция для добавления в лист переменных
def dobavlenie():
    tickets.append(Avia(input("номер рейса: "), input('Город отправления: '), input('Город прибытия: '), int(input('Сколько лететь: '))))
    return tickets

#цикл для этого
while True:
    if input('Введите "123", если вы хотите выйти из цикла. Если хотите и дальше добавлять переменные нажмите Enter или другое сообщение: ') == '123':
        '\n'
        break
    dobavlenie()

#вызов всех методов в листе
for i in tickets:
    i.dep(per)
for i in tickets:
    i.over_time()

#вызов отдельной функции и для каких по индексу в листе
print('Выберите какой метод вы хотите выбрать:')
print('dep/over.')
print('Если не хотите вызывать какую-то функцию, то пишите "0".')
ab = input('писать сюда: ')

print('Напишите с каких до каких индексов в листе вы хотите выполнить свой метод через точку.', 'Если что вот столько всего переменных в листе: '+str(len(tickets)))
cd = input("сюда: ")

cd = cd.split()
for i in range(len(cd)):
    cd[i] = int(cd[i])


#цикл для этого
while True:
    if ab == '0':
       print('Ничего не произошло как и хотел :)')
       break
    elif ab == 'dep':
        for i in range(len(tickets)):
            if i >= cd[0] and i <= cd[1]:
                tickets[i].dep(per)
        break
    elif ab == 'over':
        for i in range(len(tickets)):
            if i >= cd[0] and i <= cd[1]:
                tickets[i].over_time()
        break

#вариант 19
#организовать вывод номеров рейса, отправляющихся из заданного пунтка отправления
#и вывести список номеров рейсов у которых время в пути более 10 часов
class avia:
    def __init__(self, num, departure, destination, time, per1):
        self.num = num
        self.departure = departure
        self.destination = destination
        self.time = time
        self.per1 = per1
    
    def dep(self):
        if self.departure == self.per1:
            print('Рейс под номером #'+self.num+" отправляется из "+self.per1)
    def over_time(self):
        if self.time > 10:
            print('Рейс под номером #'+self.num+" летит "+str(self.time)+' часов, что более чем 10 часов')

per = input('Введите пункт отправления на русском: ')
tickets = [avia('1', 'Москва', 'Нью-Йорк', 9.9, per), 
           avia('2', 'Огайо', 'Панама', 1.7, per), 
           avia('3', 'Нью-Йорк', 'Нью-Джерси', 12, per),
           avia('4', 'Нью-Йорк', 'Виктория', 38, per)
]


for i in range (len(tickets)):
    tickets[i].dep()
for i in range (len(tickets)):    
    tickets[i].over_time()
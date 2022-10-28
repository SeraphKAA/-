class Man(object):      #родительский класс
    def __init__(self, name, age, sved, voen_srok, kurs) -> None:
        self.name = name
        self.age = age
        self.sved = sved
        self.voen_srok = voen_srok
        self.kurs = kurs

class Young_man(Man):       #класс молодой человек
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info1(self):
        return 'Я - {}, мне {} лет.'.format(self.name, self.age)

class Student(Man):         #класс студент
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info2(self):
        return 'Я - {}, мне {}, учусь на {} курсе.'.format(self.name, self.age, self.kurs)

class Voen(Man):        #класс военник
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info3(self):
        return 'Я - {}, мне {}, мой военный срок составляет {} год(а).'.format(self.name, self.age, self.voen_srok)

class Voen_kurs(Man):       #класс военный курс
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info4(self):
        return 'Я - {}, мне {}. \nМои военные сведения следующие:\n{}'.format(self.name, self.age, self.sved)

class Obsh(Young_man, Student, Voen, Voen_kurs): #класс, в к-ом обобщаются все классы
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def pas(self):
        pass


def proga():
    while True:
        x = input('\nНапиши 4 если ты хочешь вывести военные сведения: ')
        if x == '4':
            return print(X.sved)
        else:
            print('Ты ввел не правильное слово(')


if __name__ == '__main__':
    X = Obsh('Кизогян Арман Аргамович', '18', 'Какаха', '1', '2')
    print(X.info1())
    print(X.info2())
    print(X.info3())
    print(X.info4())
    proga()    

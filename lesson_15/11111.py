class Soda():
    def __init__(self,dob=None):
        self.dob=dob
        if self.dob!=None:
            if isinstance(self.dob, str)==True:
                pass
            else:
                print('Добавка должна быть строкой')
                self.dob=input(f'Введите добавку вместо: {self.dob }')
  
    def show_my_drink(self):
        if self.dob!=None:
               print(f'Газировка и {self.dob}')
        else:
            print('Обычная газировка')


sprait=Soda('laim')
proverka=Soda(123)
bonakva=Soda()
sprait.show_my_drink()
bonakva.show_my_drink()
proverka.show_my_drink()
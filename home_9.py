from russian_names import RussianNames
import openpyxl 
import random
from random import randint
number = randint(0,15)

def person() -> tuple[str, str, str]:
    rn = RussianNames()
    person_tuple = rn.get_person().split(' ')
    return person_tuple    

def person():
    person = RussianNames(count = int(number), output_type = 'list').get_batch()
    print(person)
    person_list = list(person)
    print(person_list)
    wb = openpyxl.Workbook()
    ws = wb.active
    for i in person_list:
        ws.append(i)
    wb.save('people.xlsx')
    wb.close()
        

if __name__ == '__main__':
    person()
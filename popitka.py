import openpyxl 

from russian_names import RussianNames

number = input('введите число')

def person() -> tuple[str, str, str]:
    rn = RussianNames()
    person_tuple = rn.get_person().split(',')
    return person_tuple   

def example():
    number1 = int(number)
    person = list (RussianNames(count = number1, output_type = 'list').get_batch())
    print(person)
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in person:
        ws.append(row)
    wb.save("people.xlsx")
    wb.close()


    
if __name__ == '__main__':
    rn = RussianNames()
    person2 = RussianNames(count = 2).get_batch()
    print(person2)
   
  
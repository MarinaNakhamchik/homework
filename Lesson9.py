from abc import ABC, abstractmethod
import csv
import openpyxl

CellValue = str | int | float


class TableReader(ABC):
    @abstractmethod 
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def read (self) -> list[list[CellValue]]:
        pass


class CSVTableReader(TableReader):
    def __init__(self, filename: str):
             self._filename = filename
        
    def read(self) -> list[list[CellValue]]:
        with open(self._filename,'r') as fd:
            csvreader = csv.reader(fd)
            data = [row for row in csvreader]
        return data
         
class EXALETableReader(TableReader):
    def __init__(self, filename: str):
        self.filename = filename
    def read(self) -> list[list[CellValue]]:
        wb = openpyxl.load_workbook('example.xlsx')
        ws = wb.active 
        i = 1
        while True:
            row = [cell.value for cell in ws[f'A{i}:I{i}']]
            
    

    
        



if __name__ == "__main__": 
    reader = CSVTableReader('output.csv')
    content_csv = reader.read()
    print(content_csv)

    reader = EXALETableReader('example.xlsx')
    content_xlsx = reader.read()
    print(content_xlsx)
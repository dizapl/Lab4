

from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str

@dataclass
class MoveOfMainAssets:
    code: int 
    course1: float
    course2: float
    course3: float
    course4: float
    course5: float
    course6: float
    year: int

type_array = []
type_array.append(TypeOfMainAssets(110,"ІНКО"))
type_array.append(TypeOfMainAssets(120,"АЖІО"))
type_array.append(TypeOfMainAssets(130,"Градобанк"))
type_array.append(TypeOfMainAssets(140,"Відродження"))
type_array.append(TypeOfMainAssets(150,"Укрінбанк"))

move_array = []
move_array.append(MoveOfMainAssets(110, 4.5, 5.4, 6.3, 3.4, 3.45, 4, 2003))
move_array.append(MoveOfMainAssets(120, 4, 5, 7.5, 2.7, 3.4, 4.78, 2003))
move_array.append(MoveOfMainAssets(130, 3.9, 5.1, 8, 2.74, 3.32, 5.03, 2003))
move_array.append(MoveOfMainAssets(140, 4.2, 5, 7, 2.459, 3.252, 4.8, 2003))
move_array.append(MoveOfMainAssets(150, 4.5, 5.1, 7.7, 3.169, 3.312, 4.8, 2003))
move_array.append(MoveOfMainAssets(110, 6.5, 6.8, 7, 4.5, 4.7, 4.8, 2004))
move_array.append(MoveOfMainAssets(120, 7.9, 8, 8.1, 5.1, 5.2, 5.3, 2004))
move_array.append(MoveOfMainAssets(130, 8.25, 8.33, 8.5, 5.3, 5.34, 5.38, 2004))
move_array.append(MoveOfMainAssets(140, 8.27, 8.3, 8.52, 5.28, 5.3, 5.35, 2004))
move_array.append(MoveOfMainAssets(150, 8.3, 8.31, 8.5, 5.28, 5.3, 5.35, 2004))
move_array.append(MoveOfMainAssets(110, 8.1, 8.4, 9, 5.1, 5.11, 5.2, 2005))
move_array.append(MoveOfMainAssets(120, 8.2, 8.35, 8.55, 5.4, 5.48, 5.5, 2005))
move_array.append(MoveOfMainAssets(130, 8.7, 8.78, 8.82, 5.45, 5.5, 5.55, 2005))
move_array.append(MoveOfMainAssets(140, 8.68, 8.8, 8.85, 5.46, 5.5, 5.55, 2005))
move_array.append(MoveOfMainAssets(150, 8.65, 8.8, 8.84, 5.46, 5.52, 5.56, 2005))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Курс обміну валют для приватних осіб"
    with names and values'''
    print("Код банку: {code}, Долари США: курс на 1.10: {course1}, курс на 1.11: {course2}, курс на 1.12: {course3}; Марки ФРН: курс на 1.10: {course4}, курс на 1.11: {course5}, курс на 1.12: {course6}; Рік: {year} "
      .format(code=moveOfMainAssets.code, course1=moveOfMainAssets.course1, course2=moveOfMainAssets.course2, course3=moveOfMainAssets.course3, course4=moveOfMainAssets.course4, course5=moveOfMainAssets.course5, course6=moveOfMainAssets.course6, year=moveOfMainAssets.year))
      
for data in move_array:
    printMoveOfMainAssets(data)
    
def printTypeOfMaininAssets(typeOfMainAssets):
    '''printTypeOfMaininAssets function prints
    "Довідник ринків"
    with names and velues'''
    
    print("Код: {code}, Найменування: {name}"
    .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name))
    
for data in type_array:
    printTypeOfMaininAssets(data)
    
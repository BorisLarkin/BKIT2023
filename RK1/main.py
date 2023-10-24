# используется для сортировки
from operator import itemgetter

#Язык программирования - средство разработки
class Lang:
    """ЯП"""
    def __init__(self, id, name, ver):
        self.id = id
        self.ver = ver
        self.name = name


class IDE:
    """Средство разработки"""
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year


class Lang_IDE:
    """
    'Языки, поддерживаемые IDE' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, l_id, ide_id):
        self.l_id = l_id
        self.ide_id = ide_id


# Languages
langs = [
    Lang(1, 'Python', '3.11'),
    Lang(2, 'C#', '11'),
    Lang(3, 'C', 'C17'),

    Lang(11, 'C++', 'C++20'),
    Lang(22, 'JavaScript', ),
    Lang(33, ''),
]


# Сотрудники
emps = [
    Emp(1, 'Артамонов', 25000, 1),
    Emp(2, 'Петров', 35000, 2),
    Emp(3, 'Иваненко', 45000, 3),
    Emp(4, 'Иванов', 35000, 3),
    Emp(5, 'Иванин', 25000, 3),
]


emps_deps = [
    EmpDep(1,1),
    EmpDep(2,2),
    EmpDep(3,3),
    EmpDep(3,4),
    EmpDep(3,5),


    EmpDep(11,1),
    EmpDep(22,2),
    EmpDep(33,3),
    EmpDep(33,4),
    EmpDep(33,5),
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим 
    one_to_many = [(e.fio, e.sal, d.name) 
        for d in deps 
        for e in emps 
        if e.dep_id==d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id) 
        for d in deps 
        for ed in emps_deps 
        if d.id==ed.dep_id]
    
    many_to_many = [(e.fio, e.sal, dep_name) 
        for dep_name, dep_id, emp_id in many_to_many_temp
        for e in emps if e.id==emp_id]


    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in deps:
        # Список сотрудников отдела
        d_emps = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если отдел не пустой        
        if len(d_emps) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _,sal,_ in d_emps]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))


    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in deps:
        if 'отдел' in d.name:
            # Список сотрудников отдела
            d_emps = list(filter(lambda i: i[2]==d.name, many_to_many))
            # Только ФИО сотрудников
            d_emps_names = [x for x,_,_ in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_emps_names


    print(res_13)


if __name__ == '__main__':
    main()

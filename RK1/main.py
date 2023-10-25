# используется для сортировки
from operator import itemgetter

#Язык программирования - средство разработки
class Lang:
    """ЯП"""
    """share = market share, %"""
    def __init__(self, id, name, ver, share, ide_id):
        self.id = id
        self.ver = ver
        self.name = name
        self.market_share = share
        self.ide_id = ide_id


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
    Lang(1, 'Python', '3.11', 29.48, 2),
    Lang(2, 'C#', '11', 6.94,1),
    Lang(3, 'C', 'C17', 6.49,2),

    Lang(11, 'C++', 'C++20', 6.49,4),
    Lang(22, 'Java', 'Java SE 21', 17.18,5),
    Lang(33, 'GO', '1.21.3', 36.1,3),
]


# Сотрудники
IDEs = [
    IDE(1, 'Microsoft Visual Studio', 2023),
    IDE(2, 'Visual Studio Code', 2023),
    IDE(3, 'Komodo', 2022),
    IDE(4, 'IntelliJ IDEA', 2023),
    IDE(5, 'Eclipse', 2022),
]


IDEs_langs = [
    Lang_IDE(1,2),
    Lang_IDE(2,1),
    Lang_IDE(3,2),
    Lang_IDE(1,1),
    Lang_IDE(3,2),


    Lang_IDE(11,4),
    Lang_IDE(22,5),
    Lang_IDE(33,3),
    Lang_IDE(11,1),
    Lang_IDE(11,2),
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим 
    one_to_many = [(l.name, l.ver, i.name, i.year) 
        for l in langs 
        for i in IDEs
        if i.id==l.ide_id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(i.name, i.id, il.ide_id) 
        for i in IDEs 
        for il in IDEs_langs 
        if i.id==il.ide_id]
    
    many_to_many = [(e.fio, e.sal, dep_name) 
        for dep_name, dep_id, IDE_id in many_to_many_temp
        for e in IDEs if e.id==IDE_id]


    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in deps:
        # Список сотрудников отдела
        d_IDEs = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если отдел не пустой        
        if len(d_IDEs) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _,sal,_ in d_IDEs]
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
            d_IDEs = list(filter(lambda i: i[2]==d.name, many_to_many))
            # Только ФИО сотрудников
            d_IDEs_names = [x for x,_,_ in d_IDEs]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_IDEs_names


    print(res_13)


if __name__ == '__main__':
    main()

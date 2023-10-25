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
    Lang_IDE(2,2),


    Lang_IDE(11,4),
    Lang_IDE(22,5),
    Lang_IDE(33,3),
    Lang_IDE(11,1),
    Lang_IDE(11,2),
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим 
    one_to_many = [(l.name, l.ver, l.market_share, i.name, i.year) 
        for l in langs 
        for i in IDEs
        if i.id==l.ide_id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(i.name, i.year, il.l_id) 
        for i in IDEs 
        for il in IDEs_langs 
        if i.id==il.ide_id]
    
    many_to_many = [(i_name, i_year, l.name, l.ver, l.market_share) 
        for i_name, i_year, l_id in many_to_many_temp
        for l in langs if l.id==l_id]


    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(3))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все IDE
    for i in IDEs:
        # Список языков, поддерживаемых средой
        ide_langs = list(filter(lambda k: k[3]==i.name, one_to_many))
        # Если хотя бы один язык поддерживается 
        if len(ide_langs) > 0:
            # Доли рынка каждого языка IDE
            ide_market_shares = [share for _,_,share,_,_ in ide_langs]
            # Общая доля рынка поддерживаемых языков
            ide_ms_sum = sum(ide_market_shares)
            res_12_unsorted.append((i.name, ide_ms_sum))


    # Сортировка по суммарной доле рынка
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все IDE
    for i in IDEs:
        if 'Visual Studio' in i.name:
            # Список языков IDE
            i_langs = list(filter(lambda k: k[0]==i.name, many_to_many))
            # Только названия языков 
            i_langs_names = [x for _,_,x,_,_ in i_langs]
            # Добавляем результат в словарь
            # ключ - IDE, значение - список языков
            res_13[i.name] = i_langs_names


    print(res_13)


if __name__ == '__main__':
    main()

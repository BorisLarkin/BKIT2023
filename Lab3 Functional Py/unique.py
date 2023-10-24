# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs:
            ignore_case = kwargs['ignore_case']
        else:
            ignore_case = False
        self.collection = []
        self.cursor = 0
        for item in items:
            if ignore_case:
                if (item not in self.collection):
                    self.collection.append(item)
            else:
                for x in self.collection:
                    if (item.lower() == x.lower()):
                        break
                else:
                    self.collection.append(item)
        pass

    def __next__(self):
        self.cursor+=1
        if self.cursor <= len(self.collection):
            return self.collection[self.cursor-1]
        raise StopIteration

    def __iter__(self):
        return self

def main():
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data, ignore_case = True)))
    return 

if __name__ == "__main__":
    main()

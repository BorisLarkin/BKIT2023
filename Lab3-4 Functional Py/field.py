def field(items, *args):
    assert len(args) > 0, 'Empty parameter sweep'
    for item in items:
        if len(args)==1:
            yield item[args[0]]
        else:
            line = {}
            for arg in args:
                if arg in item:
                    line[arg] = item[arg]
            yield line

def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]
    print(list(field(goods,'title', 'price')))
    return 

if __name__ == "__main__":
    main()
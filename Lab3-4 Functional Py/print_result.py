def print_result(func):
    def format(*arg):
        print('\n'+func.__name__, ':')
        output = func(*arg)
        if type(output) is list:
            for item in output:
                print(item)
        elif type(output) is dict:
            for key, value in output.items():
                print(str(key) + ' = ' + str(value))
        else:
            print(output)
        return output

    return format

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()    
from random import randint
def gen_random(num_count, begin, end):
    assert num_count != 0, 'Empty generator'
    for iteration in range(num_count):
        yield randint(begin,end)


def main():
    print(list(gen_random(5,1,3)))
    return 

if __name__ == "__main__":
    main()

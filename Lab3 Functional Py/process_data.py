import json 
from pathlib import *
from sys import *
from cm_timer import *
from field import *
from gen_random import *
from print_result import *
from sort import *
from unique import *
import os

with open('data_light.json', 'r') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    raise NotImplemented


@print_result
def f2(arg):
    raise NotImplemented


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented

def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == '__main__':
    main()
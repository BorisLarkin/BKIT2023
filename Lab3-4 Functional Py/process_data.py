import json 
from pathlib import *
from sys import *
from cm_timer import *
from field import *
from gen_random import *
from print_result import *
from sort import *
from unique import *

with open('data_light.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique([s['job-name'] for s in arg], ignore_case = True)))


@print_result
def f2(arg):
    return list(filter(lambda s: (s.lower().startswith("программист")), arg))


@print_result
def f3(arg):
    return [(s + " с опытом Python") for s in arg]


@print_result
def f4(arg):
    return list([(s +', зарплата ' + str(list(gen_random(1,100000,200000))[0])) for s in arg])

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
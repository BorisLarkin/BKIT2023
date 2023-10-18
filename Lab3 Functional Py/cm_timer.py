from time import *
from contextlib import contextmanager

class cm_timer_1():
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.start
        self.read = f'CMT1. Time elapsed: {self.time:.3f} seconds'
        print(self.read)

@contextmanager
def cm_timer_2():
    start = perf_counter()
    yield lambda: perf_counter() - start
    print(f'CMT2. Time elapsed: {perf_counter() - start:.3f} seconds')

def main():
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)

if __name__ == "__main__":
    main()
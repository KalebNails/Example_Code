#THIS CODE COMES DIRECTLY FROM: https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
#It's here for convience, I was going to make my own decorator that measure how long a function took,
#But after starting to read decorator documentation I immiedately found a better version of what I wanted

from functools import wraps
import tracemalloc
from time import perf_counter


def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper

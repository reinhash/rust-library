import time
from functools import wraps

import rust_library


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        retval = func(*args, **kwargs)
        print(f"the function took {time.time()-start_time} seconds")
        return retval
    return wrapper

@timer
def get_rust_array():
    return rust_library.big_calculation()

@timer
def get_python_array():
    return [x for x in range(1_000_000)]


get_rust_array() # the function took 0.08529520034790039 seconds
get_python_array() # the function took 0.041697025299072266 seconds

# turns out python is faster for such a task.

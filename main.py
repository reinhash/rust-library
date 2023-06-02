"""
Developed with maturin.

to compile the rust code, run:
    maturin develop
"""
import time

import rust_library

ELEMENTS = 1000 # around 1000, python and rust seem to be the same speed.

def timer(name):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            retval = func(*args, **kwargs)
            print(f"{name}: the function took {time.time()-start_time} seconds")
            return retval
        return wrapper
    return decorator_function

@timer('rust')
def get_rust_array():
    return rust_library.big_calculation(ELEMENTS)

@timer('python')
def get_python_array():
    _ = [x for x in range(ELEMENTS)]
    return


for element in range(ELEMENTS):
    print(f"Running with size: {element}")
    get_rust_array()
    get_python_array()


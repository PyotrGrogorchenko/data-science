import time


def execution_time(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        finish_time = time.time()
        print(f'Execution time: {(finish_time - start_time) * 10**3} ms')
        return res

    return wrapper


@execution_time
def a_plus_b(a, b):
    return a + b


@execution_time
def a_minus_b(a, b):
    return a - b


print(a_plus_b(2, 2))
print(a_minus_b(2, 2))

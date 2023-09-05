def int_only(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        if not isinstance(res, int):
            raise ValueError('Invalid result')
        return res
    return wrapper


@int_only
def good_val():
    return 5


@int_only
def bad_val():
    return '5'


print(good_val())

try:
    print(bad_val())
except Exception as ex:
    print(ex)


try:
    print(bad_val())
except ValueError as ex:
    print(ex)

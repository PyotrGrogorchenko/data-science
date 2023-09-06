def call_again(fn):
    def wrapper(*args, **kwargs):
        res = None
        try:
            res = fn(*args, **kwargs)
        except:
            res = fn(*args, **kwargs)
        return res

    return wrapper


@call_again
def division_by_zero():
    return 5/0


@call_again
def five_plus_five():
    return 5 + 5


print(five_plus_five())
try:
    print(division_by_zero())
except Exception as ex:
    print(ex)

def get_capital_letter(val):
    return val[0].capitalize()


def acronym(sentence):
    if not type(sentence) is str:
        raise Exception('Invalid type')
    return ''.join(map(get_capital_letter, sentence.split()))


print(acronym('one two three'))
print(acronym(''))
print(acronym(123))
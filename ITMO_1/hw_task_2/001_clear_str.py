
def clear_str(s):
    stop_words = ['Python', 'php', 'go', 'C']
    return ''.join(filter(lambda x: x not in stop_words, s.split(' ')))


print(clear_str(''))
print(clear_str('javaScript Python go'))
print(clear_str('C javaScript go'))
print(clear_str('javaScript C php'))

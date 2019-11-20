import string
import re

list = [1, 2, 3, 4, 5, 6, 7, 8]

print(list[3::-2])


states = ['   fds', 'fda!fds', 'fdsa  ,b']


def remove_punctuation(value):
    return re.sub('[!,]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []

    for string in strings:
        for function in ops:
            value = function(string)
        result.append(value)

    return result


print(clean_strings(states, clean_ops))



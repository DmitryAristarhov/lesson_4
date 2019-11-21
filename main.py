# 1. Напишите функцию (F):
# на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random).

from random import choice
def F(N, *args):
    return [choice(args) for i in range(N)]

print(F(3, 'aaaaaaa', 'bbbbbbbbb', 'ccccccccccc', 'dddddddd', 'eee', 'fffffffff'))

lst = ['0000000', '11111111', '22222222222', '3333333', '44444444', '555555555', '666666666666', '777777777', '88888888888',
       '9999', '000', '111111', '222222', '3333333', '444', '555555555', '666666', '77777777', '88888', '9999999999']
print(len(lst), F(100, *lst))

print()
###############################################################################
# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F.

from collections import Counter
def max_count(lst):
    count = Counter(lst)
    return max(count, key = lambda x: count[x])

l = F(100, *lst)
print(l)
print(Counter(l))
print(max_count(l))
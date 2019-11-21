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
print(*Counter(l).most_common(1)) # Можно было без max() в функции max_count(lst) обойтись оказывается ;)
print(Counter(l).most_common(1)[0][0])

print(max_count(l))

print()
#########################################################################################################
# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

def rare_letter(lst):
    lst = map(lambda x: x[0], lst)  # 'Список' из первых букв
    return Counter(lst).most_common()[-1:][0][0]

print(rare_letter(l))
l += ['xxxxxxxxx'] # Добавим редкую букву)
print(rare_letter(l))
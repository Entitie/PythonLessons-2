# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

n = int(input('Введите целое двухзначное число = '))
list21 = []

# a)

for _ in range(n * 3):
    list21.append(random.randint(-n, n))
print(list21)
set_list = set(list21)
print(set_list)

# б)

or_list = []
for k in list21:
    if list21.count(k) == 1:
        or_list.append(k)
print(or_list)

# d_list = []
# for _ in list21:
#     i = list21.count(_) + 1
#     while i >= len(list21):
#         if _ == list21[i]:
#             list21.pop(i)
#         else:
#             i += 1
# print(list21)
# sd_list = set(d_list)
# final_list = set_list - sd_list
# print(final_list)

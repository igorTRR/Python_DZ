### Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list =[]
for i in range(10):
    list.append(random.randint(-5,5))
print(*list)

min = int(input('Введите минимальное число: '))
max = int(input('Введите максимальное число: '))

for i in range(len(list)):
    if min <= list[i] <= max:
      print(i)   
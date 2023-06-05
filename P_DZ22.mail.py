# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
import tempfile


n = int(input('Введите количество элементов первого набора чисел: '))
m = int(input('Введите количество элементов второго набора чисел: '))
arr1 = []
arr2 = []
for i in range(n):
     arr1.append(random.randint(0,10))
print (arr1)  
  
for j in range(m):
     arr2.append(random.randint(0,10))
print (arr2) 
x = int(input('Введите число x: ')) 

count1 =0
count2 = 0

for i in range(len(arr1)):
    if arr1[i]== x:
        count1+=1

for j in range(len(arr2)):
    if arr2[j] == x:
        count2+=1      
print(f'Число вхождений {x} в arr1  = {count1}')
print(f'Число вхождений {x} в arr2  = {count2}')
    
 
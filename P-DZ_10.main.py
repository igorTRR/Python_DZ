    # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, кото    рые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import collections
import random
m =[1, 0, 1, 1, 0 ] # const- hard cod

    # num_ coins -к-во монет
    # coins - список монет
    
num_coins = 5     #int(input('Введите кол монет:'))  
coins = []

for i in range(num_coins):
    coins.append(random.randint(0, 1))
print(coins)

avers = coins.count(0)
revers = coins.count(1)
print('avers',{avers}, 'revers',{revers})
 

if avers < revers:
        print('перевернуть avers' ,  {avers} )
else:
    print('перевернуть revers', {revers})
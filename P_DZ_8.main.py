    # Задача 8: Требуется определить, можно ли от шоколадки размером n
    # × m долек отломить k долек, если разрешается сделать один разлом по
    # прямой между дольками (то есть разломить шоколадку на два
    # прямоугольника).

n = int(input('Введите колличество долек размером n: ')) 
m = int(input('Введите колличество долек размером m: ')) 

k = int(input('Введите колличество долек которые надо отломить : ')) 

if (n*m > k) and (k % n == 0 or k % m == 0):
    print('Yes, можно разломить')
else: 
      print('No,  разломить нельзя') 


# Задача 6: Вы пользуетесь общественным транспортом? 
    #  Счастливым билетом называют такой билет с шестизначным номером, где сумма
    # первых трех цифр равна сумме последних трех. Т.е. билет с номером
    # 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
    # программу, которая проверяет счастливость билета.

  
TicetNub = input('Введите номер билета: ')
if len(TicetNub ) == 6:
    if sum(map(int,TicetNub[:3])) == sum(map(int,TicetNub[3:])):
             print('YES!, Счастье привалило!!!')
    else:
        print('NO, Может в следующий раз...') 
    
else:
    len(TicetNub ) !=6
    print('Error набора')    
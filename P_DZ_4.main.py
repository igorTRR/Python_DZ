# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?


Sum = int(input('Введите количество журавликов n: '))

if (Sum%2) == 0:
    Kt = (Sum//3)*2
    Pt = (Sum - Kt)//2
    Sr = Pt
    print(Kt, Pt, Sr)
else:
    if (Sum%2) != 0:
        Kt = (Sum//3)*2
        Pt = (Sum - Kt)//2
        Sr = Pt
    print(Kt, Pt, Sr)
    print('+ 1 Жура улетел')








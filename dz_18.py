# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 6
# -> 5


N = int(input('Введите количество элементов списка А: '))
if N < 1:
    print('Не корректное число. Введите любое число, начиная с 1')
else:
    A = input("Введите через пробел элементы списка A: ").split()
    num = list(map(int, A))
    if len(num) != N:
        print(f'Количество введённых элементов отличается от заявленного: {N}')
    else:
        X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
        j = abs(X - num[0])
        index = 0
        for i in range(1, N):
            count = abs(X - num[i])
            if count < j:
                j = count
                index = i
        print(f'Число {num[index]} наиболее близкое к числу {X}, их разница составляет {abs(X - num[index])}')

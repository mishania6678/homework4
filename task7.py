import math


def fact(num):
    for i in range(1, num + 1):
        yield math.factorial(i)


n = int(input('Введите n:'))
for el in fact(n):
    print(el)


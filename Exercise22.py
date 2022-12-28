'''
Câu 22. Với một số nguyên dương N thoả mãn 0<N<10000, đặt:
F ( N ) = N nếu N là một số nguyên tố
F ( N ) = 0 nếu là hợp số
Cho L và R nhập vào từ bàn phím, với mọi cặp i , j trong
khoảng [ L , R ] hãy viết chương trình
in ra màn hình giá trị tổng của F ( i ) * F ( j ) với j > i.
'''
import random


def square_integer(a, r, n):
    k = []
    while r > 0:
        k.append(r % 2)
        r //= 2
    temp = a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        temp = (temp * temp) % n
        if k[i] == 1:
            b = (b * temp) % n
    return b


def miller_rabin(n, t):  # dùng miller để xét nguyên tố
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    s = 0
    x = n - 1
    while x % 2 == 0:
        s += 1
        x //= 2
    r = x
    for i in range(1, t + 1):
        a = random.randint(2, n - 2)
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = y ** 2 % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True


def result(number_l, number_r):
    sum = 0
    for i in range(number_l, number_r):
        if miller_rabin(i, i):
            Fi = i
        else:
            Fi = 0
        for j in range(i + 1, number_r + 1):
            if miller_rabin(j, j):
                Fj = j
            else:
                Fj = 0
            sum += (Fi * Fj)
    return sum


if __name__ == '__main__':
    number_l = int(input('Nhập số L = '))
    number_r = int(input(f'Nhập số R > {number_l} = '))
    if number_r > number_l:
        print(result(number_l, number_r))
    else:
        print('Thử Lại')

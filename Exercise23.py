'''
Câu 23. Viết chương trình in ra màn hình YES trong trường hợp tổng
của các số nguyên tố trong khoảng [A, B] là cũng là một số nguyên tố
và NO nếu ngược lại. Với A,B là hai số được nhập vào từ bàn phím.
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


def sum(number_a, number_b):
    value = 0
    for i in range(number_a, number_b + 1):
        if miller_rabin(i, i):
            value += i
    return value


if __name__ == '__main__':
    number_a = int(input('Nhập số a = '))
    number_b = int(input('Nhập số b = '))
    s = sum(number_a, number_b)
    if miller_rabin(s, s):
        print('YES')
    else:
        print('NO')

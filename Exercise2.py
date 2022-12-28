"""
Câu 2. Viết chương trình tìm các số nguyên tố có N chữ số với N nhập từ bàn phím và 2 ≤ N ≤
10
"""
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


if __name__ == '__main__':
    number_n = int(input())
    if number_n >= 2 and number_n <= 10:
        for i in range(int(10 ** (number_n - 1)), 10 ** number_n):
            if i % 2 != 0 or i == 2:
                if miller_rabin(i, i):
                    print(i)
    else:
        print("Vui lòng nhập 2 <= n <= 10")

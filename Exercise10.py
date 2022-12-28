"""
Câu 10. Viết chương trình đếm số ước và
 số ước nguyên tố của một số N nhập vào từ bàn phím. ( đã tối ưu)
"""
import math
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


def divisor(n):
    d = [1, n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n / i == i:
            d.append(i)
            break
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d


if __name__ == '__main__':
    n = int(input('Nhập số n = '))
    d = divisor(n)
    count_prime = 0
    for i in range(0, len(d)):
        if d[i] % 2 != 0 or d[i] == 2:
            if miller_rabin(d[i], d[i]):
                count_prime += 1
    print(d)
    print(f'Số ước = {len(d)}')
    print(f'Số ước nguyên tố = {count_prime}')

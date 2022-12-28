"""
Câu 3. Cho một số nguyên dương N, gọi:
- k là số ước nguyên tố của N;
- q là tổng của các ước nguyên tố của N;
- p là tổng của các ước số của N;
- s là số ước của N;
Hãy viết chương trình tính giá trị của: N+p+s-q-k với N cho trước nhập từ bàn phím.
Ví dụ: N=24, có các ước là {1,2,3,4,6,8,12, 24} do đó:
p=1+2+3+4+6+8+12+24=60 và s=8
trong đó có 2 ước nguyên tố là {2,3} do đó:
q=2+3=5 và k=2
Và từ đó: N+p+s-q-k = 24+60+8-5-2=85;
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


def divisor_prime(d):
    p = []
    for i in d:
        if i %2 != 0 or i == 2:
            if miller_rabin(i, i):
                p.append(i)
    return p


def sum_divisor_prime(p):
    s = 0
    for e in p:
        s += e
    return s


def sum_divisor(d):
    s = 0
    for e in d:
        s += e
    return s


def divisor(n):
    d = [1, n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n / i == i:
            d.append(i)
            break
        if n % i == 0:
            d.append(i)
            d.append(int(n / i))
    return d


if __name__ == '__main__':
    n = int(input())
    d = divisor(n)
    num_prime = divisor_prime(d)
    k = len(num_prime)  # so uoc nt
    q = sum_divisor_prime(num_prime)  # tong ước nguyên tố
    p = sum_divisor(d)  # tổng ước
    s = len(d)
    print(n + p + s - q - k)

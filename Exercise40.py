'''
Câu 40. Cho mảng A nhập từ bàn phím gồm các số nguyên dương. Hãy viết chương trình đếm
các cặp số (i,j) trong mảng A sao cho ước chung lớn nhất của chúng là một số nguyên tố
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


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    count = 0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            r = gcd(A[i], A[j])
            if r % 2 != 0 or r == 2:
                if miller_rabin(r, r):
                    count += 1
    print(count)

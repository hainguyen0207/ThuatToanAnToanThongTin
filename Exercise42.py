'''
Câu 42. Viết chương trình sinh ra 2 số nguyên tố 0<p,q<1000 và kiểm tra với với số 0<a<100 thì
liệt kê những số a thoả mãn: a^p mod q là số nguyên tố.
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


def random_number():
    while True:
        n = random.randint(1, 1000)
        if n % 2 != 0 or n == 2:
            if miller_rabin(n, n):
                return n


if __name__ == '__main__':
    p = random_number()
    q = random_number()
    print(p)
    print(q)
    for a in range(2, 100):
        b = square_integer(a, p, q)
        if miller_rabin(b, b):
            print(f'{a}:{b} ', end=" ")

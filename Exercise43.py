'''
Câu 43. Cho N nhập vào từ bàn phím (0<N<1000), sinh một số nguyên tố p<100. Hãy viết
chương trình tìm tất cả các số nguyên a<N sao cho a^p mod N là số nguyên tố
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
        n = random.randint(2, 100)
        if miller_rabin(n, n):
            return n


if __name__ == '__main__':
    p = random_number()
    n = int(input('Nhập n = '))
    print(p)
    for a in range(2, n):
        b = square_integer(a, p, n)
        if miller_rabin(b, b):
            print(f'{a}:{b} ', end=" ")

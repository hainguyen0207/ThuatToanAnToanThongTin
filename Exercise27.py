'''
Câu 27. Viết chương trình in ra các cặp số (a,b) thoả mãn điều kiện 0<a,b<1000,
sao cho ước chung lớn nhất của 2 số đó là một số nguyên tố.
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


def result(a, b):
    list_result = []
    for i in range(a + 1, b):
        for j in range(a + 1, b):
            r = gcd(i, j)
            if r % 2 != 0 or r == 2:
                if miller_rabin(r, r):
                    list_result.append({(i, j): gcd(i, j)})
    return list_result


if __name__ == '__main__':

    a = int(input('Nhập số a = '))
    b = int(input(f'Nhập số b > {a} = '))
    if a <= b:
        print(result(a, b))
    else:
        print('a b không hợp lệ !')

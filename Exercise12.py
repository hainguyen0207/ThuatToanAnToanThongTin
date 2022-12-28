"""
Câu 12. Viết chương trình tìm bốn số nguyên tố liên tiếp,
 sao cho tổng của chúng là số nguyên tố
nhỏ hơn hoặc bằng N (với N được nhập vào từ bàn phím).( đã tối ưu)
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


def sum_sub(sub):
    s = 0
    for e in sub:
        s += e
    return e


def list_number_prime(n):
    p = [2]
    for i in range(3, n, 2):
        if miller_rabin(i, i):
            p.append(i)
    return p


if __name__ == '__main__':
    number_n = int(input("Nhập n = "))
    if number_n < 17:
        print("NO")
    else:
        i = 0
        p = list_number_prime(int(number_n / 2))
        while i + 4 <= len(p):
            sub = p[i:i + 4]
            s = sum_sub(sub)
            if s % 2 != 0 and miller_rabin(s, s) or s == 2:
                print(sub)
            i += 1

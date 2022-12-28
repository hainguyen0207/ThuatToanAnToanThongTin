"""
Câu 17. Viết chương trình tìm số nguyên dương x nhỏ nhất và nhỏ hơn N
 nhập từ bàn phím sao cho giá trị của biểu thức 𝐴𝑥2 + 𝐵𝑥 + 𝐶 là một số
 nguyên tố với A,B,C là các số nguyên nhập vào
từ bàn phím.
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


def expression(number_n, number_a,
               number_b, number_c):
    for x in range(1, number_n + 1):
        s = number_a * x * x + number_b * x + number_c
        if miller_rabin(s, s):
            return s, x
    return None


if __name__ == '__main__':
    number_n = int(input('Nhập n = '))
    number_a = int(input('Nhập a = '))
    number_b = int(input('Nhập b = '))
    number_c = int(input('Nhập c = '))
    r = expression(number_n, number_a,
                   number_b, number_c)
    if r != None:
        print(f'S = {r[0]}')
        print(f'X = {r[1]}')
    else:
        print('Không tồn tại số X')

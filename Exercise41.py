'''
Câu 41. Cho các số nguyên dương a,k,n, nhập từ bàn phím (0<a,k<n<1000), Viết chương trình
xác định xem a^k mod n có phải là một số nguyên tố hay không
(sử dụng thuật toán bình phương và nhân có lặp)?
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


if __name__ == '__main__':
    number_a = int(input('Nhập số a > 0 = '))
    number_k = int(input('Nhập k = '))
    number_n = int(input(f'Nhập n > {number_k} = '))
    b = square_integer(number_a, number_k, number_n)
    if miller_rabin(b,b) and b % 2 != 0 or b == 2:
        print('YES')
    else:
        print('NO')

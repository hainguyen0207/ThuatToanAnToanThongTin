'''
Câu 24. Đặt S1, S2 là các mảng chứa giá trị bình phương của các số nguyên.
Hãy viết chương trình in ra số lượng tất cả các số nguyên tố nằm trong
 khoảng [a,b] sao cho số này cũng là tổngcủa hai số x và y với x thuộc
S1 và y thuộc S2. Trong đó, a,b là các số được nhập từ bàn phím
Ví dụ: với a=10, b =15, in ra giá trị là 1 vì trong khoảng [10,15]
chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có 13 = 2^2 + 3^2=4+9.

'''
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


if __name__ == '__main__':
    a = int(input('Nhập số a = '))
    b = int(input(f'Nhập số b >='))

    if b >= a:
        q = int(math.sqrt(b))
        for i in range(2, q + 1):
            for j in range(i, q + 1):
                if miller_rabin(i, i) and miller_rabin(j, j):
                    x = i * i + j * j
                    if miller_rabin(x, x) and x >= a and x <= b:
                        print(x)
    else:
        print('Thử Lại')

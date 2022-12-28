"""
Câu 15. Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên
tố hơn kém nhau 2 đơn vị.Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc
bằng N, với N được nhập vào từ bàn phím.
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


def twin_number(number_n):  # hiển thị kếtquar
    r = []
    for i in range(2, number_n - 1):  # duyệt 2 đến n
        if miller_rabin(i, i) and miller_rabin(i + 2, i + 2):
            r.append((i, i + 2))
    return r


if __name__ == '__main__':
    n = int(input('Nhập n = '))
    r = twin_number(n)
    if len(r) > 0:
        print(r)
    else:
        print('Không tồn tại ')

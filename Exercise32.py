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


def random_number_q():  # random 2-500 khi nào dduwjojc snt ngừng
    while True:
        q = random.randint(2, 500)  # 2 > q > 500
        if q % 2 != 0 or q == 2:
            if (miller_rabin(q, q)):
                return q


def random_number_p():  # random chọn 100-500 ,khi nào được snt ngừng
    while True:
        p = random.randint(100, 500)  # 100 < p < 500
        if p % 2 != 0 or p == 2:
            if (miller_rabin(p, p)):
                return p


def gcd(a, b):  # tìm ước chung ln
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def random_number_e(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if e % 2 != 0 or e == 2:
            if gcd(e, phi_n) == 1:
                return e


def calculator_d(a, b):  # tính nghịch đảo
    if b == 0:
        x = 1
        return x
    b1 = b
    x2 = 1
    x1 = 0
    while b > 0:
        q = int(a // b)
        r = a - q * b
        x = x2 - q * x1
        a = b
        b = r
        x2 = x1
        x1 = x
    x = x2
    return (x + b1) % b1


if __name__ == '__main__':
    q = random_number_q()
    p = random_number_p()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random_number_e(phi_n)
    d = calculator_d(e, phi_n)
    sbd = int(input("Nhập SBD = "))
    m = sbd + 123
    print(f'm = {m}')
    c = square_integer(m, e, n)  # bản mã
    print(f'Bản mã c = {c}')
    dec = square_integer(c, d, n)  # giải mã
    if dec != m:
        dec = dec + (m - m % n)
    print(f'Giải mã m= {dec}')

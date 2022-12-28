"""
Câu 14. Viết chương trình tìm số nguyên tố có ba chữ số,
biết rằng nếu viết số đó theo thứ tự ngược lại thì ta được
một số là lập phương của một số tự nhiên.
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


def number_reverse(number):
    n_reverse = 0
    while number > 0:
        r = number % 10
        n_reverse = n_reverse * 10 + r
        number = int(number / 10)
    return n_reverse


if __name__ == '__main__':
    min_number = 100
    max_number = 999
    i = int(100 ** 1 / 3)
    j = int(999 ** 1 / 3)
    for i in range(i, j + 1):
        reverse = number_reverse(i * i * i)
        if miller_rabin(reverse, reverse):
            print(reverse)

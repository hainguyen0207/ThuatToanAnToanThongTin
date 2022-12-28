'''
Câu 21. Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố
từ 1 đến X (ngoại trừ X) là một số nguyên tố. Hãy viết chương trình
đếm số lượng các siêu số nguyên tố này trong khoảng [A,B] cho trước
nhập từ bàn phím
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


def super_prime(number_a, number_b):
    result_list = []
    for x in range(number_a, number_b + 1):
        count = 0
        for i in range(1, x):
            if miller_rabin(i, i) and i % 2 != 0 or i == 2:
                count += 1
        if miller_rabin(count, count) and \
                count % 2 != 0 or count == 2:
            result_list.append(x)
    return result_list


if __name__ == '__main__':
    number_a = int(input('Nhập số a = '))
    number_b = int(input(f'Nhập số b  > {number_a} =  '))
    if number_b >= number_a:
        result = super_prime(number_a, number_b)
        print(result)
        print(f'Có {len(result)} số siêu nguyên tố')
    else:
        print('Thử Lại')

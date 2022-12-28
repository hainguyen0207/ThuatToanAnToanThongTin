'''
Câu 45. Viết chương trình sinh một mảng số nguyên tố A gồm N phần tử (N nhập từ bàn phím)
sử dụng kiểm tra Miller-Rabin. In ra mảng và tính khoảng cách nhỏ nhất giữa
2 số bất kỳ trong mảng.
'''
import random


def square_integer(number_a, number_k, number_n):
    k = []
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k //= 2
    a = number_a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


def miller_rabin(n, t):
    r = n - 1
    s = 0
    while r % 2 == 0:
        s += 1
        r //= 2
    k = 1
    for i in range(2, n - 2):
        a = i
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y * y) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
        if k >= t:
            break
        k += 1
    return True


def random_number_prime(t):
    while True:
        num = random.randint(2, 100)  # lấy 2 - 1000)
        if miller_rabin(num, t):
            return num


def find_min(A):
    A.sort()
    value = A[len(A) - 1]
    for i in range(len(A) - 1):
        small = A[i + 1] - A[i]
        if small < value:
            value = small
    return value


A = []
n = int(input('Nhập số luợng n = '))
t = 100  # mặc định tham số an toàn t = 100
for i in range(n):
    num = random_number_prime(t)
    A.append(num)
print(A)
value_min = find_min(A)
print(f'Khoảng cách nhỏ nhất 2 số là : {value_min}')

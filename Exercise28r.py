'''
Câu 28. Viết chương trình tìm các số Carmichael (là các số giả nguyên tố n
thoả mãn điều kiện là hợp số và thoả mãn 𝑏 ^𝑛−1 ≡ 1 (𝑚𝑜𝑑 𝑛) với mọi số
nguyên dương b nguyên tố cùng nhau với n) nhỏ hơn một số N cho trước nhập
vào từ bàn phím (với điều kiện 0 ≤ 𝑁 ≤ 10000.
'''
import math


def is_prime(number):
    if number < 2:
        return False
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True


def binary(number_k):
    k = []
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k = int(number_k // 2)
    k.reverse()
    return k


def square_integer(number_a, number_k, number_n):
    k = binary(number_k)
    k.reverse()
    a = number_a
    if k[0] == 1:
        b = number_a
    else:
        b = 1
    for i in range(1, len(k)):
        q = int(a * a % number_n)
        a = q
        if k[i] == 1:
            b = int(b * q % number_n)
    return b


def gcd(x, number_n):
    if number_n == 0:
        return x
    return gcd(number_n, x % number_n)


def check(i):
    for x in range(1, i):
        if gcd(x, i) == 1:
            if (square_integer(x, i - 1, i) != 1):
                return False
    return True


def number_carmichael(number_n):
    for i in range(31, number_n + 1, 2):
        if is_prime(i) == False:
            if check(i):
                print(i, end=" ")


number_n = int(input())
number_carmichael(number_n)

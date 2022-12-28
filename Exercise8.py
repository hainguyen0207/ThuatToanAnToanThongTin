"""
Câu 8. Một số gọi là số Т-prime nếu có có đúng 3 ước nguyên dương.
Viết chương trình tìm các số Т-prime nhỏ hơn hoặc bằng N với N
cho trước nhập từ bàn phím.
"""
import math


def number_t_prime(n):
    d = [1, n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n / i == i:
            d.append(i)
            break
        if n % i == 0:
            d.append(i)
            d.append(int(n / i))
    return len(d) == 3


if __name__ == '__main__':
    n = int(input('Nhập n = '))
    for i in range(1, n + 1):
        if number_t_prime(i):
            print(i, end=" ")

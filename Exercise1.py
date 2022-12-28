"""
Câu 1 Một số gọi là Q-prime khi nó có đúng 4 ước số nguyên dương. Hãy viết chương trình in ra
các số Q-Prime nhỏ hơn hoặc bằng một số N cho trước nhập từ bàn phím.
"""
import math


def q_prime(n):
    q = [1, n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n / i == i:
            q.append(i)
        if n % i == 0:
            q.append(i)
            q.append(int(i))
    return len(q) == 4


if __name__ == '__main__':
    number_n = int(input())
    result = []
    for i in range(1, number_n + 1):
        if q_prime(i):
            result.append(i)
    if len(result) > 0:
        for e in result:
            print(e)
    else:
        print("None")

'''
Câu 44. Cho mảng A gồm các số nguyên thuộc 𝐹𝑝 nhập vào từ bàn phím,
hãy viết chương trình in ra mảng B có các phần tử là nghịch đảo của
các phần tử tương ứng trong A.
'''


def inversion(a, b):
    if b == 0:
        x = 1
        return x
    b1 =b
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0:
        q = int(a // b)
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return (x2 + b1) % b1


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


p = int(input('P = '))
A = [int(x) for x in input().split()]
B = [0 for x in range(len(A))]

for i in range(0, len(A)):
    if gcd(A[i], p) == 1:  # gcd = 1 mới có nghịch đảo
        B[i] = inversion(A[i], p)
    else:
        B[i] = None
print(A)
print(B)

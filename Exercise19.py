"""
Câu 19. Viết chương trình in ra các số nguyên dương x
 nằm trong khoảng [m,l] sao cho giá trị của biểu thức 𝐴𝑥
2 + 𝐵𝑥 + 𝐶 là một số nguyên tố. Với A,B,C, m,l là các
số nguyên nhập từ bàn phím (m<l)
"""
import math


# sàng số nguyên to
def find_prime_number(l):
    num = {x: 1 for x in range(2, l + 1)}
    p = 2
    while p <= l:
        for i in range(p, l + 1):
            if p * i <= l and p * i in num:
                del num[p * i]
        p += 1
    return list(num)


def expression_prime(number_a, number_b,
                     number_c, m, l):
    result = []
    for x in range(m, l + 1):
        value = number_a * x * x + number_b * x \
                + number_c
        if value in find_prime_number(value):
            result.append(x)
    return result


number_m = int(input('Nhập số m = '))
number_l = int(input(f'Nhập số l > '
                     f'{number_m} = '))
if number_l > number_m:
    number_a = int(input('Nhập số a = '))
    number_b = int(input('Nhập số b = '))
    number_c = int(input('Nhập số c = '))
    result = expression_prime(number_a, number_b,
                              number_c, number_m, number_l)
    if len(result) > 0:
        print(result)
    else:
        print('Không tồn tại giá trị x nào !')
else:
    print('Thử lại !')

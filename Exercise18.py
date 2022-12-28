"""
Câu 18. Áp dụng thuật toán đã được học để viết chương trình tính
 tổng trên trường Fp của hai số nguyên lớn nhập vào từ bàn phím a và b
"""
import math


def array(number, t, W):
    list = []
    while t > 0:
        p = int(number // math.pow(2, W * (t - 1)))
        list.append(p)
        number = int(number % math.pow(2, W * (t - 1)))
        t -= 1
    return list


def value_array(array, t, W):
    sum = 0
    i = 0
    while t > 0:
        p = int(math.pow(2, W * (t - 1)) * array[i])
        sum += p
        t -= 1
        i += 1
    return sum


def multiprecision_subtraction(array_a, array_b, W, t):  # phép trừ chính xác bội
    remeber = 0  # biến nhớ
    c = [0] * t
    while t > 0:
        if array_a[t - 1] - array_b[t - 1] - remeber < 0:
            c[t - 1] = 256 + (array_a[t - 1] - array_b[t - 1] - remeber)
            remeber = 1
        else:
            c[t - 1] = (array_a[t - 1] - array_b[t - 1] - remeber) % 256
            remeber = 0
        t = t - 1
    return remeber, c


def multiprecision_addition(array_a, array_b, t, W):  # phép cộng chính xác bội
    array_c = [0] * t
    remeber = 0
    exp = int(math.pow(2, W))
    while t > 0:
        s = array_a[t - 1] + array_b[t - 1] + remeber
        array_c[t - 1] = s % exp
        if s > exp:
            remeber = 1
        else:
            remeber = 0
        t -= 1
    return remeber, array_c


def addition_Fp(r, t, W, P):
    remeber = r[0]
    c = r[1]
    if remeber == 1:
        p = array(P, t, W)
        x = multiprecision_subtraction(c, p, W, t)
        c = x[1]
    else:
        if value_array(c, t, W) >= P:
            c = array(value_array(c, t, W) - P, t, W)
    return c


if __name__ == '__main__':
    P = 2971215073
    m = 31
    W = 8
    t = 4
    a = int(input(f'Nhập số a <= {P - 1} : '))
    b = int(input(f'Nhập số b <= {P - 1} : '))
    if a >= 0 and a <= P - 1 and b > 0 \
            and b <= P - 1:
        array_a = array(a, t, W)
        array_b = array(b, t, W)
        r = multiprecision_addition(array_a, array_b, t, W)
        r_Fp = addition_Fp(r, t, W, P)
        print(r_Fp)
        print(value_array(r_Fp, t, W))
    else:
        print('a và b không hợp lệ ! Vui lòng nhập lại')

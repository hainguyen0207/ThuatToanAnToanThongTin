"""
Câu 6. Hai số tạo thành một cặp số thân thiết khi chúng tuân theo quy luật: Số này bằng tổng tất
cả các ước của số kia (trừ chính số đó) và ngược lại. Viết chương trình tìm hai số dạng này nhỏ
hơn N (với N nhập vào từ bàn phím). đã tối ưu

"""
import math


def divisor(a, b):
    s = 1
    for i in range(2, int(math.sqrt(a) + 1)):
        if a / i == i:
            s += i
            break
        if a % i == 0:
            s += i
            s += (a / i)
    return int(s) == b


def show_result(n):
    result_list = []
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            if divisor(i, j) and divisor(j, i):
                result_list.append((i, j))
    return result_list


if __name__ == '__main__':
    n = int(input('nhập n = '))
    print(show_result(n))

'''
Câu 20. Viết chương trình in ra các cặp số (A,B) nằm trong khoảng (M,N)
 sao cho ước số chung lớn nhất của A và B có giá trị là một số D cho
 trước. Với M,N,D nhập vào từ bàn phím. (0<M,N, D < 1000).
'''


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def result(m, n, d):
    list_result = []
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            if gcd(i, j) == d:
                list_result.append((i, j))
    return list_result


if __name__ == '__main__':
    m = int(input('Nhập số m > 0 = '))
    if m > 0:
        n = int(input(f'Nhập số n > {m} = '))
        if n > m:
            d = int(input('Nhập số d = '))
            if d <= n:
                output = result(m, n, d)
                print(output)
            else:
                print('Không tồn tại cặp nào')
        else:
            print('Vui Lòng thử lại ')
    else:
        print('Vui Lòng Thử Lại')

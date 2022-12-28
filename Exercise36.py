'''
Câu 36. Lập trình tìm kiếm xâu S1 trong xâu S2 theo thuật toán Boyer-Moore
'''


def last_occurrence(T, P):  # hàm ánh xạ L
    L = {}
    for i in range(len(P)):
        if P[i] not in L:
            for j in range(len(P)):
                if P[i] == P[j]:
                    value = j
            L[P[i]] = value
    for i in range(len(T)):
        if T[i] not in L:
            L[T[i]] = -1
    return L


def boyer_moore(T, P):
    L = last_occurrence(T, P)
    m = len(T)  # độ dài của chuỗi T
    y = len(P)  # độ dài của chuỗi P
    j = len(P) - 1
    i = len(P) - 1
    while True:
        if i >= m:
            return -1
        while T[i] == P[j]:
            i -= 1
            j -= 1
            if j + 1 == 0:
                return i + 2
        i = i + y - min(j, 1 + L[T[i]])
        j = y - 1


if __name__ == '__main__':
    T = input('Chuỗi T = ')
    P = input('Chuỗi P = ')
    index = boyer_moore(T, P)
    if index != -1:
        print(f'P xuất hiện trong T từ vị trí : {index}')
    else:
        print('P không tồn tại trong T')

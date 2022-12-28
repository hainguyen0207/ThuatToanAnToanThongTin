'''
Câu 37. Lập trình tìm kiếm xâu S1 trong xâu S2 theo thuật toán Knutt-Morris-Patt.
Trong trường hợp nào thì thuật toán Boyer-Moore được xem là cải tiến hơn
 thuật toán tìm kiếm vét cạn?
'''


def failure(P):
    F = {}
    F[0] = -1
    F[1] = 0
    for i in range(2, len(P)):
        prefix = []  # tiền đố
        suffixes = []  # hậu tố
        j = 1
        a = 1
        k = i
        while j <= i:
            prefix.append(P[0:j])
            suffixes.append(P[a:k])
            j += 1
            a += 1
        suffixes.reverse()
        suffixes.remove('')
        value = 0
        for x in range(i - 1):
            if prefix[x] == suffixes[x]:
                value = len(prefix[x])
        F[i] = value
    return F


def search_kmp(T, P):
    F = failure(P)
    i = 0
    j = 0
    while True:
        if j + i >= len(T):
            return -1
        while P[j] == T[i]:
            i += 1
            j += 1
            if j == len(P):
                return i - len(P) + 1
        i = i + j - F[j]
        if (F[j] == -1):
            j = 0
        else:
            j = F[j] + 1


if __name__ == '__main__':
    T = input('Nhập chuỗi T = ')
    P = input('Nhập chuỗi P = ')
    index = search_kmp(T, P)
    if index != -1:
        print(f'P xuất hiện trong T ở vị trí {index}')
    else:
        print('P không xuất hiện trong T')

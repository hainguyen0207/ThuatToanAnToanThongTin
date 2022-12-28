"""
Câu 7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được
một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím.
"""


def find_number_next(p, a, n):
    for i in range(p + 1, n + 1):
        if i in a:
            if a[i] == 1:
                return i
    return None


def sift_prime(n):  # sàng nguyên tố
    a = {x: 1 for x in range(2, n + 1)}
    p = 2
    while p != None:
        for i in range(p, n + 1):
            if p * i <= n and p * i in a:
                del a[p * i]
        p = find_number_next(p, a, n)
    return list(a)


def reverse(number) -> int:
    number_reverse = 0
    while number > 0:
        r = int(number % 10)
        number_reverse = number_reverse * 10 + r
        number = int(number / 10)
    return number_reverse


if __name__ == '__main__':
    number_n = int(input("Nhập n = "))
    p = sift_prime(number_n)
    for i in range(2, number_n + 1):
        j = reverse(i)
        if i in p and j in p:
            print(i, end=" ")

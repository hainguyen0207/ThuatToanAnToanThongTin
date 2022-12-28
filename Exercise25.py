'''
Câu 25. Cho 2 số M và N thoả mãn điều kiện: 1<=N<=10000; 2<M<=100;
Hãy viết chương trình xác định xem số N có thể được phân tích thành
tổng của M số nguyên tố hay không? Nếu có thì in
ra các số đó.
'''
import random


def square_integer(a, r, n):
    k = []
    while r > 0:
        k.append(r % 2)
        r //= 2
    temp = a
    if k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        temp = (temp * temp) % n
        if k[i] == 1:
            b = (b * temp) % n
    return b


def miller_rabin(n, t):  # dùng miller để xét nguyên tố
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    s = 0
    x = n - 1
    while x % 2 == 0:
        s += 1
        x //= 2
    r = x
    for i in range(1, t + 1):
        a = random.randint(2, n - 2)
        y = square_integer(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = y ** 2 % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True


def result(array_prime, subsets, subsetSize, sum, current, target, r):
    if (target == sum):  # nếu tổng hiện tại bằng tổng mục tiêu
        r.append(subsets[0:subsetSize])
        # nếu chỉ số phần tử kế tiếp còn trong biên mảng tập đầu vào
        # và tổng hiện thời trừ phần tử đang xét + tổng phần tử kế tiếp
        # nhỏ hơn tổng mục tiêu
        if current + 1 < len(array_prime) and sum - array_prime[current] \
                + array_prime[current + 1] <= target:
            # tiếp tục đệ quy để tìm tập kết quả tiếp theo,
            # loại bỏ phần tử hiện tại
            result(array_prime, subsets, subsetSize - 1,
                   sum - array_prime[current], current + 1,
                   target, r)

    else:
        # kiểm tra ràng buộc chỉ số phần tử
        if current < len(array_prime) and sum + array_prime[current] <= target:
            # sinh các node dọc theo chiều rộng của mảng đầu vào
            for i in range(current, len(array_prime)):
                subsets[subsetSize] = array_prime[i]
                if sum + array_prime[i] <= target:  # nếu tổng hiện thời với
                    # phần tử đang xét nhỏ hơn hoặc bằng mục tiêu
                    # xem xét tìm tổng tập con của level tiếp theo
                    result(array_prime, subsets, subsetSize + 1,
                           sum + array_prime[i], i + 1, target, r)


def convert_prime(number_n):
    p = []
    for i in range(2, number_n + 1):
        if miller_rabin(i, i):
            p.append(i)
    return p


if __name__ == '__main__':
    number_n = int(input('Nhập số n = '))
    number_m = 3
    array_prime = convert_prime(number_n)
    array_prime.sort()
    subsets = [0] * number_n
    r = []
    p = []
    result(array_prime, subsets, 0, 0, 0, number_n, r)
    for e in r:
        if len(e) == number_m:
            p.append(e)
    if len(p) > 0:
        for e in p:
            print(e)
    else:
        print("NO")

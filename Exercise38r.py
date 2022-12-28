'''
Câu 38. Tìm nghịch đảo của một số a trong trường 𝐹𝑝 với a và p
 được nhập từ bàn phím.
'''


def inversion(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = int(v // u)
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return (x1 + p) % p


p = int(input('Nhập số SNT P = '))
a = int(input(f'Nhập a = [1 {p - 1} ]'))
print(inversion(a, p))

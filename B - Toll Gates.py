ai, bi, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cupon = [list(map(int, input().split())) for _ in range(m)]

min = min(a) + min(b)

######

for i in cupon:
    # print(i)

    ca = a[i[0] - 1]
    cb = b[i[1] - 1]
    dis = ca + cb - i[2]

    if dis < min:
        min = dis
print(min)

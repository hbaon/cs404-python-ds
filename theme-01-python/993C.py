t = int(input())
for _ in range(t):
    # m = int(input())
    # a = int(input())
    # b = int(input())
    # c = int(input())
    m, a, b, c = map(int, input().split() )
    # ['10', '5', '5', '10']
    t1 = min(m, a)
    t2 = min(m, b)
    du1 = m - t1
    du2 = m - t2
    tong = t1 + t2 + min(du1 + du2, c)
    print(tong)
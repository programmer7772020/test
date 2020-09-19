def lcm(m, n):
    if m > n:
        mx = m
        mn = n
    else:
        mx = n
        mn = m
    while (mx % mn) != 0:
        mn1 = mn
        mn = mx % mn
        mx = mn1
    k = m * n / mn
    a=3
    return k

print(lcm(16,24))
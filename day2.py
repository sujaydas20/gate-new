def fun(n):
    if n == 0:
        return 1
    return n * fun(n - 1)

print(fun(4))




def fun(x):
    x[0] = x[0] + 10
    return x

a = [5, 2, 3]
b = fun(a)

print(a)
print(b)
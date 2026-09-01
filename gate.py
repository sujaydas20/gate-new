def f(x):
    return x + 2

def g(x):
    return f(x) * 2

x = g(3)
print(f(x))






def fun(x):
    x.append(10)
    return x

a = [1, 2]
b = fun(a)

print(a)
print(b)
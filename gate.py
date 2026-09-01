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





s = 0

for i in range(10, 2, -2):
    s += i

print(s)









x = 5
y = 10

if x < 10 and y > 5:
    x = x + y

print(x)









def fun(n):
    if n <= 1:
        return n
    return fun(n - 1) + fun(n - 2)

print(fun(5))
def modify(x):
    x.append(10)
    x = x + [20]
    return x

a = [1, 2]
b = modify(a)

print(a)
print(b)




# q2
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)

print(f(5))
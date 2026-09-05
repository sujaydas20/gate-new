def modify(x):
    x.append(10)
    x = x + [20]
    return x

a = [1, 2]
b = modify(a)

print(a)
print(b)
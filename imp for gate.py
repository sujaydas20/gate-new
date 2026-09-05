
# q1
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




# q3
a = [10, 20, 30, 40, 50, 60]

x = a[1:5:2]
y = a[::-2]

print(x)
print(y)






# q4
d = {"a": 2, "b": 3}

d["c"] = d["a"] + d["b"]
d["a"] = d["c"] * 2

print(d)
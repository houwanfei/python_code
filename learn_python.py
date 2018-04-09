from functools import reduce
L = [['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'], ['Michael', 'Sarah', 'Tracy']]

print(L[2:3])

d = {'a':1, 'b':2, 'c':3}

for key in d:
    print(d.get(key))

for x,y in [(1, 2), (2, 3), (3, 4)]:
    print(x, y)
for k, v in d.items():
    print(k, "=", v)
g = (x * x for x in range(10))
for n in g:
    print(n)

def f(x):
   return  x*x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

def add(x, y):
    return x+y
print(reduce(add, [1, 2, 3, 4, 5, 6, 7]))

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
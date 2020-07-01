# Zip, Enumerate
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print(a, b)

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)

print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print("Enumerate")
    print(i, a, b)

print("----------------------------")

# Lamda
f = lambda x, y: x + y
print(f(1, 4))
print("---------------------------")

# Map
ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
# list를 꼭 붙여야 함
print(list(map(f, ex)))
print("-------------------")

# Reduce
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print("-----------------------")


# Asterisk
# 한번에 여러개 변수 넘겨줄때 사용
def aster(a, *args):
    print(a, args)


aster(1, 2, 3, 4, 5)


def kaster(a, **kargs):
    print(a, kargs)


kaster(1, b=2, c=3, d=4)

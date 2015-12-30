def f(x): 
    return x % 3 == 0 or x % 5 == 0

print filter(f, range(2, 6))

def cube(x): 
    return x*x*x
print map(cube, range(1, 11))

def add(x,y): return x+y
print reduce(add, range(1, 6))

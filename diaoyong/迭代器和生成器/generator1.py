def f(n):
    i=1
    while (i<5):
        yield i
        i+=1

g = f(5)

for i in g:
    print(i)
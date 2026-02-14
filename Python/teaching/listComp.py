x = [(lambda y: True if y %2==0 else False)(x+1) for x in range(0,10)]

y = [[[x*n*r for n in range(0,10)] for r in range(0,10)] for x in range(0,10)]

y=[]
for x in range(0,10):
    y.append([])
    for n in range(0,10):
        y[x].append([])
        for r in range(0,10):
            y[x][n].append(x*n*r)

z = [x for x in range(0,10) if x % 2 == 0]

print(x)
print(y)
print(z)
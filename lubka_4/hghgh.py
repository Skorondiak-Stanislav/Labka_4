v = []
n = int(input('n='))

for i in range(n):
    a = [float(input('Введіть координату вектора а {0} :'.format(i))) for i in range(1, n + 1)]
    a = a[i] * 2
for p in range(n):
    c = [float(input('Введіть координату вектора c {0} :'.format(p))) for i in range(1, n + 1)]
    c = c[p] * 2
    x = a +c
for o in range(n):
    b = [float(input('Введіть координату вектора b {0} :'.format(o))) for o in range(1, n + 1)]
    b = -b[o] * 3
for i in range(n):
    a = [float(input('Введіть координату вектора а {0} :'.format(i))) for i in range(1, n + 1)]
    a = a[i] * 3
    s = a - b
    c = x - s
    v.append(c)
print(v)
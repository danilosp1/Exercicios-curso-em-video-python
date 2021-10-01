import math

n = 1
for i in range(8):
    for x in range(n + 1):
        print(int(math.factorial(n)/(math.factorial(x)*math.factorial(n - x))), end=' ')
    n += 1
    print('')

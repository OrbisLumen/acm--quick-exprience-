from random import randint, choice

T = 1
print(T)

x, y = randint(-5, 5), randint(-5, 5)
len = 10

print(x, y, len)
print(''.join([choice(['L', 'R', 'U', 'D']) for _ in range(len)]))

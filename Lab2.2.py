import random
x = random.sample(range(0, 7), 5)
y = random.random()
print(x)
print(y)
mx = max(x)
print(mx)
z = mx//y
print(z)
f = int(z)
i = f
while i != 1:
    i -= 1
    f = f*i
print(f)

s = set('4785fj45')
r = set('fgh82j4774')
print(s)
k =tuple(s & r)
t = (s, r)
print(k)
print(t)
print(k[0:3])

print(k[::-1])
l = list(k+t)
print(l)

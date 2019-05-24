import string
s = (string.ascii_lowercase+string.ascii_uppercase+string.digits)
print(s)
print(s[0])
print(s[-1])
print(s[2], s[-3])
print(s[0:8])
print(s[3::3])
e = int(len(s))
i = 3
while i < e:
    print(s[i])
    i += 3
m = e//2
print(s[m])

print(s[::-1])



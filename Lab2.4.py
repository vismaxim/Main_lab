import string
s = (string.ascii_lowercase+string.ascii_uppercase)
l = list(s)
for i in range(0, 10):
    l.append(i)
print(l)
print(l[0])
print(l[-1])
print(l[2], l[-3])
print(l[0:10])
print(l[2::2])
for i in l:
    if type(i) == int:
        print(i)
print(l[::-1])
s = str(l)

string = ''
for i in l:
    string.join(str(i))

print(string)
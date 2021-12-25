a = {5:"a", "a":5}
b = 10
c = "b"
d = "10"

a[b] = {c:b}
print(a)
a.__delitem__(b)
print(a)
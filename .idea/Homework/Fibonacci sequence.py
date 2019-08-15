a0=0
a1=1
c=[a0,a1]
for i in range(100):
    a0,a1=a1,a0+a1
    c.append(a1)
print(c)
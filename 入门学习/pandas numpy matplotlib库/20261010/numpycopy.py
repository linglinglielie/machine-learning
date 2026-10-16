import numpy as np
a=np.arange(4)
print(a)
b=a
c=a
d=b
a[0]=11
print(a)
print(b)
d[1:3]=[22,33]
print(a)
print(d)
b=a.copy()
print(b)
a[3]=40
print(a)
print(b)